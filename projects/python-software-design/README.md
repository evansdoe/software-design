# python-software-design

Practising Software Design for Python Programmers - Principles and patterns by Ronald Mak

A member of this uv workspace. Run everything from the **workspace root**:

```bash
uv sync --all-packages --all-groups
uv run --package python-software-design pytest projects/python-software-design
```

Add a dependency to this member only:

```bash
uv add --package python-software-design httpx
```

Run it:

```bash
uv run --package python-software-design python-software-design
```

## Layout

```
python-software-design/
├── pyproject.toml
├── src/python_software_design/
└── tests/
```
