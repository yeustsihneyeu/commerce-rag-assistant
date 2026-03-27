from __future__ import annotations

from html import escape
from numbers import Real
from pathlib import Path
from typing import Any

import pandas as pd
from IPython.display import HTML, display


def _stringify_markdown_value(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.3f}"
    if isinstance(value, list):
        return "[" + ", ".join(str(item) for item in value) + "]"
    return str(value)


def _markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| "
        + " | ".join(
            _stringify_markdown_value(row.get(column, "")) for column in columns
        )
        + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def _write_markdown_report(lines: list[str], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return path


def _start_report(title: str, notebook_path: str | Path | None = None) -> list[str]:
    lines = [f"# {title}", ""]
    if notebook_path:
        lines.extend([f"Source notebook: `{notebook_path}`", ""])
    return lines


def _append_section(lines: list[str], heading: str, body_lines: list[str]) -> None:
    lines.extend([heading, "", *body_lines, ""])


def _append_summary_tables_section(
    lines: list[str],
    tables: list[tuple[str, pd.DataFrame, str | None]],
) -> None:
    lines.extend(["## Summary Tables", ""])
    for title, df, index_name in tables:
        table_df = df.reset_index(names=index_name) if index_name else df
        lines.extend(
            [
                f"### {title}",
                "",
                _markdown_table(
                    table_df.to_dict(orient="records"),
                    table_df.columns.tolist(),
                ),
                "",
            ]
        )


def _append_detail_block(
    lines: list[str],
    title: str,
    fields: list[tuple[str, Any]],
    *,
    text_blocks: list[tuple[str, str]] | None = None,
    table_blocks: list[tuple[str, list[dict[str, Any]], list[str]]] | None = None,
) -> None:
    lines.extend([f"### {title}", ""])

    for label, value in fields:
        lines.extend([f"**{label}:** {value}", ""])

    for heading, text in text_blocks or []:
        lines.extend([f"**{heading}:**", "", str(text), ""])

    for heading, rows, columns in table_blocks or []:
        lines.extend([f"{heading}:", "", _markdown_table(rows, columns), ""])


def _append_detail_results_heading(lines: list[str]) -> None:
    lines.extend(["## Detailed Results", ""])


def get_node_metadata(item: Any) -> dict[str, Any]:
    if hasattr(item, "node"):
        return (
            getattr(item.node, "metadata", None)
            or getattr(item, "metadata", None)
            or {}
        )
    return getattr(item, "metadata", {}) or {}


def get_node_id(item: Any) -> Any:
    node = getattr(item, "node", item)
    metadata = get_node_metadata(item)
    return (
        metadata.get("product_id")
        or metadata.get("section_id")
        or metadata.get("uuid")
        or getattr(node, "node_id", None)
        or getattr(node, "id_", None)
    )


def get_node_text(item: Any) -> str:
    node = getattr(item, "node", item)
    if hasattr(node, "get_content"):
        return node.get_content()
    return getattr(node, "text", "") or ""


def get_node_score(item: Any) -> float | None:
    score = getattr(item, "score", None)
    if isinstance(score, bool) or not isinstance(score, Real):
        return None
    return round(float(score), 4)


def preview_text(text: Any, max_len: int = 220) -> str:
    cleaned = " ".join(str(text).split())
    if len(cleaned) <= max_len:
        return cleaned
    return cleaned[: max_len - 3] + "..."


def format_node_metadata(
    metadata: dict[str, Any],
    *,
    keys: list[str] | None = None,
    max_len: int = 220,
) -> str:
    selected_keys = keys or [
        "brand",
        "color",
        "category",
        "occasion",
        "price",
    ]
    parts = []

    for key in selected_keys:
        value = metadata.get(key)
        if value in (None, "", [], {}):
            continue
        parts.append(f"{key}={value}")

    if not parts:
        return "-"

    return preview_text(", ".join(parts), max_len=max_len)


def build_retrieved_doc_rows(
    nodes: list[Any], *, preview_len: int = 220
) -> tuple[list[Any], list[dict[str, Any]]]:
    retrieved_docs = []
    doc_rows = []

    for rank, item in enumerate(nodes, start=1):
        metadata = get_node_metadata(item)
        node_id = get_node_id(item)
        retrieved_docs.append(node_id)
        doc_rows.append(
            {
                "rank": rank,
                "section_id": node_id,
                "title": metadata.get("section_title", "-"),
                "rerank_score": get_node_score(item),
                "preview": preview_text(get_node_text(item), max_len=preview_len),
            }
        )

    return retrieved_docs, doc_rows


def build_retrieval_doc_rows(
    nodes: list[Any],
    relevant_docs: list[Any],
    *,
    preview_len: int = 180,
) -> list[dict[str, Any]]:
    relevant_doc_ids = set(relevant_docs)
    doc_rows = []

    for rank, item in enumerate(nodes, start=1):
        metadata = get_node_metadata(item)
        node_id = get_node_id(item)
        doc_rows.append(
            {
                "rank": rank,
                "hit": "yes" if node_id in relevant_doc_ids else "no",
                "section_id": node_id,
                "title": metadata.get("section_title", "-"),
                "score": get_node_score(item),
                "metadata": format_node_metadata(metadata),
                "preview": preview_text(get_node_text(item), max_len=preview_len),
            }
        )

    return doc_rows


def display_metric_cards(metrics: dict[str, float], *, columns: int = 2) -> None:
    metrics_html = "".join(
        f"""
        <div style='padding:12px 14px;border:1px solid #d0d7de;border-radius:10px;background:#f6f8fa;'>
            <div style='font-size:12px;color:#57606a;text-transform:uppercase;letter-spacing:.04em;'>{escape(name)}</div>
            <div style='font-size:24px;font-weight:700;color:#24292f;'>{value:.3f}</div>
        </div>
        """
        for name, value in metrics.items()
    )
    display(
        HTML(
            f"<div style='display:grid;grid-template-columns:repeat({columns}, minmax(0, 1fr));gap:12px;margin:12px 0 18px;'>{metrics_html}</div>"
        )
    )


def display_eval_question_report(
    *,
    question: str,
    relevant_docs: list[Any],
    metrics: dict[str, float],
    text_blocks: list[tuple[str, str]],
    doc_rows: list[dict[str, Any]],
    index: int,
    total: int,
    metric_columns: int = 2,
) -> None:
    header_html = f"""
    <div style='margin:28px 0 10px;'>
        <div style='font-size:12px;color:#57606a;text-transform:uppercase;letter-spacing:.08em;'>Question {index}/{total}</div>
        <div style='font-size:22px;font-weight:700;margin:6px 0 10px;color:#24292f;'>{escape(question)}</div>
        <div style='padding:12px 14px;background:#fff8c5;border:1px solid #e3d279;border-radius:10px;'>
            <div style='font-size:12px;color:#57606a;text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px;'>Relevant docs</div>
            <div style='font-size:16px;font-weight:600;color:#24292f;'>{escape(str(relevant_docs))}</div>
        </div>
    </div>
    """
    display(HTML(header_html))
    display_metric_cards(metrics, columns=metric_columns)
    for label, text in text_blocks:
        display(
            HTML(
                f"<p style='margin:8px 0 12px;'><strong>{escape(label)}:</strong> {escape(str(text))}</p>"
            )
        )
    display(pd.DataFrame(doc_rows))


def build_eval_question_report(
    *,
    question: str,
    relevant_docs: list[Any],
    retrieved_docs: list[Any],
    doc_rows: list[dict[str, Any]],
    extra_fields: dict[str, Any],
    index: int,
    total: int,
) -> dict[str, Any]:
    return {
        "index": index,
        "total": total,
        "question": question,
        "relevant_docs": list(relevant_docs),
        "retrieved_docs": retrieved_docs,
        "doc_rows": doc_rows,
        **extra_fields,
    }


def _label_name(label: Any) -> str:
    return "none" if label is None else str(label)


def _safe_divide(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def export_retrieval_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "Retrieval Evaluation Report",
) -> Path:
    metric_columns = [
        column
        for column in report_df.columns
        if column.startswith(("precision", "recall", "ndcg"))
        or column in {"mrr", "context_relevance"}
    ]
    summary_df = report_df[metric_columns].mean().to_frame(name="mean").T.round(3)
    summary_row = summary_df.iloc[0]

    precision_column = next(
        (column for column in metric_columns if column.startswith("precision")),
        None,
    )
    recall_column = next(
        (column for column in metric_columns if column.startswith("recall")),
        None,
    )
    ndcg_column = next(
        (column for column in metric_columns if column.startswith("ndcg")),
        None,
    )

    lines = _start_report(title, notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated questions: {len(report_df)}",
            (
                f"- Mean {precision_column}: {summary_row[precision_column]:.3f}"
                if precision_column
                else "- Mean precision: -"
            ),
            (
                f"- Mean {recall_column}: {summary_row[recall_column]:.3f}"
                if recall_column
                else "- Mean recall: -"
            ),
            f"- Mean MRR: {summary_row.get('mrr', 0):.3f}",
            (
                f"- Mean {ndcg_column}: {summary_row[ndcg_column]:.3f}"
                if ndcg_column
                else "- Mean nDCG: -"
            ),
            f"- Mean context relevance: {summary_row.get('context_relevance', 0):.3f}",
        ],
    )
    _append_summary_tables_section(lines, [("Final Metrics", summary_df, "row")])
    _append_detail_results_heading(lines)

    for item in question_reports:
        metric_rows = [item["metrics"]]
        metric_columns = [
            column
            for column in item["metrics"].keys()
            if column.startswith(("precision", "recall", "ndcg"))
            or column in {"mrr", "context_relevance"}
        ]
        _append_detail_block(
            lines,
            f"Question {item['index']}/{item['total']}",
            [
                ("Query", item["question"]),
                ("Retrieval metadata", item.get("retrieval_metadata", "-")),
                ("Relevant docs", f"`{item['relevant_docs']}`"),
            ],
            table_blocks=[
                ("Metrics", metric_rows, metric_columns),
                (
                    "Retrieved documents",
                    item["doc_rows"],
                    ["rank", "hit", "section_id", "title", "score", "metadata", "preview"],
                ),
            ],
        )

    return _write_markdown_report(lines, output_path)


