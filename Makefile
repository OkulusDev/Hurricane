DEVELOPER=OkulusDev

PYTHON=python3
PIP=pip3

LIBDIR=libhurricane
RESDIR=res

REQFILE=requirements.txt
CONFIGFILE=config.ini
MAINFILE=hurricane.py
LICENSEFILE=LICENSE

MAINLANG=Python

install:
	$(PIP) install -r $(REQFILE)
	chmod +x $(MAINFILE)
