# Markdown Formatting Testbed

This page showcases every Markdown and MyST formatting feature available in this documentation theme. Use it as a visual reference for how different elements render with the Sphinx RTD theme.

---

## Inline Formatting

**Bold text** using double asterisks.

*Italic text* using single asterisks.

***Bold and italic*** using triple asterisks.

`Inline code` using backticks.

~~Strikethrough text~~ using double tildes. *(Requires `strikethrough` extension.)*

Here is a {sub}`subscript` using the sub role and a {sup}`superscript` using the sup role.

{abbr}`HTML (HyperText Markup Language)` using the abbr role for abbreviations.

{kbd}`Ctrl+Shift+P` renders as a keyboard shortcut.

---

## Headings

The heading hierarchy is demonstrated by the structure of this page itself. Here are the levels:

### Third-Level Heading

#### Fourth-Level Heading

##### Fifth-Level Heading

###### Sixth-Level Heading

## Paragraphs and Line Breaks

This is the first paragraph. It contains multiple sentences to demonstrate how paragraph text flows in the RTD theme. Notice how the text wraps and the line spacing behaves.

This is a second paragraph, separated from the first by a blank line.

This line has a hard line break after it.\
This is the next line, forced onto a new line within the same paragraph using a backslash.

---

## Links

### External Links

