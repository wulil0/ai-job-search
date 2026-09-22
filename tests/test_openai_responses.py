import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "openai_responses.py"


def load_module():
    spec = importlib.util.spec_from_file_location("openai_responses", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class OpenAIResponsesTests(unittest.TestCase):
    def test_extracts_nested_output_text(self):
        module = load_module()
        response = {
            "output": [
                {"content": [{"type": "output_text", "text": "你好"}]},
                {"content": [{"type": "output_text", "text": "，世界"}]},
            ]
        }
        self.assertEqual("你好，世界", module.extract_output_text(response))

    def test_dry_run_builds_request_without_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            context = Path(tmp) / "context.md"
            context.write_text("仅使用真实经历。", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--prompt",
                    "生成中文简历摘要",
                    "--context-file",
                    str(context),
                    "--model",
                    "MODEL",
                    "--dry-run",
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
        payload = json.loads(result.stdout)
        self.assertEqual("MODEL", payload["model"])
        self.assertFalse(payload["store"])
        self.assertIn("仅使用真实经历。", payload["input"])
        self.assertIn("生成中文简历摘要", payload["input"])


if __name__ == "__main__":
    unittest.main()
