# Software Design

Workspace for learning pythonic software design.

[![CI](https://github.com/evansdoe/software-design/actions/workflows/ci.yml/badge.svg)](https://github.com/evansdoe/software-design/actions/workflows/ci.yml)

This is a [uv workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/):
a monorepo hosting several Python projects that share one lockfile and one dev
toolchain. Each member lives under `projects/<name>/` with its own
`pyproject.toml` and its own dependencies.

```
software-design/
├── pyproject.toml          # workspace root: members = ["projects/*"]
├── uv.lock                 # one lockfile for every member
├── ruff.toml               # shared lint config
├── scripts/ci/             # project discovery used by CI
└── projects/
    ├── first-project/
    └── second-project/
```

## Setup

```bash
uv sync --all-packages --all-groups
uv run pre-commit install
```

## Adding a project

Generate one with the member template — the glob in `[tool.uv.workspace]` picks
it up automatically, and CI discovers it with no pipeline edits:

```bash
cruft create git@github.com:evansdoe/python-workspace-member.git --output-dir projects/
uv sync --all-packages --all-groups
```

## Everyday commands

| Task | Command |
| --- | --- |
| Format | `uv run poe fmt` |
| Lint (autofix) | `uv run poe lint` |
| Type check | `uv run poe types` |
| Test everything | `uv run poe test` |
| Test one member | `uv run --package <name> pytest projects/<name>` |
| List members | `uv run poe projects` |
| Everything | `uv run poe all` |

Run a member's own entry point with `uv run --package <name> <command>`.

## How CI works

Lint, type checks and the license audit run **once** at the root over all
members. Tests run **per member**, and only for members affected by the change:

- **GitHub Actions** — the `discover` job emits a JSON matrix from
  `scripts/ci/discover_projects.py`, and `test` fans out over it.

A change to `pyproject.toml`, `uv.lock`, `ruff.toml`, `scripts/` or the CI
config counts as affecting every member.

## License

MIT — see [LICENSE](LICENSE).
