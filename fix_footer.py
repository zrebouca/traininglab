import os
BASE = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME'
OLD = 'Paulo Mateus Rebou\u00e7as de Oliveira'
NEW = 'Mateus Rebou\u00e7as (zrebouca \u2014 Team Manager)'
files = sorted(f for f in os.listdir(BASE) if f.endswith('.html'))
changed = 0
for fname in files:
    path = os.path.join(BASE, fname)
    c = open(path, 'rb').read().decode('utf-8')
    if OLD in c:
        open(path, 'wb').write(c.replace(OLD, NEW).encode('utf-8'))
        changed += 1
        print('OK ', fname)
    else:
        print('SKP', fname)
print('Done: %d/%d updated' % (changed, len(files)))
