# C++ Features and Patterns Used

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Background for contributors who may not be familiar with specific C++20/23 features and patterns used in the codebase.

- **C++20 features in use**:
  - Concepts: `SupportsTransparency` and others for compile-time constraints
  - `std::source_location`: used in panic diagnostics for automatic file/line capture
  - Ranges and views: used throughout for container transformations
- **C++23 features in use**:
  - `std::format` and `std::formatter` specializations (with the critical `auto &ctx` note from `STYLE.md`)
  - `std::expected`: used in newer code for simple error returns
  - Deducing `this`: where and why it is used
- **Key patterns**:
  - Move-only types: `ChainableResult` is move-only, use case return values use `std::move`
  - Template aggregates: `PixelTile<T>`, `Image<T>`, `Metatile<T>` -- parameterized on pixel type
  - Strong types: `ArtifactKey`, `ConfigValue<T>` -- wrapping primitives for type safety
  - Bitmask enums: `Style` flags for text formatting
  - The `PT_TRY_ASSIGN_CHAIN_ERR` macro: what it expands to
- **fmtlib notes**: mostly migrated to `std::format`, but `fmt::dynamic_format_arg_store` still needed for runtime variable argument counts
- Reference to `STYLE.md` for naming conventions, include ordering, and idioms (do not duplicate)

**Cross-references:** {doc}`error-handling-and-diagnostics` for the Result/Error types in detail, `STYLE.md` (external reference)
