Инструкция по запуску и сборке Arkanoid v2:

1. Установи Python 3.10+ и библиотеки:
   pip install pygame pyinstaller

2. Запуск игры напрямую:
   python arkanoid.py

3. Сборка в exe (Windows):
   Дважды кликни build.bat
   (он выполнит pyinstaller --onefile --noconsole arkanoid.py)

Готовый exe появится в папке dist.
