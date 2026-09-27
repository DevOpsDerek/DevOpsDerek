# Derek Campbell

Principal-level Azure platform product portfolio, with agentic engineering used as a governed accelerator for delivery quality and speed.

## Portfolio summary

This profile presents an Azure-focused platform architecture where:

- **Terraform + Azure Policy** establish governed cloud foundations.
- **AKS** is the managed runtime target for workload delivery.
- **kind** provides reproducible local Kubernetes validation.
- **Helm + Argo CD** package and reconcile workloads via GitOps.
- **Agent workflows** accelerate authoring and checks, with mandatory human review gates.

This repository documents architecture and operating model only. It does **not** claim a live production Azure deployment from this profile repository.

## Credentials

User-confirmed Azure credentials:

- Microsoft Certified: Azure Administrator Associate
- Microsoft Certified: Azure Solutions Architect Expert

## Documentation hub

Start here: [/docs/index.md](./docs/index.md)

- [Architecture](./docs/architecture.md)
- [Getting started](./docs/getting-started.md)
- [Security](./docs/security.md)
- [Operations](./docs/operations.md)
- [Architecture decisions](./docs/decisions.md)
- [Repository links](./docs/repositories.md)

## Governance

This repository is public portfolio material and is governed by:

- [/GOVERNANCE.md](./GOVERNANCE.md)
- [/.github/CODEOWNERS](./.github/CODEOWNERS)

## Connect

[LinkedIn](https://www.linkedin.com/in/devopsderek/)

## Repository governance

This repository is part of a public portfolio and is governed by the standards in [/GOVERNANCE.md](./GOVERNANCE.md).

## Repository purpose

- Publish public portfolio materials only.
- Keep examples generic, reusable, and safe to share publicly.
- Exclude confidential, proprietary, employer-specific, customer, or credential-bearing content.

## Governance evidence

- Governance policy: [/GOVERNANCE.md](./GOVERNANCE.md)
- Sensitive-path ownership: [/.github/CODEOWNERS](./.github/CODEOWNERS)
- ADR template: [/docs/adr/0000-template.md](./docs/adr/0000-template.md)
- Issue template: [/.github/ISSUE_TEMPLATE/work-item.yml](./.github/ISSUE_TEMPLATE/work-item.yml)
- PR template: [/.github/pull_request_template.md](./.github/pull_request_template.md)

### Adoption checklist for this repository

- [x] Repository purpose is documented.
- [x] Public-only and synthetic-data rules are documented.
- [x] Default branch protection expectations are documented.
- [x] Required review and status-check expectations are documented.
- [x] Least-privilege GitHub Actions permissions are documented.
- [x] Sensitive paths are covered by CODEOWNERS.
- [x] Azure deployment remains disabled by default.
- [x] Any future deployment workflow must require protected human approval.
- [x] ADR, issue, and PR templates are defined and linked.
- [x] Compact label conventions are defined in governance policy.
- [x] Governance states that green checks do not replace human security/policy ownership.

### Portfolio rollout standard

Apply the same template files and label convention to every portfolio repository so work items, decisions, and pull requests stay reviewable with a consistent structure and starting label baseline across repositories.