def export_groundedness_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Groundedness Evaluation Report",
) -> Path:
    summary_df = report_df[["groundedness"]].mean().to_frame(name="mean").T.round(3)

    lines = _start_report(title, notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated questions: {len(report_df)}",
            f"- Mean groundedness: {summary_df.iloc[0].get('groundedness', 0):.3f}",
        ],
    )
    _append_summary_tables_section(lines, [("Final Metrics", summary_df, "row")])
    _append_detail_results_heading(lines)

    for item in question_reports:
        _append_detail_block(
            lines,
            f"Question {item['index']}/{item['total']}",
            [
                ("Query", item["question"]),
                ("Groundedness", f"{item['groundedness']:.3f}"),
                ("Relevant docs", f"`{item['relevant_docs']}`"),
                ("Retrieved docs", f"`{item['retrieved_docs']}`"),
            ],
            text_blocks=[
                ("Reference answer", item["reference_answer"]),
                ("Generated answer", item["generated_answer"]),
            ],
            table_blocks=[
                (
                    "Retrieved documents",
                    item["doc_rows"],
                    ["rank", "section_id", "title", "rerank_score", "preview"],
                )
            ],
        )

    return _write_markdown_report(lines, output_path)


def export_groundedness_calibration_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Groundedness Calibration Report",
) -> Path:
    metric_columns = [
        column
        for column in [
            "predicted_groundedness",
            "accuracy",
            "precision",
            "recall",
            "f1",
        ]
        if column in report_df.columns
    ]
    summary_df = report_df[metric_columns].mean().to_frame(name="mean").T.round(3)
    summary_row = summary_df.iloc[0] if not summary_df.empty else {}

    lines = _start_report(title, notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated samples: {len(report_df)}",
            f"- Mean predicted groundedness: {summary_row.get('predicted_groundedness', 0):.3f}",
            f"- Accuracy: {summary_row.get('accuracy', 0):.3f}",
            f"- Precision: {summary_row.get('precision', 0):.3f}",
            f"- Recall: {summary_row.get('recall', 0):.3f}",
            f"- F1: {summary_row.get('f1', 0):.3f}",
        ],
    )
    _append_summary_tables_section(lines, [("Final Metrics", summary_df, "row")])
    _append_detail_results_heading(lines)

    for item in question_reports:
        _append_detail_block(
            lines,
            f"Sample {item['index']}/{item['total']}",
            [
                ("Query", item["question"]),
                ("Answer type", f"`{item['answer_type']}`"),
                ("Predicted groundedness", f"{item['predicted_groundedness']:.3f}"),
                ("Predicted label", f"`{item['predicted_label']}`"),
                ("Gold label", f"`{item['grounded_label']}`"),
                ("Match", f"`{item['is_correct']}`"),
                ("Relevant docs", f"`{item['relevant_docs']}`"),
            ],
            text_blocks=[
                ("Reference answer", item["reference_answer"]),
                ("Candidate answer", item["candidate_answer"]),
            ],
            table_blocks=[("Contexts", item["context_rows"], ["index", "context"])],
        )

    return _write_markdown_report(lines, output_path)


