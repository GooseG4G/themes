@echo off
setlocal enabledelayedexpansion

:: Указываем путь к папке с AI файлами
set "aiFolderPath=.\ai"

:: Указываем путь к папке, где будут сохраняться ICO файлы
set "icoFolderPath=.\ico"

:: Проходим по каждому AI файлу
for %%F in ("%aiFolderPath%\*.ai") do (
    :: Получаем имя файла без расширения
    set "fileNameWithoutExtension=%%~nF"

    :: Создаем путь к ICO файлу
    set "icoFilePath=!icoFolderPath!\!fileNameWithoutExtension!.ico"

    :: Выводим информацию о процессе выполнения
    echo Converting "%%F" to "!icoFilePath!"

    :: Выполняем конвертацию с помощью ImageMagick
    magick convert "%%F" "!icoFilePath!"
)

echo All files have been converted.

endlocal

PAUSE
