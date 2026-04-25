import re

def tokenize(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    
    # Mencari pola: PERINTAH argumen
    match = re.match(r'^(\w+)\s+(.*)', line)
    if match:
        return match.group(1), match.group(2)
    return line, None
