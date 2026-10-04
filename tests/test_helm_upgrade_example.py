import shutil
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "helm-upgrade"


def mapping_after(manifest: str, header: str, indentation: int) -> dict[str, str]:
    lines = manifest.splitlines()
    header_index = lines.index(header)
    mapping: dict[str, str] = {}
    for line in lines[header_index + 1 :]:
        if not line.strip():
            continue
        line_indentation = len(line) - len(line.lstrip())
        if line_indentation < indentation:
            break
        if line_indentation == indentation:
            key, separator, value = line.strip().partition(":")
            if separator:
                mapping[key] = value.strip()
    return mapping


def render(chart: str, values: str) -> str:
    result = subprocess.run(
        [
            "helm",
            "template",
            "sample-api",
            str(EXAMPLE / chart),
            "--namespace",
            "example",
            "--values",
            str(EXAMPLE / values),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


class HelmUpgradeExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if shutil.which("helm") is None:
            raise RuntimeError("Helm 3 is required to render the upgrade example")

    def test_minor_upgrade_preserves_release_contract(self) -> None:
        before = render("chart-1.0.0", "values-before.yaml")
        after = render("chart-1.1.0", "values-after.yaml")

        for manifest in (before, after):
            with self.subTest(manifest="release contract"):
                self.assertIn("name: sample-api", manifest)
                self.assertIn("replicas: 2", manifest)
                self.assertIn("app.kubernetes.io/instance: sample-api", manifest)
                self.assertIn("app.kubernetes.io/name: sample-api", manifest)
                selector_labels = mapping_after(manifest, "    matchLabels:", 6)
                pod_labels = mapping_after(manifest, "      labels:", 8)
                self.assertEqual(
                    {
                        "app.kubernetes.io/name": "sample-api",
                        "app.kubernetes.io/instance": "sample-api",
                    },
                    selector_labels,
                )
                self.assertEqual(selector_labels, pod_labels)

        before_image = (
            'image: "nginx@sha256:'
            "09369da6b10306312cd908661320086bf87fbae1b6b0c49a1f50ba531fef2eab"
            '"'
        )
        after_image = (
            'image: "nginx@sha256:'
            "6784fb0834aa7dbbe12e3d7471e69c290df3e6ba810dc38b34ae33d3c1c05f7d"
            '"'
        )
        self.assertIn(before_image, before)
        self.assertIn(after_image, after)
        self.assertEqual(
            before.replace(before_image, after_image),
            after,
        )


if __name__ == "__main__":
    unittest.main()
