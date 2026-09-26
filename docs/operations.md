# Operations

## Evidence classification

| Evidence type | Status in this profile |
| --- | --- |
| Local Kubernetes validation (kind/Helm) | Verified when run in contributor environment |
| CI workflow outcomes | Verified through repository CI status/check results |
| Live Azure runtime evidence | Not claimed in this repository |

## Operating approach

- Prefer local reproducibility first (`kind`, Helm charts, and manifest checks).
- Use CI for repeatable quality and policy checks before merge.
- Treat AKS and Azure policy patterns as target-state architecture references unless explicitly backed by run evidence in linked repositories.

## Incident and change posture

- Use pull requests and review conversation as the primary change log.
- Keep operational statements evidence-backed and time-bounded.
- Avoid language implying production ownership where evidence is not published.
