Create virtual env:
pip install virtualenv
py -m venv .venv

Install de application in the virtual env:
source .venv/Scripts/activate
pip install --editable .

Find the installed app:
which pv

Search for documentation of the installe app
pv --help
pv clients --help