#!/bin/bash

echo "++++++++++ SETTING UP PICHUB ++++++++++"
echo "[*]"
echo "[*] removing dumb caches"
echo "[*] Run: rm -r __pycache__/"
rm -r __pycache__/
echo "[*] caches removed"
echo "[*] running PicHub server"
echo "[*] Status: Ready"
echo "[*] Run: export FLASK_APP=main"
export FLASK_APP=main
echo "[*] Run: flask run"
echo "[*]"
echo "[*] PicHub"
echo "[*] Developed by: Alan Tsui, Kenny Yu"
echo "[*] One Stop Shop for Your Photo Portfolio"
echo "[*] Status: Running"
echo "[*]"
flask run
