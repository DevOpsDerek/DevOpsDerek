# Golden-path lifecycle and feedback measures

## Status and evidence boundary

The lifecycle rules below are proposed portfolio policy, not a claim that
every linked repository has adopted them or that a production support service
exists. The cadence and response times are targets for maintainers to apply;
they are not measured service-level objectives. No adoption inventory,
historical policy-check dataset, CI reliability baseline, or agent evaluation
results are published here. All four indicator baselines are **unmeasured**.

## Component lifecycle policy

| Component | Support window | Review and upgrade cadence | Deprecation and migration |
| --- | --- | --- | --- |
| Container images | The latest patch in the current minor line and the previous minor line, for up to 90 days after a newer minor supersedes it. Support ends sooner if the upstream base OS or runtime is no longer supported. | Review upstream patches monthly; rebuild on a supported base-image patch monthly and expedite verified critical security fixes. Pin consumers to an immutable digest. | Mark a superseded line deprecated in release notes with its end-of-support date and replacement digest/tag. Give at least 30 days' notice when upstream support permits; document rebuild and rollback steps. |
| Helm charts | The latest patch of the current minor and previous minor chart lines; the previous line is supported for 90 days after supersession. | Review chart and application dependencies monthly; release compatible patch/minor updates after validation. | Document breaking values/API changes and a concrete values migration in release notes. Keep the old supported minor available for the 90-day overlap; identify the first unsupported version and migration target. |
| Terraform providers | The current pinned minor and the immediately preceding minor for 90 days after a newer minor is adopted, subject to upstream support. The committed lock file is the reproducible selection, not a promise that every provider release is supported. | Review provider patches monthly and assess minor upgrades quarterly; review major upgrades against provider release notes and required Terraform version before adoption. | State the provider constraint and lock-file update in the change. For a breaking major, publish a migration note and a reviewed plan/validation path before removing the previous supported line. |
| Cluster components | Kubernetes: the latest patch of the two newest upstream-supported minor lines, never beyond upstream support. Add-ons (for example Argo CD, Kyverno, CNI, and certificate controllers): current and immediately preceding minor for up to 90 days, only where compatible with the supported Kubernetes lines. | Review security patches monthly. Plan Kubernetes and add-on minor upgrades quarterly, sooner when upstream support ends or a security fix requires it. Check published compatibility matrices before each change. | Record component versions, compatibility constraints, upgrade order, and rollback/migration steps. Give 30 days' notice where upstream support permits; upstream end-of-support may shorten that notice and must be called out explicitly. |

These windows are maintenance guidance for the portfolio, not a substitute for
an upstream vendor's lifecycle. A component whose upstream support ends sooner
must not be represented as supported by this policy.

## Exceptions and expiry

Every exception must be recorded in an issue or reviewed pull request with the
affected component/version and consumers, reason, risk and compensating
controls, accountable maintainer, and an explicit UTC expiry date. The
exception expires automatically on that date; it does not extend component
support or upstream security coverage. Set a maximum 30-day expiry for an
urgent security exception and 90 days for other exceptions. Renewal requires a
new review before expiry, an updated remediation plan, and a new expiry within
the same limit. Do not use an exception to extend support past upstream
end-of-life.

## Upgrade example

[`examples/helm-upgrade/README.md`](../examples/helm-upgrade/README.md)
shows a patch upgrade from chart 1.0.0 to 1.1.0 while preserving the release
name, replica count, and selector. Its test renders both versions locally with
`helm template` and checks those invariants and the intended image change. This
is an offline render test, not a cluster upgrade; no cluster was contacted or
changed.

## Proposed indicators

These definitions are intended to make later reporting reproducible. They do
not assert current results, targets met, causality, or productivity gains.

| Indicator | Proposed definition | Evidence source and limits | Baseline |
| --- | --- | --- | --- |
| Golden-path adoption | At a reporting date, count and proportion of inventoried, in-scope repositories or workloads using a currently supported golden-path image/chart/module version. Publish numerator, denominator, inventory date, and the version rule together. | Requires a maintained eligible-consumer inventory plus version evidence. Adoption alone does not show satisfaction, speed, or quality. | Unmeasured; no complete inventory is available here. |
| Pre-merge policy failures caught | Count unique pull requests in a stated period where a named policy check reported a policy violation before merge; report rule/check and disposition. Deduplicate repeated runs of the same rule on the same PR. | Use check-run or workflow records and retain failed/neutral/cancelled distinctions. This measures observed pre-merge failures, not violations prevented or counterfactual risk reduction. | Unmeasured; no historical policy-check dataset is published here. |
| CI reliability | For the default branch and a stated workflow set/window, successful completed runs divided by all completed eligible runs. Report raw numerator/denominator and separately disclose cancelled, skipped, and infrastructure-failure runs; do not silently drop failures. | Use GitHub Actions run/check data. Results depend on the explicitly listed workflow and eligibility rules and are not a claim about production service reliability. | Unmeasured; no time-bounded CI run analysis is published here. |
| Agent evaluation outcomes | For a versioned, fixed evaluation set and stated agent/model/prompt versions, report passed scored cases divided by all scored cases, plus failed and unscored counts and the evaluation date. | Requires versioned cases, scoring rubric, and retained outputs/reviewer labels. A result applies only to that evaluation set and configuration; it is not a general quality or productivity claim. | Unmeasured; no evaluation set or scored runs are published here. |

Do not publish an aggregate success claim without the underlying period,
numerator, denominator, scope, and evidence source. Keep proposed definitions
separate from later measured observations and state missing data explicitly.
