# How to Add a New Packing Strategy

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Recipe for the Strategy pattern in the packing subsystem. Also serves as a concrete example of extending the domain layer.

- The `PackingStrategy` abstract interface in `domain/packing/services/`
- Existing strategies as reference:
  - `BestFusionStrategy` (greedy fusion)
  - `OverloadAndRemoveStrategy` (heuristic retries)
  - `BacktrackingStrategy` (exhaustive search)
- Step 1: Create a new strategy class implementing `PackingStrategy`
- Step 2: Add a new enum value to `PackingStrategyType` in `config_schema.yaml`
- Step 3: Run code generation to update the enum and CLI/YAML parsing
- Step 4: Wire the new strategy into `PalettePacker` (the orchestrating service)
- Step 5: Write unit tests with known tile/palette inputs and expected outputs
- Key packing domain models to understand: `PackableTile`, `PackedPalette`, `PaletteHint`, `PrefilledPalette`, `PalettePool`, `ColorSet`
- Brief overview of packing metrics

**Cross-references:** {doc}`data-flow-and-pipelines` for where packing fits in compilation, {doc}`config-generation-system` and {doc}`adding-a-config-value` for adding the enum
