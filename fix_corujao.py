import os, re

BASE = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME'

# Replace any mention of CorujaoCS / CorujãoCS in game files only
REPLACEMENTS = [
    # in explanation strings inside JS/HTML
    (r'CorujãoCS',  'a base de conhecimento'),
    (r'CorujaoCS',  'a base de conhecimento'),
    (r'Coruj\u00e3oCS', 'a base de conhecimento'),
    # possessive variants
    (r'o CorujãoCS', 'a base de conhecimento'),
    (r'no CorujãoCS', 'na base de conhecimento'),
    (r'pelo CorujãoCS', 'pela base de conhecimento'),
    (r'do CorujãoCS', 'da base de conhecimento'),
    (r'Use o DART Decisor no CorujãoCS para checar antes de transferir',
     'Consulte o DART Decisor na sua ferramenta de conhecimento antes de transferir'),
]

game_files = [f for f in sorted(os.listdir(BASE)) if 'Equipe' in f and f.endswith('.html')]
total_changes = 0
for fname in game_files:
    path = os.path.join(BASE, fname)
    c = open(path, 'rb').read().decode('utf-8')
    original = c
    for old, new in REPLACEMENTS:
        c = c.replace(old, new)
    # also catch any remaining via regex (case variants)
    c, n = re.subn(r'Coruj[aã]oCS', 'a base de conhecimento', c)
    total_changes += n + (1 if c != original else 0)
    open(path, 'wb').write(c.encode('utf-8'))
    changed = 'CHANGED' if c != original else 'ok'
    print(changed, fname)

print('Done:', len(game_files), 'game files processed')
