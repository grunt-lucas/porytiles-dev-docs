# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pathlib import Path

project = 'Porytiles Developer Documentation'
copyright = '2026, grunt-lucas'
author = 'grunt-lucas'

# Version read from the top-level VERSION file (kept in lockstep with the main porytiles repo).
_version_str = (Path(__file__).parent.parent / 'VERSION').read_text().strip()
version = release = _version_str

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
]

# MyST parser configuration
myst_enable_extensions = [
    'amsmath',
    'attrs_block',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]

suppress_warnings = ['myst.strikethrough']

myst_substitutions = {
    'project_name': 'Porytiles',
    'version': _version_str,
    'author': 'grunt-lucas',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# GitHub context for "Edit on GitHub" links
html_context = {
    'display_github': True,
    'github_user': 'grunt-lucas',
    'github_repo': 'porytiles-dev-docs',
    'github_version': 'master',
    'conf_py_path': '/docsrc/',
}

# -- Options for MyST parser -------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
