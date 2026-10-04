# Offline Helm chart upgrade example

This example rehearses a chart minor upgrade from `1.0.0` to `1.1.0` without a
Kubernetes cluster. The release name and replica count remain stable while the
nginx image is updated from the manifest digest for `1.27.4` to the manifest
digest for `1.27.5`. Both immutable digests were resolved from Docker Hub; the
test verifies that only the pinned image reference changes.

Render both revisions and run the invariant test from the repository root:

```sh
helm template sample-api examples/helm-upgrade/chart-1.0.0 \
  --namespace example --values examples/helm-upgrade/values-before.yaml
helm template sample-api examples/helm-upgrade/chart-1.1.0 \
  --namespace example --values examples/helm-upgrade/values-after.yaml
python3 -m unittest discover -s tests -v
```

After reviewing the rendered diff and validating the target cluster's
compatibility, the corresponding apply command is:

```sh
helm upgrade --install sample-api examples/helm-upgrade/chart-1.1.0 \
  --namespace example --create-namespace \
  --values examples/helm-upgrade/values-after.yaml
```

That command is illustrative and was **not** run. The test only renders local
manifests; it does not contact a cluster or claim the release was applied.
