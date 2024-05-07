@echo off 
pip3 install pytube 
cd Source
copy cipher.py %localappdata%\Programs\Python\Python312\Lib\site-packages\pytube
echo Installed