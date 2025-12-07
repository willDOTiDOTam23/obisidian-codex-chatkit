import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import qrcode  # noqa: F401
except ImportError:
    qrcode = None


QR_SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "qr-code-generator" / "generate_qr.py"


@unittest.skipUnless(qrcode, "qrcode library is not installed")
class QRCodeGeneratorTestCase(unittest.TestCase):
    def test_generate_qr_creates_png(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            output_png = tmp_path / "qr.png"

            result = subprocess.run(
                [
                    sys.executable,
                    str(QR_SCRIPT),
                    "--text",
                    "https://example.com",
                    "--output",
                    str(output_png),
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                self.fail(f"QR generation failed: {result.stderr}")

            self.assertTrue(output_png.exists(), "Output PNG was not created")
            self.assertGreater(output_png.stat().st_size, 0, "Output PNG is empty")


if __name__ == "__main__":
    unittest.main()
