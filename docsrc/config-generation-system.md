# The Configuration Code Generation System

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

The most complex and unique system in the project. A single YAML file drives the generation of ~38 C++ files across three architectural layers.

- Overview: `config_schema.yaml` (780+ lines) -> `Scripts/generate_config.py` -> 24 Jinja2 templates -> ~38 generated C++ files
- **The schema format** -- fields per config value:
  - `canonical_name`, `symbol`, `yaml_path`, `cli_option`, `cli_desc`
  - `layer`, `type`, `parser`, `default_value`
  - `validators`, `cross_field_validators`
  - `header_define`, `yaml_only`, `yaml_is_map`
- **Enum type definitions** in the schema: what they generate (enum class, `*_from_str()`, `to_string()`, fuzzy matching)
- **What gets generated and where**:
  - Layer config interfaces: `DomainConfig`, `AppConfig`, `InfraConfig`
  - `LazyLayeredConfig`: single class implementing all three interfaces
  - Config providers: `DefaultProvider`, `YamlFileProvider`, `HeaderDefineProvider`, `CliOptionProvider`
  - CLI integration: `CliOptionStorage`, `CliOptionRegistration`, `CliCompletionData`
  - Mock configs for testing
- **The provider priority chain**: CLI > per-tileset local YAML > per-tileset YAML > project local YAML > project YAML > header defines > defaults
- **`ConfigValue<T>`**: the wrapper that tracks provenance
- **Three-tier validation**: raw fetch -> single-value validators -> cross-field validators
- **How CMake triggers regeneration**

**Cross-references:** {doc}`adding-a-config-value` for the step-by-step recipe, {doc}`layered-architecture` for why config interfaces are split by layer
