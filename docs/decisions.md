# Architecture Decisions

## Decision 1: Governed accelerator model for agents

- **Decision**: Use agentic engineering as an accelerator with mandatory human review.
- **Rationale**: Increases delivery speed while preserving governance and accountability.
- **Consequence**: Agent outputs are treated as proposals, not automatic production actions.

## Decision 2: Local-first Kubernetes validation

- **Decision**: Validate Kubernetes behavior in `kind` before downstream environments.
- **Rationale**: Fast feedback lowers change risk and improves reproducibility.
- **Consequence**: Local and CI evidence are prioritized in published claims.

## Decision 3: GitOps packaging and reconciliation pattern

- **Decision**: Use Helm for packaging and Argo CD for reconciliation workflows.
- **Rationale**: Clear separation between desired state authoring and cluster convergence.
- **Consequence**: Portfolio architecture explains AKS as managed target and kind as local proving ground.
