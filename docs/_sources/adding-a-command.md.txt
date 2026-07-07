# How to Add a New CLI Command

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Step-by-step recipe for adding a new subcommand to the `porytiles` CLI.

- The Command pattern in `tools/driver/`: `command.hpp` base class, one `command_*.hpp/.cpp` per subcommand
- Step 1: Create a new `command_<name>.hpp` and `command_<name>.cpp` in `tools/driver/`
- Step 2: Implement the `Command` subclass: register CLI11 options, implement `Run()`
- Step 3: If needed, create a use case in `app/use_cases/` to hold the orchestration logic
- Step 4: Wire services via the shared setup classes in `tools/driver/tileset_command_setup.hpp`: `TilesetCommandEnv` (config, validation, diagnostics) and `TilesetCommandServices` (schema, providers, repo, compiler); only construct command-specific services inline
- Step 5: Register the command in the driver's main setup
- Step 6: Add option groups if the command shares options with other commands
- Step 7: Add integration tests for the new command
- Reference: existing commands as templates (`command_compile_tileset` is the most complete example of the env + services pattern)

**Cross-references:** {doc}`layered-architecture` for where use cases vs commands live, {doc}`dependency-injection` for wiring services
