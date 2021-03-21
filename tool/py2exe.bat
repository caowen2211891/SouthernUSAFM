pyinstaller -w -i main.ico analysis.py

pyuic5 -o UI_Main.py UI_Main.ui
pyuic5 -o UI_Config.py UI_Config.ui
pyuic5 -o UI_Detail.py UI_Detail.ui

pyinstaller analysis.spec