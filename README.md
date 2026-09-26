# Derek Campbell

Principal DevOps Engineer focused on platform engineering, developer experience, and practical agentic engineering. Based in Scotland.

I lead engineering teams and build repeatable ways to deliver software: infrastructure as code, CI/CD standards, GitOps, container platforms, and reliability practices. My experience includes leading enterprise GitHub adoption and CI/CD migrations, designing Kubernetes-based platforms, and piloting AI-assisted DevOps workflows. I also enjoy mentoring engineers and turning platform capabilities into self-service paths for delivery teams.

## What I'm building

I'm developing an **Azure-focused platform engineering portfolio** that connects Terraform-managed infrastructure with Git-managed Kubernetes delivery. Agentic engineering is a supporting capability, with human review and clear operational guardrails rather than autonomous production deployment.

| Project | Focus |
| --- | --- |
| [Azure platform Terraform](https://github.com/DevOpsDerek/azure-platform-terraform) | Azure infrastructure and AKS reference patterns with Terraform |
| [kind and ArgoCD platform lab](https://github.com/DevOpsDerek/kind-argocd-platform-lab) | Reproducible local Kubernetes and GitOps experiments |
| [Agentic platform golden paths](https://github.com/DevOpsDerek/agentic-platform-golden-paths) | Reviewable agent-assisted platform workflows |
| [Golden Docker images](https://github.com/DevOpsDerek/golden-docker-images) | Container image build and supply-chain practices |

These repositories are portfolio work in progress, not a claim of deployed Azure infrastructure. Examples use public or synthetic data.

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

Apply the same three template files and label convention to every portfolio repository so work items, decisions, and pull requests stay reviewable with a consistent structure and starting label baseline across repositories.