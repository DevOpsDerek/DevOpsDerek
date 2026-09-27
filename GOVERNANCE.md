# Repository Governance

This repository is a public portfolio repository. All content must be safe for public release and portable outside any employer, client, or private environment.

## Allowed content

- Public documentation, portfolio artifacts, and reusable examples
- Synthetic, sample, or otherwise non-sensitive data created for demonstration
- Generic configuration that does not assume access to private infrastructure

## Prohibited content

- Credentials, secrets, tokens, certificates, or connection strings
- Confidential, proprietary, regulated, customer, or employer-specific material
- Production deployment details that assume access to a private Azure tenant, subscription, or environment

## Pull request and branch governance

Apply these defaults to the repository's default branch:

- Require pull requests before merging; do not allow direct pushes.
- Require at least one approving review.
- Require review from Code Owners when sensitive paths change.
- Dismiss stale approvals when new commits are pushed.
- Require all configured required status checks to pass before merging.
- Require conversation resolution before merging.
- Restrict force pushes and branch deletion on the default branch.

## Required checks

This repository should treat every configured continuous-integration check as required before merge. While the repository is documentation-only today, any future validation workflow added for markdown, links, policy, or tests must be marked as a required status check in branch protection before it becomes part of the normal contribution flow.

Passing checks are evidence, not ownership transfer. Repository owners and reviewers remain accountable for security, compliance, policy, and release-risk decisions even when all automated checks are green.

## GitHub Actions permissions

Use least-privilege permissions by default:

- Set workflow-level `permissions` to read-only unless a job needs more.
- Prefer explicit per-job permissions over broad write scopes.
- Avoid repository-wide secrets where a workflow can run without them.
- Do not enable automatic deployment credentials by default.

Example baseline:

```yaml
permissions:
  contents: read
```

## Deployment guardrails

- Azure deployment is disabled by default in this repository.
- Do not add automatic deployment on push or pull request.
- If deployment is introduced later, isolate it in a dedicated workflow that:
  - uses protected environments,
  - requires explicit human approval before execution, and
  - keeps credentials out of the repository.

## Sensitive paths requiring Code Owner review

Sensitive paths include repository governance, automation, and any future deployment or infrastructure definitions. If infrastructure-as-code or deployment files are introduced later, keep them under one of the protected directories below so Code Owner review is enforced consistently:

- `/.github/**`
- `/GOVERNANCE.md`
- `/infra/**`
- `/deploy/**`
- `/scripts/deploy/**`

## Architecture decision records (ADRs)

Use ADRs for decisions that impact more than one pull request or more than one contributor. ADRs should be stored in `docs/adr/` using the repository template at `docs/adr/0000-template.md`.

Decision placement across the portfolio:

- If a decision only affects this repository, record the ADR in this repository.
- If a decision affects multiple repositories, open matching ADRs in each affected repository and cross-link them to preserve local ownership and review history.
- If implementation details differ by repository, keep a shared context/problem statement but document repository-specific consequences in each ADR.

## Contribution templates and labels

All portfolio repositories should include the same contribution contract:

- `/.github/ISSUE_TEMPLATE/work-item.yml`
- `/.github/pull_request_template.md`
- `docs/adr/0000-template.md`

Use compact labels so planning views stay scannable. Apply and maintain labels in repository settings so issues and PRs can be labeled consistently:

- Repository: `r:portfolio`, `r:platform`, `r:infra`
- Priority: `p0`, `p1`, `p2`, `p3`
- Dependency: `dep:blocking`, `dep:blocked`, `dep:none`
- Agent readiness: `agent:ready`, `agent:needs-context`, `agent:needs-owner`
