# Setting Up Your Development Environment

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

The first page any new contributor reads. Purely procedural, gets you from zero to a working build.

- Prerequisites: C++23 compiler (Clang 17+ recommended, GCC 14+), CMake 3.20+, `uv` (Python package manager for code generation and scripts)
- Platform-specific notes: macOS (Homebrew Clang), Linux (system Clang or GCC)
- Cloning the repo
- First build walkthrough: `cmake -S . -B porytiles-build-debug -DCMAKE_BUILD_TYPE=Debug` then `cmake --build porytiles-build-debug -j7`
- Emphasis on the build directory name convention (`porytiles-build-debug`, **never** `build`)
- Running the full test suite to verify the build
- Installing the built executable: `cmake --install porytiles-build-debug --prefix ~/.local`
- Editor/IDE setup tips: clangd configuration, `compile_commands.json` symlink
- Troubleshooting common first-build issues (missing `uv`, wrong compiler version, FetchContent download failures)

**Cross-references:** {doc}`project-layout` for orientation, {doc}`build-and-test` for full build details
