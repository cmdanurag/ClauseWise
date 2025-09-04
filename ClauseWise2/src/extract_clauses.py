from pathlib import Path
from typing import List

# Install these if you haven't: pip install python-docx PyPDF2
from docx import Document
import PyPDF2

def extract_clauses(file_path: str) -> List[str]:
    """
    Extracts text clauses from PDF or DOCX files.
    Returns a list of clauses (split by paragraph or line).
    """
    file_path = Path(file_path)
    clauses = []

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:  # skip empty paragraphs
                clauses.append(text)

    elif file_path.suffix.lower() == ".pdf":
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    # Split by line breaks as clauses
                    for line in text.splitlines():
                        line = line.strip()
                        if line:
                            clauses.append(line)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")

    return clauses
