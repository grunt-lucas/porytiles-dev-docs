# CI/CD and Release Process

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

Reference for the GitHub Actions setup.

- Workflow files in `.github/workflows/`
- Build matrix:
  - Linux Clang (amd64 + arm64) -- primary CI targets
  - macOS Clang (arm64) -- Apple Silicon
  - Linux GCC -- planned (waiting for C++23 support in GitHub Actions runners)
- `dev_build.yml`: triggered on pushes to `develop` branch and manual dispatch
- `pr_dev_build.yml`: triggered on pull requests
- `nightly_release.yml`: scheduled nightly release builds
- Reusable workflow template: `build_jobs_template.yml` with composite actions for install, build, test
- What CI checks: build success on all matrix entries, all tests pass
- Branch strategy: `develop` as the primary development branch, feature branches merged via PR
- Documentation deployment: separate workflow for GitHub Pages

**Cross-references:** {doc}`build-and-test` for local equivalents of CI steps
