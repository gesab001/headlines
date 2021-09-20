git pull
git add .
git commit -m "update news"
git push --all

pyinstaller --onefile main.py
del headlines.exe
cd dist
ren  main.exe headlines.exe
move headlines.exe ../
cd ..

pyinstaller --onefile installpyqt5.py
del installpyqt5.exe
cd dist
move installpyqt5.exe ../
cd ..
setup_inno_script.iss