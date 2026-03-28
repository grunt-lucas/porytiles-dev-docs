# Data Flow and Compilation Pipelines

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Concrete walkthrough of how data moves through the system during the major operations. This page makes the architecture *real* -- showing the actual classes and methods involved at each step.

- **The compile pipeline** (detailed):
  - Input: RGBA layer PNGs (bottom, middle, top) + `attributes.csv`
  - `LayerImageMetatileizer` -> `ImageTileizer` -> tile canonicalization -> `PalettePacker` -> `PrimaryTilesetCompiler` -> output artifacts
- **Edit mode branching**: how optimize/patch/locked modes affect the pipeline
- **The decompile pipeline** (reverse direction):
  - Input: Porymap binary artifacts -> `MetatileDecompiler` -> RGBA layers + `attributes.csv`
- **The import pipeline**:
  - C parser reads header files, discovers INCBIN paths, reads binary artifacts
  - Constructs both `PorytilesTilesetComponent` and `PorymapTilesetComponent`
- Key domain models that flow through: `Tileset`, `PorytilesTilesetComponent`, `PorymapTilesetComponent`, `PixelTile<T>`, `Metatile`, `PackedPalette`
- The use case layer as orchestrator
- Animation data flow (brief overview)

**Cross-references:** {doc}`layered-architecture` for layer context, {doc}`adding-a-packing-strategy` for extending the packing step, {doc}`c-parser` for the import parser