def build_groundedness_calibration_summary(
    report_df: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "samples": len(report_df),
                "threshold": threshold,
                "mean_groundedness_score": report_df["groundedness_score"].mean(),
                "accuracy": report_df["label_match"].mean(),
            }
        ]
    ).round(3)


def build_groundedness_calibration_details(report_df: pd.DataFrame) -> pd.DataFrame:
    return (
        report_df[
            [
                "question",
                "answer_type",
                "groundedness_score",
                "predicted_is_grounded",
                "expected_is_grounded",
                "label_match",
            ]
        ]
        .copy()
        .round({"groundedness_score": 3})
    )


def save_groundedness_calibration_report(
    report_df: pd.DataFrame,
    output_path: str | Path,
    *,
    threshold: float,
    notebook_path: str = "notebooks/14_faq_groundedness_calibrating.ipynb",
) -> Path:
    summary_df = build_groundedness_calibration_summary(
        report_df=report_df,
        threshold=threshold,
    )
    details_df = build_groundedness_calibration_details(report_df)

    lines = _start_report("FAQ Groundedness Calibration Report", notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated samples: {len(report_df)}",
            f"- Threshold: {threshold:.3f}",
            f"- Mean groundedness score: {summary_df.iloc[0].get('mean_groundedness_score', 0):.3f}",
            f"- Accuracy: {summary_df.iloc[0].get('accuracy', 0):.3f}",
        ],
    )
    _append_summary_tables_section(
        lines,
        [
            ("Final Metrics", summary_df, None),
            ("Sample Results", details_df, None),
        ],
    )

    return _write_markdown_report(lines, output_path)


