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

### Adoption checklist for this repository

- [x] Repository purpose is documented.
- [x] Public-only and synthetic-data rules are documented.
- [x] Default branch protection expectations are documented.
- [x] Required review and status-check expectations are documented.
- [x] Least-privilege GitHub Actions permissions are documented.
- [x] Sensitive paths are covered by CODEOWNERS.
- [x] Azure deployment remains disabled by default.
- [x] Any future deployment workflow must require protected human approval.