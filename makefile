# Определение переменных
PYTHON := python
INSTALL := ./bin/install.py
UNINSTALL := ./bin/uninstall.py
BUILD := ./bin/build.py
CLEAN := ./bin/clean.py

.PHONY: all run

# Цель по умолчанию
all: install

# Цель для запуска Python скрипта
install:
	$(PYTHON) $(INSTALL)

uninstall:
	$(PYTHON) $(UNINSTALL)