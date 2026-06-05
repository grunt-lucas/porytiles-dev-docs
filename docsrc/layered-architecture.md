# Layered Architecture and DDD

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

The core architectural reference. Complements `porytiles/ARCHITECTURE.md` with richer diagrams, decision frameworks, and worked examples of "where does this code go?"

- The five layers and their responsibilities:
  - **utilities**: zero-dependency helpers (result types, text formatting, C parser, string utils)
  - **xcut**: cross-cutting concerns (config value wrapper, diagnostics interface, DI wiring, validators)
  - **domain**: pure business logic (models, algorithms, services, repositories as abstract interfaces, packing subsystem)
  - **app**: use case orchestration (compile, decompile, create, import tileset)
  - **infra**: I/O adapters and concrete implementations (file readers/writers, YAML parsing, CLI, header parsing)
- The strict dependency rule with ASCII diagram
- **"Where does my code go?" decision framework** -- the main value-add over `ARCHITECTURE.md`:
  - Pure data transformation with 1-2 params? -> `domain/algorithms/` free function
  - Multi-step operation with 3+ deps? -> `domain/services/` class
  - Orchestrates domain services for a user goal? -> `app/use_cases/`
  - Reads/writes files or external systems? -> `infra/`
  - Shared across layers? -> `xcut/` or `utilities/`
- The service vs free function decision framework
- The repository pattern: abstract interfaces in `domain/repos/`, concrete implementations in `infra/repos/`
- Design principles summary (reference `ARCHITECTURE.md` for full details)

**Cross-references:** {doc}`data-flow-and-pipelines` for concrete data flow, {doc}`dependency-injection` for DI, `porytiles/ARCHITECTURE.md` in-repo for the detailed codemap
