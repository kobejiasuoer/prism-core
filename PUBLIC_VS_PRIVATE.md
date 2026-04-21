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