def save_base_prompting_report(
    report_df: pd.DataFrame,
    output_path: str | Path,
    *,
    notebook_path: str = "notebooks/11_base_prompting.ipynb",
) -> Path:
    summary_df = pd.DataFrame(
        [
            {
                "samples": len(report_df),
                "greet_true_cases": (
                    int(report_df["greet"].sum()) if "greet" in report_df.columns else 0
                ),
                "greet_false_cases": (
                    int((~report_df["greet"]).sum())
                    if "greet" in report_df.columns
                    else 0
                ),
            }
        ]
    )

    details_columns = [
        column
        for column in ["query", "greet", "chat_history", "response"]
        if column in report_df.columns
    ]
    details_df = report_df[details_columns].copy()

    lines = _start_report("Base Prompting Report", notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated samples: {len(report_df)}",
            (
                f"- Greeting cases: {int(report_df['greet'].sum())}"
                if "greet" in report_df.columns
                else "- Greeting cases: -"
            ),
            (
                f"- Non-greeting cases: {int((~report_df['greet']).sum())}"
                if "greet" in report_df.columns
                else "- Non-greeting cases: -"
            ),
        ],
    )
    _append_summary_tables_section(
        lines,
        [
            ("Final Metrics", summary_df, None),
            ("Sample Results", details_df, None),
        ],
    )

    return _write_markdown_report(lines, output_path)


def build_answer_relevance_calibration_summary(
    report_df: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "samples": len(report_df),
                "threshold": threshold,
                "mean_answer_relevance_score": report_df[
                    "answer_relevance_score"
                ].mean(),
                "accuracy": report_df["label_match"].mean(),
            }
        ]
    ).round(3)


def build_answer_relevance_calibration_details(report_df: pd.DataFrame) -> pd.DataFrame:
    return (
        report_df[
            [
                "question",
                "answer_type",
                "answer_relevance_score",
                "predicted_is_relevant",
                "expected_is_relevant",
                "label_match",
            ]
        ]
        .copy()
        .round({"answer_relevance_score": 3})
    )


