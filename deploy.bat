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