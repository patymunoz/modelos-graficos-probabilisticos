# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


## Otros
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'modelos-graficos-probabilisticos'
copyright = '2025, Paty Munoz'
author = 'MCD. Paty Munoz'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'nbsphinx',
    "sphinx_book_theme"
]

myst_enable_extensions = [
    "colon_fence"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/patymunoz/modelos-graficos-probabilisticos",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
}

html_title = "Modelos gráficos probabilísticos"
html_logo = "_static/nodo.png"
html_static_path = ['_static']

# Para reconocer .md como fuente válida
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}


