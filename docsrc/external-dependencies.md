# External Dependencies

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Quick reference for every third-party library: what it provides, why it was chosen, and where it is used.

| Library | Version | Purpose | Used In |
|---------|---------|---------|---------|
| **fmt** (fmtlib) | 11.1.4 | String formatting (`dynamic_format_arg_store`) | Throughout |
| **GSL** | v4.2.0 | `gsl::not_null`, safety annotations | Throughout |
| **png++** | HEAD | Header-only libpng wrapper | `infra/services/` (PNG I/O) |
| **nlohmann/json** | v3.12.0 | JSON parsing (header-only) | `infra/services/` (`anim.json`) |
| **yaml-cpp** | master | YAML config file parsing | `infra/config/` |
| **cpptrace** | v0.7.5 | Cross-platform stacktrace capture | `utilities/panic/`, test main |
| **Google Fruit** | master | Dependency injection framework | `xcut/di/` |
| **CLI11** | v2.5.0 | Command-line argument parsing | `tools/driver/` |
| **GoogleTest** | v1.16.0 | Testing framework | `tests/` only |

- How dependencies are fetched: CMake FetchContent with pinned versions
- System dependencies: `libpng` and `zlib` (via `find_package`)
- The Fruit C++17 workaround: Fruit is built with C++17 during fetch, then restored to C++23
- Adding a new dependency: where to add in `lib/CMakeLists.txt`, FetchContent pattern to follow

**Cross-references:** {doc}`build-and-test` for build system details, {doc}`dependency-injection` for Fruit specifics
