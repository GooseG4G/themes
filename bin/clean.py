import shutil
import pathlib

# Определение базового пути относительно расположения текущего файла скрипта
BASE_PATH = pathlib.Path(__file__).parents[1].absolute()

# Путь к папке ico
ICO_PATH = BASE_PATH / "ico"

# Удаление папки ico с использованием shutil.rmtree
if ICO_PATH.exists() and ICO_PATH.is_dir():
    shutil.rmtree(ICO_PATH)
    print(f"Folder '{ICO_PATH}' has been removed.")
else:
    print(f"Folder '{ICO_PATH}' does not exist.")
