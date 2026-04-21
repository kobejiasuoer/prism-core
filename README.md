# Prism Core

Prism Core is an AI-native investment research workflow framework.

## What it is

- A public demo framework for the Prism research pipeline
- A reference implementation of `dataset -> scanner -> scorer -> reviewer -> report`
- A starting point for contributors building adapters, demo strategies, and reporting tools

## What it is not

- It is not investment advice
- It is not the full private production Prism stack
- It is not a live trading system

## Open-source scope

This repo contains public-safe methodology, demo data, example strategies, and a runnable demo pipeline.

Private alpha details, real thresholds, real watchlists, production prompts, and operating artifacts are intentionally excluded.

## Quickstart

```bash
python -m scripts.run_demo
pytest -q
```

The generated sample report will be written to `reports/examples/demo-report.md`.
