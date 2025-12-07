import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PANDOC_PATH = shutil.which("pandoc")
CONVERT_SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "markdown-to-docx" / "convert.py"


@unittest.skipUnless(PANDOC_PATH, "Pandoc is not installed")
class MarkdownToDocxTestCase(unittest.TestCase):
    def test_convert_creates_docx(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            input_md = tmp_path / "sample.md"
            output_docx = tmp_path / "sample.docx"
            input_md.write_text("# Hello\n\nThis is a test.\n")

            result = subprocess.run(
                [sys.executable, str(CONVERT_SCRIPT), str(input_md), str(output_docx)],
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                self.fail(f"Conversion failed: {result.stderr}")

            self.assertTrue(output_docx.exists(), "Output docx was not created")
            self.assertGreater(output_docx.stat().st_size, 0, "Output docx is empty")


if __name__ == "__main__":
    unittest.main()
