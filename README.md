# Prism Core

Prism Core is an AI-native investment research workflow framework.

Chinese version: [README.zh-CN.md](README.zh-CN.md)

It turns the Prism workflow into a public-safe demo repository that people can read, run, and extend without exposing the private production edge.

## Why This Exists

Prism is not being open-sourced as a live trading system.

This repository exists to share the shape of the workflow:

- how a research universe is narrowed
- how scoring stages are composed
- how a reviewer turns scored candidates into decisions
- how structured reports are generated

The goal is to make the framework understandable and reusable while keeping production alpha details private.

## What This Repo Is

- A public demo framework for the Prism research pipeline
- A reference implementation of `dataset -> scanner -> scorer -> reviewer -> report`
- A starting point for contributors building adapters, demo strategies, tests, and reporting tools

## What This Repo Is Not

- It is not investment advice
- It is not the full private production Prism stack
- It is not a live trading system
- It does not publish private prompts, thresholds, or real operating outputs

## Open-Source Boundary

This repository contains:

- public-safe methodology docs
- demo data
- teaching/demo strategies
- a runnable demo pipeline
- sample reports
- tests

This repository intentionally excludes:

- private alpha details
- real thresholds and production weights
- real watchlists and operating artifacts
- production prompts
- private caches, logs, snapshots, and shortlist rules

The detailed rule set lives in [PUBLIC_VS_PRIVATE.md](PUBLIC_VS_PRIVATE.md).

## Demo Pipeline

The public demo flow is:

`stocks.json -> demo_loader -> scorers -> demo_reviewer -> markdown_report`

The implementation is intentionally simple. The point is not to mimic the private system one-to-one, but to expose the workflow seams clearly enough that other people can extend them.

## Quickstart

Create a local virtual environment and install test dependencies:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pytest
```

Run the demo pipeline:

```bash
python -m scripts.run_demo
```

Run the test suite:

```bash
pytest -q
```

The generated sample report is written to `reports/examples/demo-report.md`.

## Example Output

```markdown
# Prism Demo Report

| Symbol | Momentum | Rebound | Decision |
| --- | ---: | ---: | --- |
| DEMO001 | 74 | 49 | shortlist |
| DEMO002 | 38 | 68 | watchlist |
| DEMO003 | 57 | 44 | watchlist |
```

## Project Layout

```text
prism-core/
├── data/demo/
├── docs/
├── engine/
│   ├── adapters/
│   ├── reports/
│   ├── reviewers/
│   └── scorers/
├── reports/examples/
├── scripts/
└── tests/
```

Important entry points:

- `engine/pipeline.py` - end-to-end demo orchestration
- `scripts/run_demo.py` - CLI entrypoint
- `engine/scorers/` - public teaching strategies
- `engine/reviewers/demo_reviewer.py` - deterministic public reviewer

## Documentation

- [docs/methodology/overview.md](docs/methodology/overview.md)
- [docs/architecture/pipeline.md](docs/architecture/pipeline.md)
- [PUBLIC_VS_PRIVATE.md](PUBLIC_VS_PRIVATE.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [README.zh-CN.md](README.zh-CN.md)

## Contributing

Contributions are welcome around:

- framework abstractions
- demo strategies
- adapters and fixtures
- testing improvements
- report generation
- documentation clarity

Before opening a PR, make sure your changes stay inside the public-safe boundary and do not introduce private operating data or production logic.

## Disclaimer

Prism Core is a software framework and demo implementation for investment research workflows. It is provided for educational and engineering purposes only and does not constitute investment advice.
