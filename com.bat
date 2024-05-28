color 2
::Убиваем процесс программы
taskkill /f /im "Extract frames from video.exe"
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "Extract frames from video.py"
:: Запускаем программу после компиляции
cd dist
start "Extract frames from video" "Extract frames from video.exe"