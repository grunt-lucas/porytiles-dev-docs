# How to Add a DI-Managed Service

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Step-by-step recipe for wiring a new service into the Google Fruit DI system.

- Step 1: Define the abstract interface in the appropriate layer (`domain/` or `xcut/`)
- Step 2: Create the concrete implementation in `infra/` (or same layer for non-I/O services)
- Step 3: Create a Fruit component function in `xcut/di/components.hpp`
- Step 4: Bind the component in the relevant command handler(s) in `tools/driver/`
- Step 5: Write tests using mock implementations (e.g., `BufferedUserDiagnostics`, `NullUserDiagnostics`)
- Reference: the existing `get_formatter_component()` as a template

**Cross-references:** {doc}`dependency-injection` for conceptual understanding of the DI system, {doc}`layered-architecture` for interface placement decisions
