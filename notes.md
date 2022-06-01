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

- Installing + adding `matplotlib`
    - `poetry add matplotlib` takes a while
```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % poetry add matplotlib
Using version ^3.5.2 for matplotlib

Updating dependencies
Resolving dependencies... (89.2s)

Writing lock file

Package operations: 10 installs, 0 updates, 0 removals

  • Installing pyparsing (3.0.9)
  • Installing packaging (21.3)
  • Installing tomli (2.0.1)
  • Installing cycler (0.11.0)
  • Installing fonttools (4.33.3)
  • Installing kiwisolver (1.4.2)
  • Installing numpy (1.22.4)
  • Installing pillow (9.1.1)
  • Installing setuptools-scm (6.4.2)
  • Installing matplotlib (3.5.2)
```
- `poetry add` It also installs the missing packages into somewhere weird... `file:///Users/danielchen/Library/Caches/pypoetry/artifacts/`
```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % pip freeze
arrow==1.2.2
binaryornot==0.4.4
certifi==2022.5.18.1
chardet==4.0.0
charset-normalizer==2.0.12
click==8.1.3
cookiecutter==1.7.3
cycler @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/ba/28/11/cf3c90b4ca621519019fffb7d9019a6a62f7219045ac852aeaa6d70eee/cycler-0.11.0-py3-none-any.whl
fonttools @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/6a/c9/b0/daaca061f1da576b3ac4975b064d75f39e1ee2cd0cb30be8f27ad82ad2/fonttools-4.33.3-py3-none-any.whl
idna==3.3
Jinja2==3.1.2
jinja2-time==0.2.0
kiwisolver @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/ee/a1/a4/31eb580060c6536b09665db68daf930a3b7299dc2f3ed6260fe97292eb/kiwisolver-1.4.2-cp310-cp310-macosx_11_0_arm64.whl
MarkupSafe==2.1.1
matplotlib @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/e6/7d/dc/1378ad89957d993e9cb44cbd80feaf7ac9c0e15429d24a04906923cbe7/matplotlib-3.5.2-cp310-cp310-macosx_11_0_arm64.whl
numpy @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/24/55/2f/4998d42da79d2c140ed9ae3acf15e3ca07086e5b821128949b3dbfd0f7/numpy-1.22.4-cp310-cp310-macosx_11_0_arm64.whl
packaging @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/d3/1f/90/3f2473250ebd055fe7f0856810677783949fc0d2e5f25bbb4dc00ad0a9/packaging-21.3-py3-none-any.whl
Pillow @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/52/79/58/1dbe7506d0e35ba32c707da5aa1f772d6ebd53591cde4d2b0b1187e09c/Pillow-9.1.1-cp310-cp310-macosx_11_0_arm64.whl
poyo==0.5.0
pycounts-poetry==0.1.0
pyparsing @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/e1/09/c0/6a6df3ef412eb19fcda1b353ea54e3b48f9c518348fadd0967a962cbb6/pyparsing-3.0.9-py3-none-any.whl
python-dateutil==2.8.2
python-slugify==6.1.2
requests==2.27.1
setuptools-scm @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/07/32/3e/daaca33fafcc46341f41b03799ee9e5818f84978949190fae930908209/setuptools_scm-6.4.2-py3-none-any.whl
six==1.16.0
text-unidecode==1.3
tomli @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/62/12/b6/6db9ebb9c8e1a6c5aa8a92ae73098d8119816b5e8507490916621bc305/tomli-2.0.1-py3-none-any.whl
urllib3==1.26.9
```
- However, it doesn't seem to corrupt my base `pyenv` enviornment (which is good!)
```
danielchen@heartsbane py-pkgs-poetry % pyenv versions
  system
* 3.10.3 (set by PYENV_VERSION environment variable)
  3.10.3/envs/dsci100
  3.10.3/envs/py-pkgs-poetry
  3.10.3/envs/pygradethis
  3.9.11
  3.9.11/envs/ds
  ds
  dsci100
  py-pkgs-poetry
  pygradethis
danielchen@heartsbane py-pkgs-poetry % pip freeze
danielchen@heartsbane py-pkgs-poetry % pyenv shell py-pkgs-poetry
(py-pkgs-poetry) danielchen@heartsbane py-pkgs-poetry % pip freeze
arrow==1.2.2
binaryornot==0.4.4
certifi==2022.5.18.1
chardet==4.0.0
charset-normalizer==2.0.12
click==8.1.3
cookiecutter==1.7.3
cycler @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/ba/28/11/cf3c90b4ca621519019fffb7d9019a6a62f7219045ac852aeaa6d70eee/cycler-0.11.0-py3-none-any.whl
fonttools @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/6a/c9/b0/daaca061f1da576b3ac4975b064d75f39e1ee2cd0cb30be8f27ad82ad2/fonttools-4.33.3-py3-none-any.whl
idna==3.3

...

setuptools-scm @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/07/32/3e/daaca33fafcc46341f41b03799ee9e5818f84978949190fae930908209/setuptools_scm-6.4.2-py3-none-any.whl
six==1.16.0
text-unidecode==1.3
tomli @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/62/12/b6/6db9ebb9c8e1a6c5aa8a92ae73098d8119816b5e8507490916621bc305/tomli-2.0.1-py3-none-any.whl
urllib3==1.26.9
```

## Testing

- Installing pytest with `poetry add --dev pytest` to add a development dependency
```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % poetry add --dev pytest
Using version ^7.1.2 for pytest

Updating dependencies
Resolving dependencies... (3.6s)

Writing lock file

Package operations: 5 installs, 0 updates, 0 removals

  • Installing attrs (21.4.0)
  • Installing iniconfig (1.1.1)
  • Installing pluggy (1.0.0)
  • Installing py (1.11.0)
  • Installing pytest (7.1.2)
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % pyenv which pytest
/Users/danielchen/.pyenv/versions/py-pkgs-poetry/bin/pytest
```
- But this seems like it isn't in the PATH

```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % which pytest
pytest not found
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % pytest
```

- most likely this is due to my `pyenv` enviornment, but `python -m pytest` should fix it since it is in the `pip freeze | grep pytest`

```
(py-pkgs-poetry) danielchen@heartsbane py-pkgs-poetry % pip freeze | grep pytest
pytest @ file:///Users/danielchen/Library/Caches/pypoetry/artifacts/81/e7/80/83cc65ea38ab41a59121aea7e519147cea204e1eaf989149cc12b3b342/pytest-7.1.2-py3-none-any.whl
```

```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % python -m pytest tests/
============================================ test session starts =============================================
platform darwin -- Python 3.10.3, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/danielchen/temp/py-pkgs-poetry/pycounts
collected 1 item                                                                                             

tests/test_pycounts.py .                                                                               [100%]

============================================= 1 passed in 0.00s ==============================================
```

- Can also use `poetry run` (as mentioned in the book)

```
(py-pkgs-poetry) danielchen@heartsbane pycounts_poetry % poetry run pytest tests/
============================================ test session starts =============================================
platform darwin -- Python 3.10.3, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/danielchen/temp/py-pkgs-poetry/pycounts
collected 1 item                                                                                             

tests/test_pycounts.py .                                                                               [100%]

============================================= 1 passed in 0.00s ==============================================
```

# Code Coverage

- uses the `pytest-cov` pytest extension.

```
poetry add --dev pytest-cov
```

- can also install using `pip install pytest-cov`

- call the coverage with `pytest tests/ --cov=pycounts_poetry`

