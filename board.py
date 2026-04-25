import sys
import os
from lexer import tokenize
from engine import BoardEngine

def run_interpreter():
    if len(sys.argv) < 2:
        print("Penggunaan: board <file.board>")
        return

    interpreter = BoardEngine()
    target_file = sys.argv[1]

    if not os.path.exists(target_file):
        print(f"File '{target_file}' tidak ditemukan!")
        return

    with open(target_file, 'r') as f:
        for line in f:
            tokens = tokenize(line)
            if tokens:
                cmd, args = tokens
                interpreter.execute(cmd, args)

if __name__ == "__main__":
    run_interpreter()
