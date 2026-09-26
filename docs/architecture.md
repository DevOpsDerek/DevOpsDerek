# Architecture

## System relationship map

1. **Terraform + Azure Policy** define and govern Azure baseline resources.
2. **AKS** is the managed Kubernetes landing zone for platform workloads.
3. **kind** mirrors Kubernetes behavior locally for fast feedback.
4. **Helm** packages workloads and platform add-ons.
5. **Argo CD** reconciles Git state to Kubernetes clusters (local kind and target AKS patterns).
6. **Agent workflows** support drafting, validation, and review preparation with human-controlled approvals.

## Delivery flow

`Git change -> local validation (kind/Helm) -> CI checks -> review approval -> GitOps reconciliation intent (Argo CD)`

This documentation describes target architecture and verification practice. It does not assert an active live Azure deployment from this profile repository.
