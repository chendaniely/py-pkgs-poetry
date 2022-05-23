# Py-pkgs book notes

## Installation

- My setup uses `pyenv` for the virtual environment

```bash
pipx install poetry # i did thiss
pip install cookiecutters
```

## Running code

shift + enter:

https://stackoverflow.com/questions/64730660/how-do-i-find-excute-python-interactive-mode-in-visual-studio-code

## General Setup

- conda for environment managmeent, not poetry
    - https://py-pkgs.org/03-how-to-package-a-python#create-a-virtual-environment
    - poetry does support enviornments, but poetry is just being used for packaging
- Packaging tool: poetry
    - comparisons: poetry, flint, setuptools
    - https://py-pkgs.org/04-package-structure#packaging-tools

## General Notes

- do not use `-` in package names, because `-` is also not a valid varianble name
    - https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them
    - pkg_name = `__import__("pkg_name")`

- installing package names
    - the `name` in the `pyproject.toml` needs to match the `src/pkg_name`
    - otherwise the package will not install (confirmed with using `poetry install`)