def save_answer_relevance_calibration_report(
    report_df: pd.DataFrame,
    output_path: str | Path,
    *,
    threshold: float,
    notebook_path: str = "notebooks/15_faq_answer_relevance_calibrating.ipynb",
) -> Path:
    summary_df = build_answer_relevance_calibration_summary(
        report_df=report_df,
        threshold=threshold,
    )
    details_df = build_answer_relevance_calibration_details(report_df)

    lines = _start_report("FAQ Answer Relevance Calibration Report", notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated samples: {len(report_df)}",
            f"- Threshold: {threshold:.3f}",
            f"- Mean answer relevance score: {summary_df.iloc[0].get('mean_answer_relevance_score', 0):.3f}",
            f"- Accuracy: {summary_df.iloc[0].get('accuracy', 0):.3f}",
        ],
    )
    _append_summary_tables_section(
        lines,
        [
            ("Final Metrics", summary_df, None),
            ("Sample Results", details_df, None),
        ],
    )

    return _write_markdown_report(lines, output_path)


def export_answer_relevance_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Answer Relevance Evaluation Report",
) -> Path:
    summary_df = report_df[["answer_relevance"]].mean().to_frame(name="mean").T.round(3)

    lines = _start_report(title, notebook_path)
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated questions: {len(report_df)}",
            f"- Mean answer relevance: {summary_df.iloc[0].get('answer_relevance', 0):.3f}",
        ],
    )
    _append_summary_tables_section(lines, [("Final Metrics", summary_df, "row")])
    _append_detail_results_heading(lines)

    for item in question_reports:
        _append_detail_block(
            lines,
            f"Question {item['index']}/{item['total']}",
            [
                ("Query", item["question"]),
                ("Answer relevance", f"{item['answer_relevance']:.3f}"),
                ("Relevant docs", f"`{item['relevant_docs']}`"),
                ("Retrieved docs", f"`{item['retrieved_docs']}`"),
            ],
            text_blocks=[
                ("Reference answer", item["reference_answer"]),
                ("Generated answer", item["generated_answer"]),
            ],
            table_blocks=[
                (
                    "Retrieved documents",
                    item["doc_rows"],
                    ["rank", "section_id", "title", "rerank_score", "preview"],
                )
            ],
        )

    return _write_markdown_report(lines, output_path)


