# The C Parser System

```{admonition} Page Status
:class: warning
This page is a placeholder. Content coming soon.
```

A standalone subsystem that deserves dedicated documentation since it is non-trivial and critical for the import pipeline.

- **Purpose**: parse pokeemerald C/C++ header files to discover enum declarations, `#define` constants, `INCBIN` paths, function definitions, struct declarations, designated initializer lists
- **Location**: `utilities/c_parser/` -- lives in utilities because it has zero project-specific dependencies
- **Architecture**: lexer (`lexer.hpp`) -> token stream (`token.hpp`) -> parser (`parser.hpp`) -> AST node types
- **AST node types** and what each represents:
  - `EnumDeclaration` / `EnumMember`, `DefineStatement`, `IncbinDeclaration`
  - `FunctionDefinition` / `FunctionCallInfo`, `StructVariableDeclaration` / `DesignatedInitializerField`
  - `ArrayDeclaration`
- **`CParserFacade`**: high-level entry point that wraps the lexer+parser
- **How the import pipeline uses it**: `HeaderBehaviorMapProvider` reads `metatile_behaviors.h`, `HeaderDefineProvider` reads `fieldmap.h`, import use case reads `graphics.h` and `tileset_anims.c`
- **Testing the parser**: unit tests with string inputs, no file I/O needed

**Cross-references:** {doc}`data-flow-and-pipelines` for how import uses the parser, {doc}`layered-architecture` for why it lives in utilities
