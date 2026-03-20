import ast
import csv
import json
import re
from html import unescape
from pathlib import Path


NA_VALUES = {"", "na", "n/a", "none", "null"}


def clean_text(value: str | None) -> str | None:
    if value is None:
        return None

    text = unescape(str(value)).strip()
    text = re.sub(r"\s+", " ", text)

    if text.lower() in NA_VALUES:
        return None

    return text


def pretty_phrase(value: str | None) -> str | None:
    text = clean_text(value)
    if not text:
        return None

    lowered = text.lower()
    return lowered[:1].upper() + lowered[1:]


def combine_parts(*parts: str | None) -> str | None:
    items: list[str] = []

    for part in parts:
        text = clean_text(part)
        if not text:
            continue
        if text.lower() not in {item.lower() for item in items}:
            items.append(text)

    if not items:
        return None

    return " ".join(items)


def parse_attributes(raw_attributes: str | None) -> dict[str, str]:
    if not raw_attributes:
        return {}

    try:
        parsed = ast.literal_eval(raw_attributes)
    except (SyntaxError, ValueError):
        return {}

    if not isinstance(parsed, dict):
        return {}

    result = {}
    for key, value in parsed.items():
        clean_value = clean_text(value)
        if clean_value:
            result[str(key)] = clean_value

    return result


def infer_category(name: str | None, attributes: dict[str, str]) -> str | None:
    top_type = clean_text(attributes.get("Top Type"))
    bottom_type = clean_text(attributes.get("Bottom Type"))
    dupatta = clean_text(attributes.get("Dupatta"))
    explicit_type = clean_text(attributes.get("Type"))
    product_name = clean_text(name)

    if explicit_type:
        return pretty_phrase(explicit_type)

    if top_type == "Kurta" and bottom_type:
        return "Kurta set"

    if product_name:
        lowered = product_name.lower()
        if "kurta" in lowered and bottom_type:
            return "Kurta set"
        if "dress" in lowered:
            return "Dress"
        if "saree" in lowered:
            return "Saree"

    if dupatta and top_type:
        return pretty_phrase(f"{top_type} set")

    return pretty_phrase(top_type)


def build_pattern(attributes: dict[str, str]) -> str | None:
    pattern_type = pretty_phrase(attributes.get("Print or Pattern Type"))
    top_pattern = pretty_phrase(attributes.get("Top Pattern") or attributes.get("Pattern"))

    if pattern_type and top_pattern:
        if pattern_type.lower() == top_pattern.lower():
            return pattern_type
        return f"{pattern_type} {top_pattern.lower()}"

    return pattern_type or top_pattern


def build_sleeves(attributes: dict[str, str]) -> str | None:
    sleeve_length = pretty_phrase(attributes.get("Sleeve Length"))
    sleeve_styling = pretty_phrase(attributes.get("Sleeve Styling"))

    if sleeve_length and sleeve_styling:
        normalized_length = re.sub(r"\s+sleeves?$", "", sleeve_length, flags=re.IGNORECASE)
        normalized_styling = re.sub(r"\s+sleeves?$", "", sleeve_styling, flags=re.IGNORECASE)

        if normalized_length.lower() == normalized_styling.lower():
            return sleeve_length

        if normalized_length.lower() == "sleeveless":
            return f"{normalized_length} {normalized_styling.lower()}"

        return f"{normalized_length} {normalized_styling.lower()} sleeves"

    return sleeve_length or sleeve_styling


def normalize_product_record(row: dict[str, str]) -> dict[str, object]:
    attributes = parse_attributes(row.get("p_attributes"))

    product_id = clean_text(row.get("p_id"))
    if product_id and product_id.endswith(".0"):
        product_id = product_id[:-2]

    record = {
        "product_id": product_id,
        "product": clean_text(row.get("name")),
        "brand": clean_text(row.get("brand")),
        "color": clean_text(row.get("colour")),
        "category": infer_category(row.get("name"), attributes),
        "top_type": pretty_phrase(attributes.get("Top Type")),
        "bottom_type": pretty_phrase(attributes.get("Bottom Type")),
        "dupatta": pretty_phrase(attributes.get("Dupatta")),
        "pattern": build_pattern(attributes),
        "shape": pretty_phrase(attributes.get("Top Shape") or attributes.get("Shape")),
        "neck": pretty_phrase(attributes.get("Neck")),
        "sleeves": build_sleeves(attributes),
        "length": pretty_phrase(attributes.get("Top Length") or attributes.get("Length")),
        "hemline": pretty_phrase(attributes.get("Top Hemline") or attributes.get("Hemline")),
        "top_fabric": pretty_phrase(attributes.get("Top Fabric") or attributes.get("Fabric")),
        "bottom_fabric": pretty_phrase(attributes.get("Bottom Fabric")),
        "dupatta_fabric": pretty_phrase(attributes.get("Dupatta Fabric")),
        "occasion": pretty_phrase(attributes.get("Occasion")),
        "pockets": clean_text(attributes.get("Number of Pockets")),
        "wash_care": pretty_phrase(attributes.get("Wash Care")),
        "price": clean_text(row.get("price")),
        "rating_count": clean_text(row.get("ratingCount")),
        "avg_rating": clean_text(row.get("avg_rating")),
        "image_url": clean_text(row.get("img")),
    }

    filtered_record = {key: value for key, value in record.items() if value is not None}
    filtered_record["text"] = render_rag_text(filtered_record)
    filtered_record["attributes"] = attributes
    return filtered_record


def render_rag_text(record: dict[str, object]) -> str:
    field_order = [
        ("Product", "product"),
        ("Brand", "brand"),
        ("Color", "color"),
        ("Category", "category"),
        ("Top type", "top_type"),
        ("Bottom type", "bottom_type"),
        ("Dupatta", "dupatta"),
        ("Pattern", "pattern"),
        ("Shape", "shape"),
        ("Neck", "neck"),
        ("Sleeves", "sleeves"),
        ("Length", "length"),
        ("Hemline", "hemline"),
        ("Top fabric", "top_fabric"),
        ("Bottom fabric", "bottom_fabric"),
        ("Dupatta fabric", "dupatta_fabric"),
        ("Occasion", "occasion"),
        ("Pockets", "pockets"),
        ("Wash care", "wash_care"),
    ]

    lines = []
    for label, key in field_order:
        value = record.get(key)
        if value:
            lines.append(f"{label}: {value}")

    return "\n".join(lines)


def parse_product_dataset(csv_path: str | Path) -> list[dict[str, object]]:
    path = Path(csv_path)
    records: list[dict[str, object]] = []

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = normalize_product_record(row)
            if not record.get("product_id") or not record.get("text"):
                continue
            records.append(record)

    return records


def build_product_rag_records(
    csv_path: str | Path,
    output_path: str | Path | None = None,
) -> list[dict[str, object]]:
    records = parse_product_dataset(csv_path)

    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    return records