def export_class_routing_report_to_markdown(
    results_df: pd.DataFrame,
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "Class Routing Report",
) -> tuple[Path, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    normalized_df = results_df.copy()
    normalized_df["expected"] = normalized_df["expected"].map(_label_name)
    normalized_df["predicted"] = normalized_df["predicted"].map(_label_name)

    classes = ["none", "faq", "product"]
    confusion_rows = []
    class_metrics_rows = []

    for expected in classes:
        row = {"expected": expected}
        for predicted in classes:
            row[predicted] = int(
                (
                    (normalized_df["expected"] == expected)
                    & (normalized_df["predicted"] == predicted)
                ).sum()
            )
        confusion_rows.append(row)

    confusion_df = pd.DataFrame(confusion_rows)

    for label in classes:
        tp = int(
            (
                (normalized_df["expected"] == label)
                & (normalized_df["predicted"] == label)
            ).sum()
        )
        fp = int(
            (
                (normalized_df["expected"] != label)
                & (normalized_df["predicted"] == label)
            ).sum()
        )
        fn = int(
            (
                (normalized_df["expected"] == label)
                & (normalized_df["predicted"] != label)
            ).sum()
        )
        support = int((normalized_df["expected"] == label).sum())

        precision = _safe_divide(tp, tp + fp)
        recall = _safe_divide(tp, tp + fn)
        f1 = _safe_divide(2 * precision * recall, precision + recall)

        class_metrics_rows.append(
            {
                "label": _label_name(label),
                "precision": round(precision, 3),
                "recall": round(recall, 3),
                "f1": round(f1, 3),
                "support": support,
            }
        )

    class_metrics_df = pd.DataFrame(class_metrics_rows)
    summary_df = pd.DataFrame(
        [
            {
                "total_cases": int(len(normalized_df)),
                "accuracy": round(float(normalized_df["is_correct"].mean()), 3),
                "avg_confidence": round(
                    float(normalized_df["confidence"].fillna(0).mean()), 3
                ),
            }
        ]
    )
    per_case_df = normalized_df.copy()

    lines = _start_report(title, notebook_path)
    summary_row = summary_df.iloc[0]
    _append_section(
        lines,
        "## Overview",
        [
            f"- Total cases: {int(summary_row['total_cases'])}",
            f"- Accuracy: {summary_row['accuracy']:.3f}",
            f"- Average confidence: {summary_row['avg_confidence']:.3f}",
        ],
    )
    _append_summary_tables_section(
        lines,
        [
            ("Final Metrics", summary_df, None),
            ("Per-class Metrics", class_metrics_df, None),
            ("Confusion Matrix", confusion_df, None),
            ("Raw Results", per_case_df, None),
        ],
    )
    _append_detail_results_heading(lines)

    for index, row in per_case_df.iterrows():
        _append_detail_block(
            lines,
            f"Case {index + 1}",
            [
                ("Query", row["query"]),
                ("Expected", row["expected"]),
                ("Predicted", row["predicted"]),
                (
                    "Confidence",
                    f"{row['confidence']:.3f}" if pd.notna(row["confidence"]) else "-",
                ),
                ("Correct", "yes" if row["is_correct"] else "no"),
            ],
        )

    path = _write_markdown_report(lines, output_path)
    return path, summary_df, class_metrics_df, confusion_df, per_case_df


def export_reranking_report_to_markdown(
    report_df: pd.DataFrame,
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Reranking Evaluation Report",
) -> tuple[Path, pd.DataFrame]:
    summary_df = pd.DataFrame(
        [
            {
                "questions": int(len(report_df)),
                "precision": round(float(report_df["precision"].mean()), 3),
                "RERANKED_precision": round(
                    float(report_df["RERANKED_precision"].mean()), 3
                ),
                "recall": round(float(report_df["recall"].mean()), 3),
                "RERANKED_recall": round(float(report_df["RERANKED_recall"].mean()), 3),
                "mrr": round(float(report_df["mrr"].mean()), 3),
                "RERANKED_mrr": round(float(report_df["RERANKED_mrr"].mean()), 3),
                "ndcg": round(float(report_df["ndcg"].mean()), 3),
                "RERANKED_ndcg": round(float(report_df["RERANKED_ndcg"].mean()), 3),
            }
        ]
    )

    lines = _start_report(title, notebook_path)
    summary_row = summary_df.iloc[0]
    _append_section(
        lines,
        "## Overview",
        [
            f"- Evaluated questions: {int(len(report_df))}",
            (
                f"- Mean precision: {summary_row['precision']:.3f} -> "
                f"{summary_row['RERANKED_precision']:.3f}"
            ),
            (
                f"- Mean recall: {summary_row['recall']:.3f} -> "
                f"{summary_row['RERANKED_recall']:.3f}"
            ),
            f"- Mean MRR: {summary_row['mrr']:.3f} -> {summary_row['RERANKED_mrr']:.3f}",
            (
                f"- Mean nDCG: {summary_row['ndcg']:.3f} -> "
                f"{summary_row['RERANKED_ndcg']:.3f}"
            ),
        ],
    )
    _append_summary_tables_section(lines, [("Final Metrics", summary_df, None)])
    _append_detail_results_heading(lines)

    for index, row in report_df.iterrows():
        metrics_row = {
            "precision": row["precision"],
            "RERANKED_precision": row["RERANKED_precision"],
            "recall": row["recall"],
            "RERANKED_recall": row["RERANKED_recall"],
            "mrr": row["mrr"],
            "RERANKED_mrr": row["RERANKED_mrr"],
            "ndcg": row["ndcg"],
            "RERANKED_ndcg": row["RERANKED_ndcg"],
        }
        _append_detail_block(
            lines,
            f"Question {index + 1}",
            [
                ("Query", row["question"]),
                ("Relevant docs", row["relevant_docs"]),
                ("Retrieved docs", row["retrieved_docs"]),
                ("Reranked docs", row["RERANKED_retrieved_docs"]),
            ],
            table_blocks=[("Metrics", [metrics_row], list(metrics_row.keys()))],
        )

    path = _write_markdown_report(lines, output_path)
    return path, summary_df
