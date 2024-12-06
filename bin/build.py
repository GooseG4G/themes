from os import environ
from subprocess import run
from pathlib import Path

# Определение базового пути относительно расположения текущего файла скрипта

BASE_DIRECTORY = Path(__file__).parents[1].absolute()

# Определение путей
AI_PATH = BASE_DIRECTORY / "ai"
ICO_PATH = BASE_DIRECTORY/ "ico"
ICO_PATH.mkdir(exist_ok=True)
MAGICK = BASE_DIRECTORY / "bin" / "magick" / "magick.exe"

ENV = environ.copy()
ENV["PATH"] += f";{BASE_DIRECTORY / "bin" / "ghost"}"

# Получение списка всех .ai файлов в директории
ai_files = list(AI_PATH.glob('*.ai'))

for ai_file in ai_files:
    ico_file = ICO_PATH / ai_file.with_suffix('.ico').name
    run([MAGICK, ai_file, ico_file], env=ENV)
    print(f'{ai_file.name} -> {ico_file.name}')

print("Success")
