import re, unicodedata

def slugify(s: str) -> str:
    # 1) normalize accents -> ASCII; 2) lowercase/trim
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = s.lower().strip()
    # 3) spaces -> dashes
    s = re.sub(r'\s+', '-', s)
    # 4) strip invalid chars (keep a–z, 0–9, dash)
    s = re.sub(r'[^a-z0-9-]', '', s)
    # 5) collapse multiple dashes and trim
    s = re.sub(r'-{2,}', '-', s).strip('-')
    
    return s
