# Building, Testing, and Development Workflows

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Detailed build and test reference beyond the initial setup.

- CMake configuration options and build types (Debug, Release)
- The code generation step: what `generate_config.py` does, when CMake re-runs it
- Building specific targets: `porytiles2` (executable), `Porytiles2UnitTests`, `Porytiles2IntegrationTests`, `Porytiles2AllTests`
- Running tests: GoogleTest filter flags (`--gtest_filter`), running specific test suites or individual tests
- The custom test main (`test_main.cpp`): stacktrace control via `--enable-stacktrace`
- Test resource files in `Resources/` and how integration tests reference them
- Running the formatter: `uv run Scripts/format.py`
- Running the linter: `uv run Scripts/tidy.py`
- Running code coverage: `uv run Scripts/coverage.py build`, `report`, `show`, `clean`
- The common development loop: edit code -> build -> run tests -> format -> commit
- Testing against a real decomp project: the `../pokeemerald-expansion` testbed

**Cross-references:** {doc}`dev-environment-setup` for initial setup, {doc}`scripts-and-tooling` for full script reference, {doc}`writing-tests` for test authoring patterns
