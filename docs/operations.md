# Operations

## Evidence classification

| Evidence type | Status in this profile |
| --- | --- |
| Local Kubernetes validation (kind/Helm) | Verified when run in contributor environment |
| CI workflow outcomes | Verified through repository CI status/check results |
| Live Azure runtime evidence | Not claimed in this repository |
| Golden-path adoption, policy, CI reliability, and agent evaluation baselines | Not measured |

## Operating approach

- Prefer local reproducibility first (`kind`, Helm charts, and manifest checks).
- Use CI for repeatable quality and policy checks before merge.
- Treat AKS and Azure policy patterns as target-state architecture references unless explicitly backed by run evidence in linked repositories.
- Use the proposed [lifecycle policy and feedback measures](./lifecycle.md) as definitions only; they are not evidence that linked repositories meet the policy or that any outcome has improved.

## Incident and change posture

- Use pull requests and review conversation as the primary change log.
- Keep operational statements evidence-backed and time-bounded.
- Avoid language implying production ownership where evidence is not published.

## Portfolio automation

This documentation-only repository has no application build, package manifest,
production deployment, or live service. Its checked-in automation is limited to:

- `Validate portfolio automation`: pull requests, pushes to `main`, and manual
  runs call the central Actions/gh-aw validator with `contents: read` and no
  inherited secrets, and run the offline Helm upgrade test with pinned Python
  and Helm versions.
- `Portfolio documentation upkeep`: manual runs import the central documentation
  pattern, with read-only agent permissions and at most one safe-output draft PR.
  Proposals are limited to `README.md` and `docs/**/*.md`, excluding
  `docs/security.md`; governance, automation, security policy, and deployment
  changes are outside its scope. There is no schedule or autonomous merge.
- `Lint Markdown`: pull requests and pushes to `main` run the central Markdown
  style linter, scoped to `README.md`, `docs/**/*.md`, and `examples/**/*.md`.
  It is read-only and does not check external links.
- A local, offline-tested Helm chart upgrade example is covered by a Python
  standard-library test. It renders both chart versions but does not connect to
  a cluster or apply a release.

The automation validator and documentation-upkeep import are pinned to
[`dac4b81c298cb3ea6821ea312efa5375f42d5ccb`](https://github.com/DevOpsDerek/workflows/tree/dac4b81c298cb3ea6821ea312efa5375f42d5ccb).
The source `.github/workflows/documentation-upkeep.md` and generated
`documentation-upkeep.lock.yml` must be reviewed and committed together. Imports
are inlined at compile time; the agent does not need to check out the catalog at
runtime. The agent job is read-only; compiler-managed output and reporting jobs
hold the write scopes needed for draft proposals and runtime diagnostics.
The caller also enforces a documentation path allowlist, excludes security
policy, blocks protected files (except the explicitly allowed README), and
disables proposal fallback issues, automatic merge,
issue closure, and extra CI-trigger credentials. The compiler's optional
`group-concurrency-queue` feature is disabled for compatibility with stock
`actionlint`; ordinary Actions concurrency still serializes manual runs.

### Validation and maintenance

Install the GitHub CLI gh-aw extension at `v0.89.21`; install Go to run stock
`actionlint` at the version below. From the repository root, run:

```sh
gh aw compile --validate --actionlint --no-check-update --dir .github/workflows
git diff --exit-code -- .github/workflows/documentation-upkeep.lock.yml .github/aw/actions-lock.json
go run github.com/rhysd/actionlint/cmd/actionlint@v1.7.12
git diff --check
```

Compilation must succeed and leave the committed lock unchanged. After an
intentional source or central-pin update, review and commit the regenerated lock
before checking for drift. Keep full commit-SHA references; do not substitute
floating branches or tags for action/import pins.
Commit the compiler-generated `.github/aw/actions-lock.json` and `.gitattributes`
as well. Downloaded `.github/aw/imports/` files are an ignored compilation cache,
not local copies of the central implementation.

The Markdown check uses the central workflow's Node.js `22.15.0` and
`markdownlint-cli2` `0.17.2` defaults. To run the same scoped style check
locally from the repository root, use:

```sh
npx --yes markdownlint-cli2@0.17.2 README.md 'docs/**/*.md' 'examples/**/*.md'
```

To run the offline Helm upgrade example test (requires Helm 3 and Python 3):

```sh
python3 -m unittest discover -s tests -v
```

The central catalog does not provide external link checking or a
portfolio-governance validator. Review relative documentation links, external
portfolio links, public-content safety, and governance consistency manually;
record results and any checks not run in the PR template. Do not interpret
Markdown style lint or Actions/gh-aw validation as link/content-policy checks.

### Activation and human review

Before manually running the documentation agent, configure the gh-aw Copilot
engine's `COPILOT_GITHUB_TOKEN` secret using the upstream setup guidance and
review the generated workflow's permissions and safe outputs. Do not share
deployment credentials or enable schedules. This adoption does not configure
secrets or execute the agent.
The GitHub tool and safe outputs explicitly use the job-scoped `GITHUB_TOKEN`,
not an optional broader MCP/output credential. Safe-output PRs use this token
without an extra CI-trigger token; GitHub does
not automatically trigger PR CI for these bot-created PRs. A reviewer must
manually dispatch `Validate portfolio automation` against the proposed branch
and review the results before merge.

At adoption inventory, `main` had no classic branch protection and no effective
branch rules. The documented approval, Code Owner, and required-check expectations
are therefore not evidence of enforced controls. A repository administrator must
configure them, including the actual check names emitted by the central validator,
before treating automation as a required merge gate. Keep documentation proposals
as drafts until human review; green checks never authorize merging or publishing.
