# Project Layout and Directory Structure

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Orientation page. After building, the contributor needs a mental map of what lives where.

- Top-level directory layout: `porytiles/` (main source), `scripts/`, `resources/`, `.github/workflows/`, `porytiles-dev-docs/`, `porytiles-user-docs/`
- Inside `porytiles/`: `include/porytiles/`, `lib/`, `tools/driver/`, `tests/`, `config_templates/`, `notes/`
- The include/lib split: headers in `include/porytiles/<layer>/`, implementations in `lib/<layer>/`
- Layer directories at a glance: `domain/`, `app/`, `infra/`, `xcut/`, `utilities/` -- one-sentence description each (full details on the architecture page)
- `tools/driver/`: the CLI executable entry point
- `config_templates/`: Jinja2 templates and `config_schema.yaml` for code generation
- `tests/unit/` vs `tests/integration/` vs `tests/support/`
- `notes/`: internal design decision documents (not user-facing, but valuable for understanding rationale)
- `porytiles/ARCHITECTURE.md`: the in-repo architecture overview (the dev docs site expands on it)
- `STYLE.md`: code style guide (the authoritative reference -- dev docs reference it, not duplicate it)
- `resources/`: test assets and example files used by integration tests

**Cross-references:** {doc}`layered-architecture` for DDD layer details, {doc}`config-generation-system` for config_templates, {doc}`scripts-and-tooling` for scripts/
