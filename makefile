# Определение переменных
PYTHON := python
BUILD := ./bin/build.py
CLEAN := ./bin/clean.py

.PHONY: all run

# Цель по умолчанию
all: build

# Цель для запуска Python скрипта
build:
	$(PYTHON) $(BUILD)

clean:
	$(PYTHON) $(CLEAN)

install: