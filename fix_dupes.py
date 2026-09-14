path = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\SIC\WISMO\Chat_WISMO.html'
s = open(path, 'rb').read().decode('utf-8')

# Fix 1: linha 1136/1137 - duplicata de var totalSec
dupe_calc = (
    "var totalSec=state.elapsed;var mm=Math.floor(totalSec/60);var ss=totalSec%60;"
    "var timeStr=(mm<10?'0':'')+mm+':'+(ss<10?'0':'')+ss;\n"
    "  var totalSec=state.elapsed;var mm=Math.floor(totalSec/60);var ss=totalSec%60;"
    "var timeStr=(mm<10?'0':'')+mm+':'+(ss<10?'0':'')+ss;"
)
single_calc = (
    "var totalSec=state.elapsed;var mm=Math.floor(totalSec/60);var ss=totalSec%60;"
    "var timeStr=(mm<10?'0':'')+mm+':'+(ss<10?'0':'')+ss;"
)
c = s.count(dupe_calc)
print('dupe_calc found:', c)
s = s.replace(dupe_calc, single_calc, 1)

# Fix 2: linhas 227/228 - duplicata do div sftimer no HTML
timer_div = (
    '  <div style="background:#082f49;border:1px solid #38bdf844;padding:10px 22px;'
    'border-radius:6px;margin-bottom:12px;font-size:.82rem;color:#7dd3fc;'
    'letter-spacing:1px;font-weight:700;display:flex;justify-content:center;gap:28px;">'
    '&#9201; TEMPO TOTAL: <span id="sftimer" style="color:#fff;font-size:1rem">--:--</span>'
    ' &nbsp;&nbsp; CCX M&eacute;dio: <span id="sfccx2" style="color:#fbbf24"></span>/5'
    '</div>\n'
    '<div style="background:#082f49;border:1px solid #38bdf844;padding:10px 22px;'
    'border-radius:6px;margin-bottom:12px;font-size:.82rem;color:#7dd3fc;'
    'letter-spacing:1px;font-weight:700;display:flex;justify-content:center;gap:28px;">'
    '&#9201; TEMPO TOTAL: <span id="sftimer" style="color:#fff;font-size:1rem">--:--</span>'
    ' &nbsp;&nbsp; CCX M&eacute;dio: <span id="sfccx2" style="color:#fbbf24"></span>/5'
    '</div>'
)
single_div = (
    '<div style="background:#082f49;border:1px solid #38bdf844;padding:10px 22px;'
    'border-radius:6px;margin-bottom:12px;font-size:.82rem;color:#7dd3fc;'
    'letter-spacing:1px;font-weight:700;display:flex;justify-content:center;gap:28px;">'
    '&#9201; TEMPO TOTAL: <span id="sftimer" style="color:#fff;font-size:1rem">--:--</span>'
    ' &nbsp;&nbsp; CCX M&eacute;dio: <span id="sfccx2" style="color:#fbbf24"></span>/5'
    '</div>'
)
c2 = s.count(timer_div)
print('dupe_div found:', c2)
s = s.replace(timer_div, single_div, 1)

# Fix 3: linhas 1143/1145 - duplicata de timerEl JS
dupe_timer_js = (
    "  var timerEl=document.getElementById('sftimer');if(timerEl)timerEl.textContent=timeStr;\n"
    "  var ccx2El=document.getElementById('sfccx2');if(ccx2El)ccx2El.textContent=ccxAvg;\n"
    "  var timerEl=document.getElementById('sftimer');if(timerEl)timerEl.textContent=timeStr;"
)
single_timer_js = (
    "  var timerEl=document.getElementById('sftimer');if(timerEl)timerEl.textContent=timeStr;\n"
    "  var ccx2El=document.getElementById('sfccx2');if(ccx2El)ccx2El.textContent=ccxAvg;"
)
c3 = s.count(dupe_timer_js)
print('dupe_timer_js found:', c3)
s = s.replace(dupe_timer_js, single_timer_js, 1)

open(path, 'wb').write(s.encode('utf-8'))
print('SAVED', len(s), 'bytes')
