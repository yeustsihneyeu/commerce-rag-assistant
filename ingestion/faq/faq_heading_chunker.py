from docx import Document as DocxDocument

# custom parser to split document by tags <header> that were added as RuleBasedChunking strategy
def parse_faq_docx(path: str) -> list[dict]:
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

        if text == "<header>":
            if current_header:
                sections.append({
                    "section_id": section_id,
                    "header": current_header,
                    "content": "\n".join(current_lines).strip(),
                })
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
        sections.append({
            "section_id": section_id,
            "header": current_header,
            "content": "\n".join(current_lines).strip(),
        })


    return sections
