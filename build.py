import os
import subprocess
from pathlib import Path

# Определение путей
input_path = Path("./ai")
output_path = Path("./ico")
output_path.mkdir(exist_ok=True)

# Обновление переменной окружения PATH
magick_path = Path("./bin/ImageMagick/magick.exe")

env = os.environ.copy()
ghost_path = str(Path("./bin/Ghostscript/bin/"))
env["PATH"] = f"{ghost_path};" + env["PATH"]

# Получение списка всех .ai файлов в директории
ai_files = list(input_path.glob('*.ai'))

for ai_file in ai_files:
    ico_file = output_path / ai_file.with_suffix('.ico').name

    # Конвертация AI в ICO с помощью ImageMagick
    result = subprocess.run([
        magick_path, ai_file, ico_file
    ], env=env, capture_output=True, text=True)
    
    print(f'{ai_file} -> {ico_file}')

print("Success")
