#!/data/data/com.termux/files/usr/bin/bash

# Setup Folder
BIN_DIR="$PREFIX/bin"
LIB_DIR="$PREFIX/lib/boardlang"

echo "Memasang Board-lang ke sistem..."

mkdir -p $LIB_DIR
cp lexer.py engine.py board.py $LIB_DIR/

# Bikin shortcut perintah 'board'
echo "#!/usr/bin/python3
import sys
sys.path.append('$LIB_DIR')
from board import run_interpreter
if __name__ == '__main__':
    run_interpreter()
" > $BIN_DIR/board

chmod +x $BIN_DIR/board

echo "Instalasi sukses! Gunakan perintah 'board' untuk mencoba."
