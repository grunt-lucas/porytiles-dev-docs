# Dependency Injection with Google Fruit

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Focused page on the DI system. Fruit is not widely used in C++ projects, so contributors need explicit guidance.

- Why DI in Porytiles: testability, runtime conditional binding (TTY detection for formatter selection), decoupling
- Google Fruit basics for contributors who have not used it: components, injectors, binding
- The composition root: where the injector is created (in `tools/driver/` command handlers)
- Current DI components in `xcut/di/components.hpp`
- Runtime conditional binding walkthrough: how `--no-color` flag and TTY detection flow through
- DI migration status: most services still manually instantiated in command handlers (migration planned)
- Testing with DI: using mock implementations, `BufferedUserDiagnostics`, `NullUserDiagnostics`

Note: The step-by-step recipe for adding a new DI-managed service has been extracted to {doc}`adding-a-di-managed-service` in the How-To Guides section.

**Cross-references:** {doc}`layered-architecture` for why interfaces live in domain, {doc}`external-dependencies` for Fruit library details, {doc}`adding-a-di-managed-service` for the step-by-step recipe
