import unittest
from io import BytesIO

from PyPDF2 import PdfWriter

from resume_utils import MAX_RESUME_BYTES, extract_text_from_pdf, extract_text_from_upload


class ResumeExtractionTests(unittest.TestCase):
    def test_extracts_utf8_text(self):
        self.assertEqual(extract_text_from_upload(b"Python engineer", "resume.txt"), "Python engineer")

    def test_accepts_utf8_bom_text(self):
        self.assertEqual(extract_text_from_upload(b"\xef\xbb\xbfResume", "resume.txt"), "Resume")

    def test_rejects_unsupported_extension(self):
        with self.assertRaisesRegex(ValueError, "Only PDF and TXT"):
            extract_text_from_upload(b"content", "resume.docx")

    def test_rejects_invalid_pdf(self):
        with self.assertRaisesRegex(ValueError, "PDF file is invalid"):
            extract_text_from_upload(b"not a pdf", "resume.pdf")

    def test_rejects_oversized_upload(self):
        with self.assertRaisesRegex(ValueError, "5 MB"):
            extract_text_from_upload(b"x" * (MAX_RESUME_BYTES + 1), "resume.txt")

    def test_handles_textless_pdf_without_crashing(self):
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        output = BytesIO()
        writer.write(output)
        self.assertEqual(extract_text_from_pdf(BytesIO(output.getvalue())), "")


if __name__ == "__main__":
    unittest.main()
