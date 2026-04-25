import re
import random

class BoardEngine:
    def __init__(self):
        self.papan = None
        self.pemain = []

    def execute(self, cmd, args):
        # Logika BUAT (papan atau pemain)
        if cmd == "BUAT":
            if "papan" in args:
                dimensi = re.findall(r'\[(.*?)\]', args)
                self.papan = dimensi[0] if dimensi else "0x0"
                print(f"[System] Papan {self.papan} berhasil dibuat.")
            elif "pemain" in args:
                daftar = re.findall(r'\{(.*?)\}', args)
                if daftar:
                    self.pemain = [p.strip() for p in daftar[0].split(',')]
                    print(f"[System] Pemain: {', '.join(self.pemain)} telah siap.")

        # Logika OUTPUT
        elif cmd == "tulis":
            print(f"> {args}")

        # Logika ACAK (dadu)
        elif cmd == "acak":
            if args == "dadu":
                print(f"[Dice] Hasil kocokan: {random.randint(1, 6)}")
        
        else:
            print(f"[Error] Perintah '{cmd}' tidak dikenali.")
