@echo off
set "PATH=%PATH%;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Program Files (x86)\Git\cmd;C:\Users\%USERNAME%\AppData\Local\Programs\Git\cmd"

echo Configuring Git identity...
git config user.email "bot@daz.ai"
git config user.name "Daz.AI Assistant"

echo Committing...
git add .
git commit -m "Initial commit of Daz.AI-Workforce"

echo Linking remote...
git branch -M main
git remote remove origin
git remote add origin https://github.com/mrbug9112002-pixel/Daz.AI-Workforce.git

echo Pushing...
git push -u origin main
