import sys, os

path = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\SIC\WISMO\Chat_WISMO.html'
data = open(path, 'rb').read()
s = data.decode('utf-8')

changes = []

# 1. CSS warn/crit - remover
before = len(s)
s = s.replace('.htimer.warn{color:#fbbf24}\n', '')
s = s.replace('.htimer.crit{color:#f87171;animation:pulse .35s infinite alternate}\n', '')
changes.append('CSS warn/crit removed: ' + str(before - len(s)) + ' chars removed')

# 2. HUD initial value
c = s.count('>45<')
s = s.replace('<span class="htimer" id="htimer">45</span>', '<span class="htimer" id="htimer">00:00</span>', 1)
changes.append('HUD initial value: ' + str(c) + ' replaced')

# 3. Estado inicial
c = s.count('timer:null,timeLeft:45')
s = s.replace('timer:null,timeLeft:45', 'timer:null,timeLeft:0,elapsed:0', 1)
changes.append('state.elapsed added: ' + str(c))

# 4. Remove bonus por tempo
s = s.replace('var bonus=Math.floor(state.timeLeft/10);', 'var bonus=0;', 1)
s = s.replace('var bonus=Math.floor(state.timeLeft/15);', 'var bonus=0;', 1)
changes.append('bonus zeroed')

# 5. Simplificar labels de pontos (remover +bonus)
s = s.replace("fbTitle='BLURB EXCELENTE! +'+(Math.round(pct*10)+bonus)+' pts';",
              "fbTitle='BLURB EXCELENTE! +'+Math.round(pct*10)+' pts';", 1)
s = s.replace("fbTitle='BLURB PARCIAL \u2014 '+(Math.round(pct*8)+bonus)+' pts';",
              "fbTitle='BLURB PARCIAL \u2014 '+Math.round(pct*8)+' pts';", 1)
s = s.replace('addPts=Math.round(pct*10)+bonus;', 'addPts=Math.round(pct*10);', 1)
s = s.replace('addPts=Math.round(pct*8)+bonus;', 'addPts=Math.round(pct*8);', 1)
s = s.replace('addPts=Math.max(1,bonus);', 'addPts=1;', 1)
changes.append('pts labels simplified')

# 6. Substituir funcao startTimer
old_timer = (
    "function startTimer(seconds){\n"
    "  clearInterval(state.timer);state.timeLeft=seconds;\n"
    "  var el=document.getElementById('htimer');el.textContent=seconds;el.className='htimer';\n"
    "  state.timer=setInterval(function(){\n"
    "    state.timeLeft--;el.textContent=state.timeLeft;\n"
    "    var warn=state.phase===1?15:20;\n"
    "    var crit=state.phase===1?5:8;\n"
    "    if(state.timeLeft<=warn)el.className='htimer warn';\n"
    "    if(state.timeLeft<=crit)el.className='htimer crit';\n"
    "    if(state.timeLeft<=0){\n"
    "      clearInterval(state.timer);\n"
    "      if(!state.answered){\n"
    "        var txt=document.getElementById('chatinput').value.trim();\n"
    "        if(txt.length<5)document.getElementById('chatinput').value='[Tempo esgotado]';\n"
    "        submitResponse();\n"
    "      }\n"
    "    }\n"
    "  },1000);\n"
    "}"
)

new_timer = (
    "function startTimer(){\n"
    "  clearInterval(state.timer);\n"
    "  var el=document.getElementById('htimer');el.textContent='00:00';el.className='htimer';\n"
    "  state.timer=setInterval(function(){\n"
    "    state.elapsed++;\n"
    "    var m=Math.floor(state.elapsed/60);\n"
    "    var sec=state.elapsed%60;\n"
    "    el.textContent=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec;\n"
    "  },1000);\n"
    "}"
)

c = s.count(old_timer)
changes.append('startTimer old found: ' + str(c))
s = s.replace(old_timer, new_timer, 1)
changes.append('startTimer replaced: ' + str(new_timer[:30] in s))

# 7. Chamadas startTimer(45) -> startTimer()
s = s.replace('startTimer(45);', 'startTimer();', 1)
s = s.replace('startTimer(90);', 'startTimer();', 1)
changes.append('startTimer calls fixed')

# 8. Tela final: calcular tempo e mostrar
old_sfpts = "document.getElementById('sfpts').textContent=state.pts;"
new_sfpts = (
    "var totalSec=state.elapsed;"
    "var mm=Math.floor(totalSec/60);"
    "var ss=totalSec%60;"
    "var timeStr=(mm<10?'0':'')+mm+':'+(ss<10?'0':'')+ss;\n"
    "  document.getElementById('sfpts').textContent=state.pts;"
)
c = s.count(old_sfpts)
s = s.replace(old_sfpts, new_sfpts, 1)
changes.append('final screen time calc: found=' + str(c))

# 9. Linha de tempo na tela final (antes do sfnpt)
old_npt_div = '<div class="sf-npt" id="sfnpt"></div>'
new_npt_div = (
    '<div style="background:#082f49;border:1px solid #38bdf844;padding:10px 22px;'
    'border-radius:6px;margin-bottom:12px;font-size:.82rem;color:#7dd3fc;'
    'letter-spacing:1px;font-weight:700;display:flex;justify-content:center;gap:28px;">'
    '&#9201; TEMPO TOTAL: <span id="sftimer" style="color:#fff;font-size:1rem">--:--</span>'
    ' &nbsp;&nbsp; CCX M&eacute;dio: <span id="sfccx2" style="color:#fbbf24"></span>/5'
    '</div>\n'
    '<div class="sf-npt" id="sfnpt"></div>'
)
c = s.count(old_npt_div)
s = s.replace(old_npt_div, new_npt_div, 1)
changes.append('final screen timer row: found=' + str(c))

# 10. Atualizar sftimer e sfccx2 no JS
old_npt_js = "document.getElementById('sfnpt').textContent=npt;"
new_npt_js = (
    "document.getElementById('sfnpt').textContent=npt;\n"
    "  var timerEl=document.getElementById('sftimer');"
    "if(timerEl)timerEl.textContent=timeStr;\n"
    "  var ccx2El=document.getElementById('sfccx2');"
    "if(ccx2El)ccx2El.textContent=ccxAvg;"
)
c = s.count(old_npt_js)
s = s.replace(old_npt_js, new_npt_js, 1)
changes.append('sftimer JS update: found=' + str(c))

# Salvar
open(path, 'wb').write(s.encode('utf-8'))

log = path.replace('Chat_WISMO.html', 'patch_log.txt')
open(log, 'w').write('\n'.join(changes))
print('DONE ' + str(len(s)) + ' bytes')
for c in changes:
    print(c)
