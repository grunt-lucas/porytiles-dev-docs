# Scripts and Tooling

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Reference for the `scripts/` directory and developer utilities. All scripts use `uv run` for execution.

| Script | Purpose | Key Usage |
|--------|---------|-----------|
| `generate_config.py` | Config code generation from YAML schema | `uv run scripts/generate_config.py` |
| `format.py` | Runs clang-format on all Porytiles sources | `uv run scripts/format.py` |
| `coverage.py` | LLVM source-based code coverage | `uv run scripts/coverage.py build\|report\|show\|clean` |
| `tidy.py` | Runs clang-tidy static analysis | `uv run scripts/tidy.py` |
| `todo.py` | Scans for TODO/FIXME/HACK comments | `uv run scripts/todo.py` |
| `new_class.py` | Scaffolds new C++ class (header + cpp + test) | `uv run scripts/new_class.py ClassName` |
| `dump_metatiles_json.py` | Debugging: dump metatile data as JSON | `uv run scripts/dump_metatiles_json.py` |
| `find_and_replace.py` | Project-wide find-and-replace | `uv run scripts/find_and_replace.py` |
| `set_pixel.py` | Pixel manipulation for test assets | `uv run scripts/set_pixel.py` |

- Python environment management: `pyproject.toml` + `uv.lock`, requires Python >= 3.13
- The `.porytiles-marker-file`: used by scripts to validate they are running from the repo root

**Cross-references:** {doc}`build-and-test` for common development workflows, {doc}`config-generation-system` for `generate_config.py` deep-dive
