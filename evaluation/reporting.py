from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def _stringify(value: Any) -> str:
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
        "| " + " | ".join(_stringify(row.get(column, "")) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def export_retrieval_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Retrieval Evaluation Report",
) -> Path:
    metric_columns = [
        column
        for column in report_df.columns
        if column.startswith(("precision", "recall", "ndcg"))
        or column in {"mrr", "context_relevance"}
    ]
    summary_df = report_df[metric_columns].mean().to_frame(name="mean").T.round(3)

    lines = [f"# {title}", ""]
    if notebook_path:
        lines.append(f"Source notebook: `{notebook_path}`")
        lines.append("")

    lines.extend(
        [
            "## Summary",
            "",
            f"- Evaluated questions: {len(report_df)}",
            f"- Mean precision@5: {summary_df.iloc[0].get('precision@5', 0):.3f}",
            f"- Mean recall@5: {summary_df.iloc[0].get('recall@5', 0):.3f}",
            f"- Mean MRR: {summary_df.iloc[0].get('mrr', 0):.3f}",
            f"- Mean nDCG@5: {summary_df.iloc[0].get('ndcg@5', 0):.3f}",
            f"- Mean context relevance: {summary_df.iloc[0].get('context_relevance', 0):.3f}",
            "",
            "## Final Metrics",
            "",
            _markdown_table(
                summary_df.reset_index(names="row").to_dict(orient="records"),
                ["row", *summary_df.columns.tolist()],
            ),
            "",
            "## Per-question Results",
            "",
        ]
    )

    for item in question_reports:
        lines.extend(
            [
                f"### Question {item['index']}/{item['total']}",
                "",
                f"**Query:** {item['question']}",
                "",
                f"**Relevant docs:** `{item['relevant_docs']}`",
                "",
                "Metrics:",
                "",
                _markdown_table(
                    [item["metrics"]],
                    [
                        column
                        for column in item["metrics"].keys()
                        if column.startswith(("precision", "recall", "ndcg"))
                        or column in {"mrr", "context_relevance"}
                    ],
                ),
                "",
                "Retrieved documents:",
                "",
                _markdown_table(
                    item["doc_rows"],
                    ["rank", "hit", "section_id", "title", "score", "preview"],
                ),
                "",
            ]
        )

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return path


def export_groundedness_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Groundedness Evaluation Report",
) -> Path:
    summary_df = report_df[["groundedness"]].mean().to_frame(name="mean").T.round(3)

    lines = [f"# {title}", ""]
    if notebook_path:
        lines.append(f"Source notebook: `{notebook_path}`")
        lines.append("")

    lines.extend(
        [
            "## Summary",
            "",
            f"- Evaluated questions: {len(report_df)}",
            f"- Mean groundedness: {summary_df.iloc[0].get('groundedness', 0):.3f}",
            "",
            "## Final Metrics",
            "",
            _markdown_table(
                summary_df.reset_index(names="row").to_dict(orient="records"),
                ["row", *summary_df.columns.tolist()],
            ),
            "",
            "## Per-question Results",
            "",
        ]
    )

    for item in question_reports:
        lines.extend(
            [
                f"### Question {item['index']}/{item['total']}",
                "",
                f"**Query:** {item['question']}",
                "",
                f"**Groundedness:** {item['groundedness']:.3f}",
                "",
                f"**Relevant docs:** `{item['relevant_docs']}`",
                "",
                f"**Retrieved docs:** `{item['retrieved_docs']}`",
                "",
                "**Reference answer:**",
                "",
                item["reference_answer"],
                "",
                "**Generated answer:**",
                "",
                item["generated_answer"],
                "",
                "Retrieved documents:",
                "",
                _markdown_table(
                    item["doc_rows"],
                    ["rank", "section_id", "title", "rerank_score", "preview"],
                ),
                "",
            ]
        )

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return path


def export_answer_relevance_report_to_markdown(
    report_df: pd.DataFrame,
    question_reports: list[dict[str, Any]],
    output_path: str | Path,
    *,
    notebook_path: str | Path | None = None,
    title: str = "FAQ Answer Relevance Evaluation Report",
) -> Path:
    summary_df = report_df[["answer_relevance"]].mean().to_frame(name="mean").T.round(3)

    lines = [f"# {title}", ""]
    if notebook_path:
        lines.append(f"Source notebook: `{notebook_path}`")
        lines.append("")

    lines.extend(
        [
            "## Summary",
            "",
            f"- Evaluated questions: {len(report_df)}",
            f"- Mean answer relevance: {summary_df.iloc[0].get('answer_relevance', 0):.3f}",
            "",
            "## Final Metrics",
            "",
            _markdown_table(
                summary_df.reset_index(names="row").to_dict(orient="records"),
                ["row", *summary_df.columns.tolist()],
            ),
            "",
            "## Per-question Results",
            "",
        ]
    )

    for item in question_reports:
        lines.extend(
            [
                f"### Question {item['index']}/{item['total']}",
                "",
                f"**Query:** {item['question']}",
                "",
                f"**Answer relevance:** {item['answer_relevance']:.3f}",
                "",
                f"**Relevant docs:** `{item['relevant_docs']}`",
                "",
                f"**Retrieved docs:** `{item['retrieved_docs']}`",
                "",
                "**Reference answer:**",
                "",
                item["reference_answer"],
                "",
                "**Generated answer:**",
                "",
                item["generated_answer"],
                "",
                "Retrieved documents:",
                "",
                _markdown_table(
                    item["doc_rows"],
                    ["rank", "section_id", "title", "rerank_score", "preview"],
                ),
                "",
            ]
        )

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return path
