# Contributing

We welcome contributions to the public framework, demo adapters, example strategies, documentation, and tests.

We do not use this repository for stock-pick requests, guaranteed performance claims, or publication of private production logic.

Before opening a pull request:

1. Run `pytest -q`
2. Confirm no sensitive data is introduced
3. Update docs for user-visible behavior changes

## Sensitive Data Check

Before committing, confirm that your change does not add:

- real watchlists
- real snapshots or fund-flow caches
- logs from private cron runs
- credentials, cookies, proxy config, or browser profile references
- private prompts or production shortlist logic
