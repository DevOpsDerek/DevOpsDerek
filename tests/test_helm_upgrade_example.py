import shutil
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "helm-upgrade"


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

    def test_patch_upgrade_preserves_release_contract(self) -> None:
        before = render("chart-1.0.0", "values-before.yaml")
        after = render("chart-1.1.0", "values-after.yaml")

        for manifest in (before, after):
            with self.subTest(manifest="release contract"):
                self.assertIn("name: sample-api", manifest)
                self.assertIn("replicas: 2", manifest)
                self.assertIn("app.kubernetes.io/instance: sample-api", manifest)
                self.assertIn("app.kubernetes.io/name: sample-api", manifest)

        self.assertIn('image: "nginx:1.27.4"', before)
        self.assertIn('image: "nginx:1.27.5"', after)
        self.assertEqual(
            before.replace('image: "nginx:1.27.4"', 'image: "nginx:1.27.5"'),
            after,
        )


if __name__ == "__main__":
    unittest.main()
