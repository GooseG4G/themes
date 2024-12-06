import shutil
import pathlib

# Определение базового пути относительно расположения текущего файла скрипта
BASE = pathlib.Path(__file__).parents[1].absolute()
HOME = pathlib.Path.home() / "AppData" / "Local" / "Goose Apps"

# Путь к папке ico
GAPP = HOME / "Themes"

# Удаление папки ico с использованием shutil.rmtree
if GAPP.exists() and GAPP.is_dir():
    shutil.rmtree(GAPP)
    print(f"'{GAPP}' has been removed.")
else:
    print(f"'{GAPP}' does not exist.")
