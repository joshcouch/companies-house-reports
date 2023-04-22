# Companies House Reports

There are lots of corporate reports on companies house. They are in a non-text pdf format, so you can't `ctrl` + `f` things :(


### Manage venv
Using pip-tools to manage venv requirements. Top-level package requirements are in `requirements.in`. The advatange is you can easily distinguish between top-level packages (i.e. the ones we chose to install), and the dependencies of the top-level packages (i.e. the ones that get installed by pip automatically).

To create venv:

1. `python -m venv VENV_NAME`  -> create new virtualenv
1. `VENV_NAME/Scripts/Activate.ps1` -> activate virtualenv
1. `pip install pip-tools`  -> install pip-tools (Currently using 6.13.0)
1. `pip-sync` -> install packages

To add new top-level packages to the virtualenv:

1. Add them to requirements.in  
1. `pip-compile` -> compile new requirements.txt from requirements.in
1. `pip-sync` -> install packages
