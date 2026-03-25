from docx import Document as DocxDocument
import re


HEADER_INLINE_RE = re.compile(r"<header>(.*?)</header>(.*)")


# custom parser to split document by tags <header> that were added as RuleBasedChunking strategy
def split_by_docs(path: str) -> list[dict]:
    doc = DocxDocument(path)

    sections = []
    section_id = 1
    current_header = None
    current_lines = []
    inside_header = False
    header_lines = []

    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue

        inline_match = HEADER_INLINE_RE.fullmatch(text)
        if inline_match:
            if current_header:
                sections.append(
                    {
                        "section_id": section_id,
                        "header": current_header,
                        "content": "\n".join(current_lines).strip(),
                    }
                )
                section_id += 1

            current_header = inline_match.group(1).strip() or None
            current_lines = []

            trailing_text = inline_match.group(2).strip()
            if trailing_text:
                current_lines.append(trailing_text)
            continue

        if text == "<header>":
            if current_header:
                sections.append(
                    {
                        "section_id": section_id,
                        "header": current_header,
                        "content": "\n".join(current_lines).strip(),
                    }
                )
                section_id += 1
            inside_header = True
            header_lines = []
            current_lines = []
            continue

        if text == "</header>":
            current_header = " ".join(header_lines).strip() or None
            inside_header = False
            continue

        if inside_header:
            header_lines.append(text)
            continue

        if current_header:
            current_lines.append(text)

    if current_header:
        sections.append(
            {
                "section_id": section_id,
                "header": current_header,
                "content": "\n".join(current_lines).strip(),
            }
        )

    return sections
