color 2
::������� ����� �ணࠬ��
taskkill /f /im "Extract frames from video.exe"
:: ����᪠�� �������� �஥�� � ������� pyinstaller
:: �।���⥫쭮 ��⠭���� ����஢�� - ��ਫ�� OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "Extract frames from video.py"
:: ����᪠�� �ணࠬ�� ��᫥ �������樨
cd dist
start "Extract frames from video" "Extract frames from video.exe"