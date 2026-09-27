---
name: code-review
description: Review pull requests in the DevOpsDerek portfolio repository for Azure Terraform, kind/ArgoCD GitOps, GitHub Actions CI, and container image supply-chain changes. Use when asked to review a PR, diff, or branch in this repository.
---

# Code review for the DevOpsDerek portfolio

This skill is defined in this repository only. It guides reviews of changes to
`DevOpsDerek/DevOpsDerek` and does not apply to other repositories unless they
add their own copy. Follow `GOVERNANCE.md` and `.github/CODEOWNERS` as the
source of truth for repository policy.

## 1. Understand intent before judging code

- Read the linked issue and the PR title/description. State the intended
  outcome in one sentence before reviewing.
- Flag scope creep: changes unrelated to the stated intent, or intent that the
  diff does not actually deliver.
- Read the surrounding code and files the change depends on, not only the diff
  hunks, before concluding something is wrong.

## 2. Check evidence, not claims

- Look at CI results for the **current head commit** only. Results from older
  commits do not count.
- Separate what was verified (passing checks, test output, `terraform plan`
  output, rendered manifests) from what is only asserted in the description.
- Explicitly list missing checks, e.g. "no plan output attached", "no workflow
  run on latest commit", "manifests not validated". Do not treat absent
  evidence as a pass.

## 3. Write high-confidence, actionable findings

- Report only issues you are confident about. Prefer a few real problems over
  many speculative ones; label genuine uncertainty as a question.
- Anchor each finding to a specific file and line, explain the impact, and
  propose a concrete fix or suggestion.
- Rank by severity: blocking (correctness, security, policy) before
  non-blocking (clarity, maintainability). Skip pure style nits unless asked.

## 4. Handle secrets and vulnerabilities safely

- If you find a credential, token, key, connection string, or private
  tenant/subscription identifier, say that sensitive material appears to be
  present and where, but **do not repeat the value** in comments, summaries,
  or commit messages. Recommend removal and rotation.
- Describe vulnerabilities at the level needed to fix them. Do not publish
  exploit steps or sensitive details in public PR comments; direct the author to
  private reporting where appropriate.
- Content must remain safe for a public portfolio: no employer, client, or
  confidential material (see `GOVERNANCE.md`).

## 5. Require explicit human approval for sensitive changes

Do not approve on your own authority, and call out that a human owner must
explicitly approve, when a change affects:

- governance, branch protection, CODEOWNERS, or other policy files;
- security controls, permissions, or credentials handling;
- anything that could deploy to or modify real (production) infrastructure.

Paths under `/.github/**`, `/GOVERNANCE.md`, `/infra/**`, `/deploy/**`, and
`/scripts/deploy/**` require Code Owner review.

## 6. Domain checks

### Azure Terraform

- Changes should be validated with `terraform fmt`, `validate`, and a reviewed
  `plan`. There must be no automatic `apply` on push or pull request.
- Any apply path must use a protected environment with manual approval and
  OIDC/federated credentials, not stored secrets.
- Check provider and module versions are pinned, state backends are not
  hardcoded to private resources, and no real subscription/tenant IDs are
  committed.
- Watch for destructive plan actions (replace/destroy) and overly broad RBAC or
  public network exposure.

### kind / ArgoCD GitOps

- Git is the source of truth: flag manual `kubectl apply` steps that bypass
  reconciliation, and check sync policy (auto-sync, prune, self-heal) is
  intentional.
- Confirm manifests/Kustomize/Helm render and target the intended cluster and
  namespace.
- No plaintext Kubernetes `Secret` data in the repo; expect sealed/external
  secret references or local-only placeholders.
- Check resource requests/limits, probes, and non-root security context where
  relevant.

### GitHub Actions CI

- Workflow and job `permissions` should be least privilege (default
  `contents: read`); justify every write scope.
- Pin third-party actions to a full commit SHA; avoid `pull_request_target`
  with untrusted checkout, and avoid interpolating untrusted input (e.g. PR
  titles) directly into `run:` scripts.
- Secrets should not be exposed to fork PRs or echoed to logs.
- New validation workflows should be listed as required checks per
  `GOVERNANCE.md`.

### Container image supply chain

- Base and deployed images should be pinned by digest (`@sha256:...`), not
  mutable tags such as `latest`.
- Provenance, SBOM, signing, or attestation claims in docs or PRs must be
  backed by a workflow step or artifact that actually produces them; flag
  unverified claims.
- Check for minimal base images, non-root users, and no secrets baked into
  layers or build args.

## 7. Summarize the review

End with: the stated intent, verified evidence, missing checks, findings by
severity, and whether human owner approval is required. Recommend
"approve", "request changes", or "comment" and give the reason.
