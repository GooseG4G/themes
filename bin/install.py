from os import environ
from subprocess import run
from pathlib import Path

# Определение базового и домашнего пути
BASE = Path(__file__).parents[1].absolute()
HOME = Path.home() / "AppData" / "Local" / "Goose Apps"

# Определение путей
AI = BASE / "ai"
GAPP = HOME / "Themes"

GAPP.mkdir(exist_ok=True, parents=True)
MAGICK = BASE / "bin" / "magick" / "magick.exe"

ENV = environ.copy()
ENV["PATH"] += f";{BASE / "bin" / "ghost"}"

# Получение списка всех .ai файлов в директории
ai_files = list(AI.glob('*.ai'))

for i, ai_file in enumerate(ai_files):
    ico_file = GAPP / ai_file.with_suffix('.ico').name
    run([MAGICK, ai_file, ico_file], env=ENV)
    print(
        f'{round((i+1)/len(ai_files)*100, 2)}%'
        f'\t{ai_file.name} -> {ico_file.name}'
    )
