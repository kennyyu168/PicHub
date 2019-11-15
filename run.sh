#!/bin/bash

echo "++++++++++ SETTING UP PICHUB ++++++++++"
echo "[*]"
echo "[*] removing dumb caches"
echo "[*] Run: rm -r __pycache__/"
rm -r __pycache__/
echo "[*] caches removed"
echo "[*] running PicHub server"
echo "[*] Status: Ready"
echo "[*] Run: export FLASK_APP=pichub"
export FLASK_APP=pichub
echo "[*] Run: flask run"
echo "[*]"
echo "[*] PicHub"
echo "[*] One stop shop for your photo portfolio"
echo "[*] Developed by: Alan Tsui, Kenny Yu"
echo "[*] Status: Running"
echo "[*]"
flask run
