# Public vs Private

## Put changes in `prism-core` when

- The change improves framework abstractions
- The change improves demo strategies or fixtures
- The change improves docs, tests, or reporting infrastructure
- The change teaches people how Prism works without exposing the private edge

## Keep changes in the private repo when

- The change depends on real thresholds or production weights
- The change depends on private prompts or shortlist rules
- The change includes real caches, logs, snapshots, watchlists, or outputs
- The change reveals operating details that reproduce the current edge

## Promotion rule

If a private change becomes generally useful, rewrite it as a public-safe abstraction with docs, demo data, and tests before moving it into `prism-core`.

## Promotion Workflow

1. Build and validate a change in the private repo if it depends on private edge.
2. Strip out private thresholds, prompts, data, and operating artifacts.
3. Re-express the idea as a public abstraction, demo strategy, or doc improvement.
4. Add demo data and tests.
5. Land the public-safe version in `prism-core`.
