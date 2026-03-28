# Scripts and Tooling

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Reference for the `Scripts/` directory and developer utilities. All scripts use `uv run` for execution.

| Script | Purpose | Key Usage |
|--------|---------|-----------|
| `generate_config.py` | Config code generation from YAML schema | `uv run Scripts/generate_config.py` |
| `format.py` | Runs clang-format on all Porytiles2 sources | `uv run Scripts/format.py` |
| `coverage.py` | LLVM source-based code coverage | `uv run Scripts/coverage.py build\|report\|show\|clean` |
| `tidy.py` | Runs clang-tidy static analysis | `uv run Scripts/tidy.py` |
| `todo.py` | Scans for TODO/FIXME/HACK comments | `uv run Scripts/todo.py` |
| `new_class.py` | Scaffolds new C++ class (header + cpp + test) | `uv run Scripts/new_class.py ClassName` |
| `dump_metatiles_json.py` | Debugging: dump metatile data as JSON | `uv run Scripts/dump_metatiles_json.py` |
| `find_and_replace.py` | Project-wide find-and-replace | `uv run Scripts/find_and_replace.py` |
| `set_pixel.py` | Pixel manipulation for test assets | `uv run Scripts/set_pixel.py` |

- Python environment management: `pyproject.toml` + `uv.lock`, requires Python >= 3.13
- The `.porytiles-marker-file`: used by scripts to validate they are running from the repo root

**Cross-references:** {doc}`build-and-test` for common development workflows, {doc}`config-generation-system` for `generate_config.py` deep-dive
