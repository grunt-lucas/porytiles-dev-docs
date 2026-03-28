# Error Handling and User Diagnostics

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Covers two tightly related systems: the error propagation model and the diagnostic output system.

- **Error handling philosophy**: no C++ exceptions; two mechanisms for two purposes:
  - `ChainableResult<T, E>` for recoverable errors (most of the codebase)
  - `panic()` / `assert_or_panic()` for programmer errors / invariant violations (immediate abort with source location)
- **`ChainableResult<T, E>`**: monadic result type, move-only, error chain accumulation
  - How chaining works: preserves the full path from root cause to proximate error
  - The `PT_TRY_ASSIGN_CHAIN_ERR` macro for ergonomic propagation (similar to Rust's `?` operator)
- **`Error` interface and `FormattableError`**:
  - Format strings with styled `FormatParam` parameters
  - The message style rules (capital first letter, ends with period, single quotes around highlighted items)
- **`UserDiagnostics` system**:
  - Abstract interface: `remark()`, `warning()`, `error()`, `fatal()` at four severity levels
  - Tag-based filtering: regex include/exclude patterns
  - Concrete implementations: `StderrStyledUserDiagnostics`, `BufferedUserDiagnostics`, `NullUserDiagnostics`, `FilteredUserDiagnostics`
- **`TextFormatter` integration**: `AnsiStyledTextFormatter` vs `PlainTextFormatter`, selected via DI
- **When to use which**: Result for domain/app errors, panic for precondition violations, diagnostics for user-facing messages

**Cross-references:** {doc}`dependency-injection` for how formatter/diagnostics are injected, {doc}`writing-tests` for testing with `BufferedUserDiagnostics`, {doc}`cpp-features-and-patterns` for the macro details
