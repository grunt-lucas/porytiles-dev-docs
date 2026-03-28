# Writing Tests

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Patterns and conventions for the test suite.

- **Unit tests vs integration tests**: when to use each
  - Unit: no I/O, no filesystem, all dependencies mocked, tests a single component in isolation
  - Integration: real file I/O, real assets from `Resources/`, tests multiple components together
- Test directory structure: `tests/unit/` mirrors the source layout, `tests/integration/` organized by feature
- GoogleTest basics for contributors who have not used it: `TEST`, `TEST_F`, `EXPECT_*`, `ASSERT_*`
- Custom test main (`test_main.cpp`): stacktrace control with `--enable-stacktrace`
- Testing with `BufferedUserDiagnostics`: inject it, run code, assert on buffered messages
- Testing with generated mock configs: `MockDomainConfig`, `MockAppConfig`, `MockInfraConfig`
- Testing `ChainableResult` error paths: checking error chains, verifying error messages
- Testing domain algorithms: pure functions are trivial to test
- Integration test resources: where they live (`Resources/`), how to add new test fixtures
- Running specific tests: GoogleTest filter flags (`--gtest_filter`)
- Code coverage: using `Scripts/coverage.py` to verify new code paths are exercised

**Cross-references:** {doc}`error-handling-and-diagnostics` for testing error paths, {doc}`build-and-test` for running the suite and coverage
