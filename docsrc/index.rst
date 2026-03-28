Porytiles Developer Documentation
==================================

Welcome to the Porytiles developer documentation! This documentation covers the architecture, core systems, contributing recipes, and reference material for Porytiles development.

The target audience is a **C++ developer who may be new to the Porytiles codebase** but is not new to programming. The goal is "what you need to know to contribute effectively" -- not an exhaustive API reference for every class.

.. note::

   This documentation is for Porytiles **v2.0.0**. For documentation matching an older release,
   checkout the corresponding `git tag <https://github.com/grunt-lucas/porytiles-dev-docs/tags>`_
   and build locally with ``cd docsrc && uv run make html``.

About This Documentation
------------------------

This documentation is organized according to the `Diataxis framework <https://diataxis.fr/>`_, a systematic approach to technical documentation that distinguishes four types of content based on the reader's needs:

- **Tutorials** (Getting Started) --- learning-oriented, step-by-step walkthroughs that take you from zero to a working build. Follow these when you are new to the project.
- **Explanation** (Architecture, Core Systems) --- understanding-oriented content that clarifies the codebase structure, design decisions, patterns, and the "why" behind the system. Read these to build a mental model before contributing.
- **How-to Guides** --- task-oriented, step-by-step recipes for common contributor tasks. Consult these when you need to add a config value, implement a new command, extend the packing system, or write tests.
- **Reference** --- information-oriented, precise descriptions of build commands, dependencies, scripts, and CI/CD. Look things up here when you need exact details.

The in-repo ``Porytiles2/ARCHITECTURE.md`` provides a detailed codemap optimized for quick reference. This documentation site **complements** that document with deeper dives, worked examples, data flow walkthroughs, and contributor recipes.

For class-level and function-level API details, consult the `Doxygen API reference <https://grunt-lucas.github.io/porytiles/>`_. That site is auto-generated from source comments and covers every public interface. Use it alongside this documentation: start here for architecture and concepts, then drill into Doxygen when you need the exact signature, parameters, or preconditions for a specific class or function.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   dev-environment-setup

.. toctree::
   :maxdepth: 2
   :caption: Architecture

   project-layout
   layered-architecture
   data-flow-and-pipelines
   dependency-injection
   cpp-features-and-patterns

.. toctree::
   :maxdepth: 2
   :caption: Core Systems

   config-generation-system
   error-handling-and-diagnostics
   c-parser

.. toctree::
   :maxdepth: 2
   :caption: How-To Guides

   adding-a-config-value
   adding-a-command
   adding-a-packing-strategy
   adding-a-di-managed-service
   writing-tests

.. toctree::
   :maxdepth: 2
   :caption: Reference

   build-and-test
   external-dependencies
   scripts-and-tooling
   ci-cd
   glossary

.. toctree::
   :hidden:

   testbed

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