- Inline link: [Porytiles GitHub](https://github.com/grunt-lucas/porytiles)
- Bare URL (auto-linked): <https://github.com/grunt-lucas/porytiles>
- Link with title: [Porytiles GitHub](https://github.com/grunt-lucas/porytiles "Visit the Porytiles repository")

### Internal Cross-References

- Link to another page: {doc}`dev-environment-setup`
- Link to another page with custom text: {doc}`Go to Architecture <layered-architecture>`
- Reference-style link to a section on this page: [Admonitions](admonitions-section)

### Reference-Style Links

This uses [reference-style links][porytiles-ref] which define the URL elsewhere.

[porytiles-ref]: https://github.com/grunt-lucas/porytiles

---

## Lists

### Unordered Lists

- Item one
- Item two
- Item three

Alternative markers:

* Star item one
* Star item two
* Star item three

### Ordered Lists

1. First item
2. Second item
3. Third item

Starting from a different number:

5. Fifth item
6. Sixth item
7. Seventh item

### Nested Lists

- Outer item A
  - Inner item A.1
  - Inner item A.2
    - Deep item A.2.a
    - Deep item A.2.b
  - Inner item A.3
- Outer item B
  1. Numbered inner B.1
  2. Numbered inner B.2
- Outer item C

### Task Lists

*(Requires `tasklist` extension.)*

- [x] Completed task
- [x] Another completed task
- [ ] Incomplete task
- [ ] Another incomplete task
  - [x] Completed subtask
  - [ ] Incomplete subtask

---

## Blockquotes

> This is a simple blockquote. It can contain multiple sentences and will be styled with a left border in the RTD theme.

> This is a blockquote with **bold**, *italic*, and `code` inside.

### Nested Blockquotes

> Outer blockquote.
>
> > Inner nested blockquote.
> >
> > > Even deeper nesting.

### Blockquote with Attribution

> The best error message is the one that never shows up.
>
> --- Thomas Fuchs

---

## Code Blocks

### Inline Code

Use `std::vector<int>` for dynamic arrays. The function `compute_something()` returns an integer.

### Fenced Code Blocks

```c++
#include <iostream>
#include <vector>

namespace porytiles {

class TileCompiler {
  public:
    TileCompiler() = default;

    [[nodiscard]] int compile_tiles(const std::vector<Tile> &tiles) const {
        int total = 0;
        for (const auto &tile : tiles) {
            total += tile.pixel_count();
        }
        return total;
    }

  private:
    std::string name_;
};

} // namespace porytiles
```

```python
# Python example
def generate_config(schema_path: str) -> dict:
    """Generate configuration from a YAML schema."""
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)
    return process_schema(schema)
```

```bash
# Shell commands
cmake --build clion-build-debug -j7
cmake --install clion-build-debug --prefix ~/.local
./clion-build-debug/porytiles/tests/PorytilesAllTests
```

```json
{
  "name": "porytiles",
  "version": "2.0.0",
  "settings": {
    "max_palettes": 16,
    "tile_size": 8
  }
}
```

```yaml
# YAML configuration
project:
  name: porytiles
  version: 2.0.0
  settings:
    max_palettes: 16
    tile_size: 8
```

### Code Block Without Language (No Highlighting)

```
This is a plain code block.
No syntax highlighting is applied.
It preserves    whitespace    and
    indentation.
```

### Code Block with Line Numbers

```{code-block} c++
:linenos:

#include <string>

namespace porytiles {

int main() {
    std::string message = "Hello, Porytiles!";
    return 0;
}

} // namespace porytiles
```

### Code Block with Line Emphasis

```{code-block} c++
:linenos:
:emphasize-lines: 3,5-7

#include <vector>

// This line is emphasized
int process_tiles() {
    // These lines
    // are also
    // emphasized
    return 0;
}
```

### Code Block with Caption

```{code-block} c++
:caption: Example: A simple tile processor
:linenos:

struct Tile {
    int index;
    int palette_id;
};
```

### Colon Fence Code Blocks

*(Requires `colon_fence` extension.)*

:::{code-block} c++
:linenos:

// This code block uses colon fence syntax
void example() {
    // Useful when nesting directives
}
:::

---

## Tables

### Simple Pipe Table

| Feature       |   Status    |                  Notes |
|:--------------|:-----------:|-----------------------:|
| Compilation   |  Complete   |  All targets supported |
| Decompilation | In Progress | Partial implementation |
| Animation     |  Complete   |  Full keyframe support |
| Dual Layer    |   Planned   |        Not yet started |

*Note: Column alignment is demonstrated above --- left, center, and right.*

### Wide Table

| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
|----------|----------|----------|----------|----------|----------|
| Data A1  | Data A2  | Data A3  | Data A4  | Data A5  | Data A6  |
| Data B1  | Data B2  | Data B3  | Data B4  | Data B5  | Data B6  |
| Data C1  | Data C2  | Data C3  | Data C4  | Data C5  | Data C6  |

### Table with Inline Formatting

| Element       | Syntax        | Rendered                    |
|---------------|---------------|-----------------------------|
| Bold          | `**bold**`    | **bold**                    |
| Italic        | `*italic*`    | *italic*                    |
| Code          | `` `code` ``  | `code`                      |
| Link          | `[text](url)` | [text](https://example.com) |
| Strikethrough | `~~strike~~`  | ~~strike~~                  |

### List Table Directive

```{list-table} Comparison of Approaches
:header-rows: 1
:widths: 20 40 40

* - Approach
  - Pros
  - Cons
* - Direct compilation
  - Fast, simple pipeline
  - Less flexible
* - Multi-pass
  - Better optimization opportunities
  - More complex, slower
* - Hybrid
  - Balance of speed and flexibility
  - Implementation complexity
```

---

## Definition Lists

*(Requires `deflist` extension.)*

Metatile
: A 2x2 arrangement of 8x8 pixel tiles that forms a 16x16 pixel unit in the game's tileset system.

Palette
: A set of 16 colors (including one transparent color) used to color tiles. GBA games support up to 16 palettes.

Tileset
: A collection of tiles, palettes, and metatile definitions that define the visual appearance of a map area.

Primary Tileset
: The base tileset shared across many maps (e.g., general terrain).

Secondary Tileset
: A tileset layered on top of the primary, providing map-specific tiles.

### Multi-paragraph Definition

Domain-Driven Design (DDD)
: An approach to software development that centers the project on the core business domain.

  In Porytiles, the domain layer contains pure business logic with no I/O dependencies. This includes tile compilation, palette optimization, and metatile assembly.

  The infrastructure layer handles file I/O, CLI parsing, and external library integration.

---

## Field Lists

*(Requires `fieldlist` extension.)*

:Author: grunt-lucas
:Version: 2.0.0
:License: GPLv3
:Platform: Linux, macOS, Windows
:Language: C++23

---

(admonitions-section)=
## Admonitions

### Standard Admonitions

```{note}
This is a **note** admonition. Use it for supplementary information that adds context.
```

```{tip}
This is a **tip** admonition. Use it for helpful suggestions and best practices.
```

```{important}
This is an **important** admonition. Use it to highlight critical information the reader should not miss.
```

```{warning}
This is a **warning** admonition. Use it to caution about potential pitfalls or dangerous operations.
```

```{danger}
This is a **danger** admonition. Use it for actions that could cause severe problems like data loss.
```

```{caution}
This is a **caution** admonition. Similar to warning but less severe.
```

```{attention}
This is an **attention** admonition. Draws the reader's eye to something noteworthy.
```

```{hint}
This is a **hint** admonition. Like a tip, but softer --- suggesting a possible approach.
```

```{error}
This is an **error** admonition. Use it to describe error conditions or failure modes.
```

```{seealso}
This is a **see also** admonition. Use it to point readers to related topics.
- {doc}`layered-architecture`
- {doc}`writing-tests`
```

### Admonition with Custom Title

```{admonition} Custom Title Here
:class: tip

This admonition has a custom title but uses the `tip` styling.
```

### Collapsed/Dropdown Admonition

```{admonition} Click to expand (toggle)
:class: dropdown

This content is hidden by default and can be revealed by clicking the title. Useful for lengthy explanations, optional details, or spoiler content.

- Item one
- Item two
- Item three
```

### Colon Fence Admonitions

*(Requires `colon_fence` extension.)*

:::{note}
This admonition uses colon fence syntax (`:::{note}`) instead of backtick fence syntax.
Colon fences are useful when you need to nest directives.
:::

:::{warning}
Colon fence warning --- especially useful when the admonition body itself contains fenced code blocks:

```c++
// This code block inside a colon-fence admonition
void danger_zone() {
    // Proceed with caution
}
```
:::

---

## Images and Figures

### Markdown Image Syntax

![Placeholder diagram](https://via.placeholder.com/600x200/0073e6/ffffff?text=Porytiles+Architecture+Diagram)

### Sphinx Figure Directive

```{figure} https://via.placeholder.com/600x200/28a745/ffffff?text=Figure+With+Caption
:alt: Example figure
:width: 100%
:align: center

**Figure 1:** This is a figure with a caption. Figures support captions and cross-referencing, unlike plain images.
```

### Image with Specific Width

```{image} https://via.placeholder.com/400x150/6f42c1/ffffff?text=Resized+Image
:alt: Resized image example
:width: 300px
:align: center
```

---

## Mathematics

*(Requires `dollarmath` extension for `$` syntax.)*

### Inline Math

The formula for tile index calculation is $i = y \times w + x$ where $w$ is the width in tiles.

Euler's identity: $e^{i\pi} + 1 = 0$

### Display Math (Dollar Signs)

$$
P(palette) = \frac{\text{tiles using palette}}{\text{total tiles}} \times 100\%
$$

### Display Math (Directive)

```{math}
:label: quadratic

x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

### AMS Math Environment

*(Requires `amsmath` extension.)*

\begin{align}
\text{metatile\_index} &= \text{row} \times \text{cols} + \text{col} \\
\text{tile\_offset} &= \text{metatile\_index} \times 4 \\
\text{total\_tiles} &= \text{rows} \times \text{cols} \times 4
\end{align}

---

## Footnotes

This algorithm was first described in the original GBA hardware documentation[^1]. The palette optimization uses a greedy approach[^2] with some modifications for the GBA's specific constraints[^3].

[^1]: Game Boy Advance Technical Reference Manual, Chapter 12: Video.
[^2]: Cormen, T.H. et al., *Introduction to Algorithms*, Chapter 16.
[^3]: The GBA supports a maximum of 16 palettes with 16 colors each, where color index 0 is always transparent.

---

## Horizontal Rules

Three different syntaxes produce horizontal rules:

---

Here is a horizontal rule above (using `---`). And here is one below (using `***`):

***

And another below (using `___`):

___

*(They should all look identical.)*

---

## Substitutions

*(Requires `substitution` extension. Values defined in `conf.py`.)*

- Project name: {{project_name}}
- Version: {{version}}
- Author: {{author}}

---

## Smart Quotes and Replacements

*(Requires `smartquotes` and `replacements` extensions.)*

- Smart quotes: "double quotes" and 'single quotes'
- Em dash: ---
- En dash: --
- Ellipsis: ...
- Copyright: (c)
- Trademark: (tm)
- Registered: (r)

---

## Block-Level Attributes

*(Requires `attrs_block` extension.)*

{.custom-class #custom-id}
This paragraph has a custom class and ID applied to it.

---

## Inline Attributes

*(Requires `attrs_inline` extension.)*

This sentence has a [highlighted word]{.custom-class} with an inline attribute.

---

## Roles and Cross-References

### Built-in Roles

- Document reference: {doc}`layered-architecture`
- Reference with custom text: {doc}`See the architecture page <layered-architecture>`
- Emphasis role: {emphasis}`emphasized text`
- Strong role: {strong}`strong text`
- Literal role: {literal}`literal text`
- Math role: {math}`a^2 + b^2 = c^2`
- Equation reference: {eq}`quadratic` (references the labeled math block above)

---

## Rubric Directive

```{rubric} This is a Rubric
```

A rubric is an informal heading that does not appear in the table of contents. Useful for visual separation without affecting document structure.

---

## Topic Directive

```{topic} Topic: Palette Optimization Strategy
The palette optimizer in Porytiles uses a multi-phase approach:

1. **Extraction** --- Identify unique colors from input tiles
2. **Clustering** --- Group similar colors using a distance metric
3. **Assignment** --- Assign tiles to palettes minimizing total palette count
```

---

## Epigraph

```{epigraph}
In the beginner's mind there are many possibilities, but in the expert's mind there are few.

-- Shunryu Suzuki
```

---

## Pull Quote

```{pull-quote}
The key insight is that GBA tiles are fundamentally palette-indexed, not true-color. Every design decision flows from this constraint.
```

---

## Compound Paragraph

```{compound}
This is a compound paragraph. It groups multiple body elements together so they appear as a single logical unit.

- Point one
- Point two
- Point three

The items above are part of this compound unit.
```

---

## Container Directive

```{container} custom-container
This content is wrapped in a `<div>` with the class `custom-container`. Useful for applying custom CSS styling to a block of content.
```

---

## Sidebar

```{sidebar} Quick Reference
**Tile dimensions:** 8x8 pixels\
**Metatile dimensions:** 16x16 pixels\
**Max palettes:** 16\
**Colors per palette:** 16 (including transparent)
```

The sidebar appears to the right of the main content (theme permitting). It is useful for supplementary information, quick references, or asides that relate to the main text but shouldn't interrupt the flow.

This paragraph flows alongside the sidebar. In the RTD theme, sidebars typically float to the right with a distinct background color.

---

## Parsed Literal Block

```{parsed-literal}
$ porytiles compile \\
    --primary-source ./tileset_primary \\
    --secondary-source ./tileset_secondary \\
    --output ./output \\
    --verbose

Compiling tileset... **done**
Generated *16* palettes, *512* tiles
```

---

## Centered Text

```{centered} This text is centered on the page.
```

---

## Glossary

```{glossary}
GBA
  Game Boy Advance --- Nintendo's 32-bit handheld console released in 2001.

Porymap
  A map editor for Pokémon Generation III decompilation projects.

Metatile
  A 2x2 grid of 8x8 pixel tiles forming a 16x16 pixel map unit.

RGBA
  Red, Green, Blue, Alpha --- a color model with transparency support.
```

Use glossary terms with the {term}`GBA` role or {term}`Porymap` role.

---

## Versioning Directives

```{versionadded} 2.0.0
The animation decompiler was added in this release.
```

```{versionchanged} 2.0.0
The palette optimizer now uses a greedy algorithm instead of brute force.
```

```{deprecated} 1.0.0
The `--old-flag` option is deprecated. Use `--new-flag` instead.
```

---

## HTML in Markdown

*(Requires `html_admonition` and/or `html_image` extensions for HTML passthrough.)*

<div style="background-color: #f0f0f0; padding: 1em; border-radius: 5px; border-left: 4px solid #0073e6;">
  <strong>HTML Block:</strong> This is raw HTML embedded in the Markdown document. It renders directly in the output.
</div>

<br>

<details>
<summary><strong>Click to expand (HTML details/summary)</strong></summary>

This content is hidden behind a native HTML `<details>` element. Unlike the admonition dropdown, this uses the browser's built-in disclosure widget.

- Supported in all modern browsers
- No JavaScript required
- Semantic HTML

</details>

---

## Escaped Characters

These characters are escaped to display literally:

\* Not italic \*

\*\* Not bold \*\*

\` Not code \`

\# Not a heading

\- Not a list item

\[Not a link\](https://example.com)

---

## Long Content for Scroll Testing

The following section tests how the theme handles longer content blocks:

```{code-block} c++
:linenos:

// A longer code example to test scroll behavior
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>

#include "porytiles/domain/tile.hpp"
#include "porytiles/domain/palette.hpp"
#include "porytiles/domain/metatile.hpp"

namespace porytiles {

struct CompilationResult {
    std::vector<Tile> tiles;
    std::vector<Palette> palettes;
    std::vector<Metatile> metatiles;
    int total_colors_used;
    int total_palettes_used;
    bool success;
};

[[nodiscard]] CompilationResult compile_tileset(
    const std::vector<InputTile> &input_tiles,
    const CompilationOptions &options)
{
    CompilationResult result{};

    // Phase 1: Extract unique colors
    auto unique_colors = extract_unique_colors(input_tiles);

    // Phase 2: Build palette assignments
    auto assignments = optimize_palette_assignments(
        unique_colors, options.max_palettes);

    // Phase 3: Generate indexed tiles
    for (const auto &input : input_tiles) {
        auto indexed = index_tile(input, assignments);
        result.tiles.push_back(indexed);
    }

    // Phase 4: Assemble metatiles
    result.metatiles = assemble_metatiles(result.tiles, options.metatile_layout);

    // Finalize
    result.palettes = build_final_palettes(assignments);
    result.total_colors_used = static_cast<int>(unique_colors.size());
    result.total_palettes_used = static_cast<int>(result.palettes.size());
    result.success = true;

    return result;
}

} // namespace porytiles
```

---

## Summary

This page demonstrates the following MyST Markdown features:

| Category              | Features Shown                                               |
|-----------------------|--------------------------------------------------------------|
| **Inline Formatting** | Bold, italic, code, strikethrough, subscript, superscript    |
| **Structure**         | Headings (h1--h6), paragraphs, line breaks, horizontal rules |
| **Links**             | External, internal, reference-style, cross-references        |
| **Lists**             | Ordered, unordered, nested, task lists, definition lists     |
| **Blockquotes**       | Simple, nested, with attribution                             |
| **Code**              | Inline, fenced, line numbers, emphasis, captions             |
| **Tables**            | Pipe tables, wide tables, list tables                        |
| **Admonitions**       | All 10+ types, custom titles, dropdowns, colon fence         |
| **Images**            | Markdown syntax, figure directive, resized                   |
| **Math**              | Inline, display, directive, AMS environments                 |
| **Footnotes**         | Numbered footnotes with references                           |
| **Substitutions**     | Variable replacement from conf.py                            |
| **Smart Typography**  | Quotes, dashes, ellipsis, symbols                            |
| **Directives**        | Topic, rubric, sidebar, epigraph, parsed-literal, glossary   |
| **Versioning**        | versionadded, versionchanged, deprecated                     |
| **HTML**              | Raw HTML blocks, details/summary                             |
| **Attributes**        | Block-level and inline attributes                            |
