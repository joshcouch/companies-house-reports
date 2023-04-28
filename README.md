# Companies House Reports

There are lots of corporate reports on companies house. They are in a non-text pdf format, so you can't `ctrl` + `f` things :(


### Manage venv
Using pip-tools to manage venv requirements. Top-level package requirements are in `requirements.in`. The advatange is you can easily distinguish between top-level packages (i.e. the ones we chose to install), and the dependencies of the top-level packages (i.e. the ones that get installed by pip automatically).

To create venv:

1. `python -m venv VENV_NAME`  -> create new virtualenv
1. `VENV_NAME/Scripts/Activate.ps1` -> activate virtualenv (`chrenv/Scripts/Activate.ps1`)
1. `pip install pip-tools`  -> install pip-tools (Currently using 6.13.0)
1. `pip-sync` -> install packages

To add new top-level packages to the virtualenv:

1. Add them to requirements.in  
1. `pip-compile` -> compile new `requirements.txt` from `requirements.in`
1. `pip-sync` -> install packages

### ocrmypdf
Using [ocrmypdf](https://pypi.org/project/ocrmypdf/) python package to convert PDF files to PDF/A files (make them searchable). This uses OCR and interacts with PDFs, so it requires some additional installations, including ghostscript and tesseract. For more information see the [documentation](https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows)


## Scraper
To run the scraper, navigate to `ch_scraping` and run `python ch_scraper.py SEARCH_TERM`. If no `SEARCH_TERM` is specified, it will default to `"bp plc"`.

## Website stuff

companieshousereports.com available for £10/year [link](https://domains.google.com/registrar/search?searchTerm=companieshousereports.com&hl=en)
companieshousedata.uk also available for £10/year [link](https://domains.google.com/registrar/search?searchTerm=companieshousedata.uk&hl=en)