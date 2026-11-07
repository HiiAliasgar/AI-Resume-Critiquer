from io import BytesIO
from pathlib import Path

from PyPDF2 import PdfReader

MAX_RESUME_BYTES = 5 * 1024 * 1024
MAX_EXTRACTED_CHARS = 100_000


def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from a PDF, handling encrypted and image-only documents."""
    reader = PdfReader(pdf_file)
    if reader.is_encrypted:
        try:
            decrypted = reader.decrypt("")
        except Exception as exc:
            raise ValueError("The PDF is password-protected.") from exc
        if not decrypted:
            raise ValueError("The PDF is password-protected.")
    pages = []
    total_chars = 0
    for page in reader.pages:
        page_text = page.extract_text() or ""
        remaining = MAX_EXTRACTED_CHARS - total_chars
        if remaining <= 0:
            break
        pages.append(page_text[:remaining])
        total_chars += min(len(page_text), remaining)
    return "\n".join(pages)


def extract_text_from_upload(file_bytes: bytes, filename: str) -> str:
    """Validate and extract bounded PDF or UTF-8 text resume content."""
    if len(file_bytes) > MAX_RESUME_BYTES:
        raise ValueError("Resume file exceeds the 5 MB limit.")
    suffix = Path(filename or "").suffix.lower()
    if suffix == ".pdf":
        if not file_bytes.startswith(b"%PDF-"):
            raise ValueError("The uploaded PDF file is invalid.")
        return extract_text_from_pdf(BytesIO(file_bytes))
    if suffix == ".txt":
        try:
            return file_bytes.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise ValueError("The TXT file must use UTF-8 encoding.") from exc
    raise ValueError("Only PDF and TXT resume files are supported.")
