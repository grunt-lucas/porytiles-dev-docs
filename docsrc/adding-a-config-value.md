# How to Add a New Configuration Value

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Step-by-step recipe. The most common contributor task involving the config system.

- Step 1: Add the entry to `config_schema.yaml` -- all required fields, choosing the correct layer (domain/app/infra)
- Step 2: If defining a new enum type, add it to the enum types section of the schema
- Step 3: If needed, add a parser function (for new types) or validator function
- Step 4: Run the code generator: `uv run scripts/generate_config.py` (or just build -- CMake triggers it automatically)
- Step 5: Verify generated files -- what to check in the generated layer interface, provider implementations, CLI registration
- Step 6: Use the new config value in code via the appropriate layer config interface
- Step 7: Add tests -- unit test the validator, integration test the full config resolution via mock configs
- Step 8: Update user docs `configuration.md` page with the new value
- Worked example: adding a hypothetical config value from schema entry to usage in code

**Cross-references:** {doc}`config-generation-system` for the full system explanation, {doc}`build-and-test` for running the generator
