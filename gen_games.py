
# -*- coding: utf-8 -*-
import os, json

BASE = r"C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME"
FOOTER = "Desenvolvido por Paulo Mateus Rebouças de Oliveira · 2026"

def team_html(title, subtitle, qjson, save_key, color="#6366f1", color2="#a5b4fc", emoji="⚡"):
    qcount = len(json.loads(qjson))
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Modo Equipe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0f172a;color:#e2e8f0;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px}}
.container{{width:100%;max-width:800px}}
.screen{{display:none}}.screen.active{{display:block}}
.start-card{{background:#1e293b;border:1px solid #334155;border-radius:18px;padding:36px 32px;text-align:center}}
.start-card h1{{font-size:1.8rem;font-weight:800;color:#e2e8f0;margin-bottom:8px}}
.start-card .sub{{color:#94a3b8;font-size:0.95rem;margin-bottom:18px;line-height:1.65}}
.mode-badge{{display:inline-flex;align-items:center;gap:8px;background:{color}22;border:1px solid {color}55;border-radius:20px;padding:8px 20px;color:{color2};font-size:0.88rem;font-weight:700;margin-bottom:18px}}
.stats-row{{display:flex;gap:12px;justify-content:center;margin-bottom:20px;flex-wrap:wrap}}
.stat-pill{{background:#0f172a;border:1px solid #334155;border-radius:10px;padding:8px 16px;font-size:0.85rem;color:#94a3b8}}
.stat-pill span{{color:#e2e8f0;font-weight:700}}
.team-setup-row{{display:flex;gap:8px;align-items:center;margin-bottom:8px}}
.team-input{{flex:1;background:#0f172a;border:1px solid #334155;border-radius:10px;padding:8px 12px;color:#e2e8f0;font-size:0.9rem}}
.remove-btn{{background:#ef444422;border:1px solid #ef444455;border-radius:8px;padding:6px 10px;color:#ef4444;cursor:pointer;font-size:0.8rem}}
.add-team-btn{{width:100%;background:#0f172a;border:2px dashed #334155;border-radius:12px;padding:10px;color:#64748b;font-size:0.85rem;cursor:pointer;margin-bottom:12px}}
.add-team-btn:hover{{border-color:{color};color:{color2}}}
.btn-start{{background:{color};color:#fff;border:none;border-radius:12px;padding:15px 40px;font-size:1.05rem;font-weight:700;cursor:pointer;width:100%;margin-bottom:10px}}
.btn-start:hover{{opacity:.9}}
.how-box{{background:#0f172a;border:1px solid #334155;border-radius:12px;padding:14px 18px;font-size:0.83rem;color:#94a3b8;line-height:1.65;text-align:left}}
.scoreboard{{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap}}
.team-score{{flex:1;min-width:130px;background:#1e293b;border:2px solid #334155;border-radius:14px;padding:12px;text-align:center;cursor:pointer;transition:all .2s;user-select:none}}
.team-score:hover{{border-color:{color}}}
.ts-name{{font-size:0.82rem;color:#94a3b8;font-weight:600;margin-bottom:4px}}
.ts-pts{{font-size:1.6rem;font-weight:800;color:{color2}}}
.topbar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}}
.topbar-title{{font-size:0.78rem;color:#64748b;font-weight:700;text-transform:uppercase;letter-spacing:.05em}}
.q-counter-pill{{background:#1e293b;border:1px solid #334155;border-radius:10px;padding:5px 12px;font-size:0.83rem;color:#94a3b8}}
.timer-wrap{{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:16px}}
.timer-circle{{width:70px;height:70px;border-radius:50%;background:#1e293b;border:4px solid {color};display:flex;align-items:center;justify-content:center;font-size:1.8rem;font-weight:800;color:{color2};transition:all .3s}}
.timer-circle.urgent{{border-color:#ef4444 !important;color:#ef4444 !important;animation:pulse .5s infinite}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.08)}}}}
.progress-wrap{{background:#1e293b;border-radius:8px;height:6px;margin-bottom:18px;overflow:hidden}}
.progress-bar{{background:{color};height:6px;border-radius:8px;transition:width .4s}}
.question-card{{background:#1e293b;border:1px solid #334155;border-radius:18px;padding:28px 24px}}
.q-tag{{display:inline-block;background:{color}22;color:{color2};border-radius:20px;padding:4px 14px;font-size:0.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:12px}}
.q-text{{font-size:1.08rem;color:#e2e8f0;font-weight:600;line-height:1.55;margin-bottom:22px}}
.options{{display:flex;flex-direction:column;gap:10px}}
.opt-btn{{background:#0f172a;border:2px solid #334155;border-radius:12px;padding:14px 18px;color:#cbd5e1;font-size:0.95rem;text-align:left;cursor:pointer;transition:all .18s;font-family:inherit}}
.opt-btn:hover:not(:disabled){{border-color:{color};color:#e2e8f0}}
.opt-btn.correct{{background:#10b98122;border-color:#10b981;color:#10b981;font-weight:700}}
.opt-btn.wrong{{background:#ef444422;border-color:#ef4444;color:#ef4444}}
.opt-btn.reveal{{background:#10b98111;border-color:#10b98166;color:#6ee7b7}}
.feedback{{margin-top:16px;background:#0f172a;border:1px solid #334155;border-radius:12px;padding:13px 15px;font-size:0.86rem;color:#94a3b8;line-height:1.6;display:none}}
.feedback.show{{display:block}}
.verdict{{font-weight:800;margin-bottom:5px;font-size:0.95rem}}
.verdict.ok{{color:#10b981}}.verdict.err{{color:#ef4444}}
.award-panel{{display:none;margin-top:14px;background:#0f172a;border:1px solid {color}55;border-radius:12px;padding:14px 16px}}
.award-panel.show{{display:block}}
.award-panel p{{font-size:0.85rem;color:#94a3b8;margin-bottom:10px}}
.award-btns{{display:flex;gap:8px;flex-wrap:wrap}}
.award-btn{{background:{color}22;border:1px solid {color}55;border-radius:10px;padding:8px 14px;color:{color2};font-size:0.83rem;font-weight:700;cursor:pointer}}
.award-btn:hover{{background:{color}44}}
.btn-next{{background:{color};color:#fff;border:none;border-radius:12px;padding:12px 28px;font-size:0.95rem;font-weight:700;cursor:pointer;margin-top:14px;display:none;width:100%}}
.btn-next:hover{{opacity:.9}}
.buzz-overlay{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:100;flex-direction:column;align-items:center;justify-content:center}}
.buzz-overlay.show{{display:flex}}
.buzz-card{{background:#1e293b;border:3px solid {color};border-radius:24px;padding:40px 48px;text-align:center;max-width:420px}}
.buzz-emoji{{font-size:4rem;margin-bottom:12px}}
.buzz-msg{{font-size:1.4rem;font-weight:800;color:#e2e8f0;margin-bottom:6px}}
.buzz-sub{{font-size:0.9rem;color:#94a3b8;margin-bottom:20px}}
.buzz-dismiss{{background:{color};color:#fff;border:none;border-radius:12px;padding:12px 28px;font-size:1rem;font-weight:700;cursor:pointer}}
.end-card{{background:#1e293b;border:1px solid #334155;border-radius:18px;padding:36px 32px;text-align:center}}
.winner-banner{{background:{color}22;border:2px solid {color}55;border-radius:14px;padding:20px;margin-bottom:20px}}
.w-label{{font-size:0.8rem;color:#94a3b8;font-weight:700;margin-bottom:6px;text-transform:uppercase}}
.w-name{{font-size:1.8rem;font-weight:800;color:{color2};margin-bottom:4px}}
.w-pts{{font-size:1rem;color:#64748b}}
.final-scores{{display:flex;flex-direction:column;gap:8px;margin-bottom:20px}}
.fsr{{display:flex;justify-content:space-between;align-items:center;background:#0f172a;border:1px solid #334155;border-radius:10px;padding:10px 16px}}
.fsr .fsn{{font-size:0.9rem;color:#e2e8f0;font-weight:600}}
.fsr .fsp{{font-size:1.1rem;font-weight:800;color:{color2}}}
.btn-reset{{background:#334155;color:#e2e8f0;border:none;border-radius:12px;padding:12px 28px;font-size:0.95rem;font-weight:700;cursor:pointer;width:100%}}
footer{{margin-top:20px;font-size:0.75rem;color:#475569;text-align:center}}
.ctrl-btn{{background:#1e293b;border:1px solid #334155;color:#e2e8f0;border-radius:12px;padding:10px 18px;font-size:0.88rem;font-weight:700;cursor:pointer}}
.ctrl-btn.primary{{background:{color};color:#fff;border:none}}
</style>
</head>
<body>
<div class="container">

<div class="screen active" id="startScreen">
  <div class="start-card">
    <div style="font-size:2.5rem;margin-bottom:10px">{emoji}</div>
    <h1>{title}</h1>
    <p class="sub">{subtitle}</p>
    <div class="mode-badge">🏆 Modo Equipe · Timer 5s · Pontos por time</div>
    <div class="stats-row">
      <div class="stat-pill">Perguntas: <span>{qcount}</span></div>
      <div class="stat-pill">Timer: <span>5s</span></div>
      <div class="stat-pill">Pontos: <span>10–15 pts</span></div>
    </div>
    <div style="margin-bottom:14px">
      <div style="font-size:0.85rem;color:#94a3b8;font-weight:600;margin-bottom:8px;text-align:left">Times:</div>
      <div id="teamSetup"></div>
      <button class="add-team-btn" onclick="addTeam()">+ Adicionar time</button>
    </div>
    <button class="btn-start" onclick="startGame()">▶ Iniciar Jogo</button>
    <div class="how-box"><b>Como jogar:</b> Mediador lê a pergunta em voz alta. Quem souber levanta a mão — mediador seleciona o time e clica no botão. Timer inicia (5s). Se errar, passa para outro time. Pontos acumulam por equipe!</div>
  </div>
</div>

<div class="screen" id="gameScreen">
  <div class="scoreboard" id="scoreboard"></div>
  <div class="topbar">
    <span class="topbar-title">{title.upper()[:40]}</span>
    <span class="q-counter-pill" id="qcp">Q 1/{qcount}</span>
  </div>
  <div class="progress-wrap"><div class="progress-bar" id="pb"></div></div>
  <div class="timer-wrap">
    <div>
      <div class="timer-circle" id="tc">5</div>
      <div style="font-size:0.7rem;color:#64748b;text-align:center;margin-top:3px">seg</div>
    </div>
    <button class="ctrl-btn primary" onclick="startTimer()">▶ Timer</button>
    <button class="ctrl-btn" onclick="triggerBuzz()">🔔 BUZZ!</button>
    <button class="ctrl-btn" onclick="skipQ()">⏭ Pular</button>
  </div>
  <div class="question-card">
    <div class="q-tag" id="qtag"></div>
    <div class="q-text" id="qtext"></div>
    <div class="options" id="opts"></div>
    <div class="feedback" id="fb"><div class="verdict" id="verd"></div><div id="expl"></div></div>
    <div class="award-panel" id="ap"><p>Atribuir ponto ao time que acertou:</p><div class="award-btns" id="abtns"></div></div>
    <button class="btn-next" id="nxt" onclick="nextQ()">Próxima →</button>
  </div>
</div>

<div class="buzz-overlay" id="bo">
  <div class="buzz-card">
    <div class="buzz-emoji">🔔</div>
    <div class="buzz-msg">BUZZ!</div>
    <div class="buzz-sub">Clique em OK, selecione o time que respondeu e clique na opção correta.</div>
    <button class="buzz-dismiss" onclick="document.getElementById('bo').classList.remove('show');startTimer()">OK, vamos lá!</button>
  </div>
</div>

<div class="screen" id="endScreen">
  <div class="end-card">
    <div style="font-size:3rem;margin-bottom:10px">🏆</div>
    <div style="font-size:1.5rem;font-weight:800;margin-bottom:16px">Fim de Jogo!</div>
    <div class="winner-banner">
      <div class="w-label">🥇 Vencedor</div>
      <div class="w-name" id="wn"></div>
      <div class="w-pts" id="wp"></div>
    </div>
    <div class="final-scores" id="fs"></div>
    <button class="btn-reset" onclick="resetGame()">🔄 Jogar Novamente</button>
  </div>
</div>

</div>
<footer>{FOOTER}</footer>

<script>
const Q = {qjson};
let teams=[{{name:'Time A',score:0}},{{name:'Time B',score:0}}];
let cur=0,ti=null,tv=5,answered=false;

function renderSetup(){{
  document.getElementById('teamSetup').innerHTML=teams.map((t,i)=>
    `<div class="team-setup-row"><input class="team-input" value="${{t.name}}" oninput="teams[${{i}}].name=this.value"><button class="remove-btn" onclick="removeTeam(${{i}})">✕</button></div>`
  ).join('');
}}
function addTeam(){{if(teams.length<6){{teams.push({{name:'Time '+(teams.length+1),score:0}});renderSetup();}}}}
function removeTeam(i){{if(teams.length>2){{teams.splice(i,1);renderSetup();}}}}

function renderSB(){{
  document.getElementById('scoreboard').innerHTML=teams.map((t,i)=>
    `<div class="team-score" id="ts${{i}}" onclick="selTeam(${{i}})"><div class="ts-name">${{t.name}}</div><div class="ts-pts">${{t.score}}<span style="font-size:.65rem;color:#64748b;font-weight:400"> pts</span></div></div>`
  ).join('');
}}
function selTeam(i){{
  document.querySelectorAll('.team-score').forEach((el,j)=>el.style.borderColor=j===i?'#10b981':'');
}}

function startGame(){{
  teams=teams.map(t=>Object.assign({{}},t,{{score:0}}));
  cur=0;answered=false;
  document.getElementById('startScreen').classList.remove('active');
  document.getElementById('gameScreen').classList.add('active');
  renderSB();renderQ();
}}

function renderQ(){{
  clearTi();answered=false;
  const q=Q[cur];
  document.getElementById('pb').style.width=((cur/Q.length)*100)+'%';
  document.getElementById('qcp').textContent='Q '+(cur+1)+'/'+Q.length;
  const tag=q.tag||(q.t?'PERGUNTA':'PERGUNTA');
  document.getElementById('qtag').textContent=tag+(q.trap?' 🎯':'');
  document.getElementById('qtext').textContent=q.text||q.t||'';
  const opts=q.options||q.opts||[];
  const ow=document.getElementById('opts');ow.innerHTML='';
  opts.forEach((o,i)=>{{const b=document.createElement('button');b.className='opt-btn';b.textContent=o;b.onclick=()=>ans(i);ow.appendChild(b);}});
  document.getElementById('fb').classList.remove('show');
  document.getElementById('nxt').style.display='none';
  document.getElementById('ap').classList.remove('show');
  tv=5;document.getElementById('tc').textContent='5';document.getElementById('tc').className='timer-circle';
}}

function startTimer(){{
  clearTi();tv=5;
  const c=document.getElementById('tc');c.className='timer-circle';
  ti=setInterval(()=>{{tv--;c.textContent=tv;if(tv<=2)c.className='timer-circle urgent';if(tv<=0){{clearTi();c.textContent='⏱';c.className='timer-circle urgent';}}}},1000);
}}
function clearTi(){{if(ti){{clearInterval(ti);ti=null;}}}}
function triggerBuzz(){{clearTi();document.getElementById('bo').classList.add('show');}}
function skipQ(){{cur++;if(cur>=Q.length)showEnd();else{{renderQ();}}}}

function ans(i){{
  if(answered)return;answered=true;clearTi();
  const q=Q[cur];const ci=q.correct!==undefined?q.correct:(q.c!==undefined?q.c:0);
  const ok=i===ci;
  const btns=document.querySelectorAll('.opt-btn');btns.forEach(b=>b.disabled=true);
  btns[i].classList.add(ok?'correct':'wrong');
  if(!ok)btns[ci].classList.add('reveal');
  document.getElementById('verd').className='verdict '+(ok?'ok':'err');
  document.getElementById('verd').textContent=ok?'✅ Correto!':'❌ Incorreto';
  document.getElementById('expl').textContent=q.explain||q.x||'';
  document.getElementById('fb').classList.add('show');
  if(ok){{document.getElementById('ap').classList.add('show');buildABtns(q.trap?15:10);}}
  document.getElementById('nxt').style.display='block';
}}
function buildABtns(pts){{
  document.getElementById('abtns').innerHTML=teams.map((t,i)=>
    `<button class="award-btn" onclick="award(${{i}},${{pts}})">${{t.name}}</button>`
  ).join('');
}}
function award(i,pts){{
  teams[i].score+=pts;renderSB();
  document.getElementById('ap').classList.remove('show');
  const n=document.createElement('div');n.style.cssText='color:#10b981;font-size:.82rem;font-weight:700;margin-top:6px';
  n.textContent='+'+pts+' pts → '+teams[i].name;
  document.getElementById('nxt').before(n);
}}
function nextQ(){{cur++;if(cur>=Q.length)showEnd();else renderQ();}}

function showEnd(){{
  document.getElementById('gameScreen').classList.remove('active');
  document.getElementById('endScreen').classList.add('active');
  const s=[...teams].sort((a,b)=>b.score-a.score);
  document.getElementById('wn').textContent=s[0].name;
  document.getElementById('wp').textContent=s[0].score+' pontos';
  document.getElementById('fs').innerHTML=s.map((t,i)=>`<div class="fsr"><span class="fsn">${{['🥇','🥈','🥉','4.','5.','6.'][i]||''}} ${{t.name}}</span><span class="fsp">${{t.score}} pts</span></div>`).join('');
}}
function resetGame(){{
  document.getElementById('endScreen').classList.remove('active');
  document.getElementById('startScreen').classList.add('active');
  teams=teams.map(t=>Object.assign({{}},t,{{score:0}}));
  cur=0;renderSetup();
}}

renderSetup();
</script>
</body>
</html>"""

# ================================================================
# GAME DEFINITIONS
# ================================================================
GAMES = [
  {
    "file":"Jogo_AHT_Time_Equipe.html","title":"Como Reduzir o AHT","emoji":"⚡",
    "sub":"Dicas práticas para atender mais rápido sem abrir mão da qualidade — Chat e Fone.",
    "key":"aht_equipe_v1","color":"#6366f1","color2":"#a5b4fc",
    "Q":[
      {"tag":"HISTÓRICO","text":"Ler o histórico antes de falar com o cliente é perda de tempo e aumenta o AHT.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Ler o histórico reduz AHT. 1 min de leitura economiza 5 de correção."},
      {"tag":"HISTÓRICO","text":"Em retomada, resumir o que foi tratado antes de fazer qualquer pergunta reduz o AHT.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Resumo rápido alinha em segundos, evita repetições."},
      {"tag":"ABERTURA","text":"Uma abertura enxuta no Chat — nome + disponibilidade em uma linha — é tão eficaz quanto uma longa.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Aberturas longas aumentam tempo ocioso."},
      {"tag":"ABERTURA","text":"No Fone, uma abertura padronizada longa não impacta o AHT.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! No Fone cada segundo conta. Abertura deve ser rápida e funcional."},
      {"tag":"DIAGNÓSTICO","text":"Confirmar produto e motivo do contato logo no início reduz o risco de investigar o caso errado.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! 10s de confirmação economizam minutos de retrabalho."},
      {"tag":"DIAGNÓSTICO","text":"Identificar todos os problemas do cliente antes de resolver o primeiro reduz o AHT total.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Tratamento em sequência evita interrupções no final."},
      {"tag":"VERIFICAÇÃO","text":"No Chat, verificar o caso enquanto o cliente digita é prática eficiente.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Verificação paralela é um dos maiores redutores de AHT."},
      {"tag":"VERIFICAÇÃO","text":"Enviar atualização ('ainda verificando, já volto!') durante verificação longa é desnecessário.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Sem atualização o chat fica inativo e é pausado — gerando novo AHT."},
      {"tag":"PAUSA","text":"Pausar o chat logo após receber o problema para 'pensar na solução' é recomendado.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pausa logo no início sem tentar verificar é tempo morto."},
      {"tag":"FONE","text":"Comunicar ao cliente antes do hold ('vou colocar em espera por alguns instantes') reduz o impacto negativo.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Clientes avisados antes do hold aceitam melhor a espera."},
      {"tag":"FONE","text":"Usar o tempo de hold para ter a resposta pronta ao retornar reduz o AHT total.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Retornar já com a informação pronta elimina mais uma rodada de 'vou verificar'."},
      {"tag":"EFICIÊNCIA","text":"Fazer perguntas cujas respostas já estão visíveis no sistema é prática eficiente para confirmar dados.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Perguntar o que já pode ver no sistema é tempo desperdiçado."},
      {"tag":"ENCERRAMENTO","text":"Encerrar sem perguntar se o cliente tem mais alguma dúvida é mais eficiente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Encerrar sem verificar pode gerar segundo contato — dois AHTs."},
      {"tag":"ENCERRAMENTO","text":"Um encerramento direto e específico — citando o que foi resolvido e o próximo passo — é mais eficiente que um genérico.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Encerramentos genéricos aumentam AHT sem agregar valor."},
      {"tag":"AUTONOMIA","text":"Conhecer bem os fluxos do AC3 e políticas de reembolso permite resolver mais contatos sem consultar outro setor.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Conhecimento técnico sólido é o maior redutor de AHT individual."},
      {"tag":"MINDSET","text":"AHT alto é sempre sinal de que o associate está tomando muito tempo — nunca que o caso era complexo.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Casos complexos têm AHT maior naturalmente. O foco é eliminar ineficiências."},
      {"tag":"MINDSET","text":"A melhor forma de reduzir o AHT é encerrar contatos mais rápido, mesmo sem resolver o problema.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Isso aumenta o AHT médio — gera callbacks."},
    ]
  },
  {
    "file":"Jogo_Transferencias_Equipe.html","title":"Transfere ou Não?","emoji":"🔀",
    "sub":"Regras oficiais de transferência — CAP, AMZL, contas, pausas e muito mais.",
    "key":"transf_equipe_v1","color":"#0ea5e9","color2":"#7dd3fc",
    "Q":[
      {"tag":"CAP","text":"Cliente pede reembolso, AC3 sugere CAP, mas a data TRACES ainda NÃO passou. Você transfere?","options":["Sim, transfiro","Não, sigo atendimento normal"],"correct":1,"trap":True,"explain":"❌ Pegadinha! TRACES vencido é condição obrigatória para CAP. Sem TRACES, não transfere."},
      {"tag":"CAP","text":"Reembolso já processado, mas cliente insiste em concessão extra. Você transfere para CAP?","options":["Sim, para reavaliar","Não — só informo o prazo de reembolso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Reembolso já processado: apenas informe prazo, sem transferência."},
      {"tag":"CAP","text":"Ao transferir para CAP, como você se refere à equipe com o cliente?","options":["'Equipe de Prevenção de Abuso de Concessões'","'Outra equipe que pode ajudar melhor'"],"correct":1,"trap":True,"explain":"❌ Pegadinha! NUNCA use o nome da equipe CAP com o cliente."},
      {"tag":"AMZL","text":"Motorista da AMZL bateu o carro do cliente durante a entrega. Transfere para SDS AMZL?","options":["Sim, transfiro","Não, resolvo direto"],"correct":0,"trap":False,"explain":"✅ Correto! Dano à propriedade do cliente causado pela entrega deve ir para AMZL/SDS."},
      {"tag":"AMZL","text":"Pacote atrasado em trânsito há 3 dias. Transferir para AMZL?","options":["Sim, transfiro","Não — trato como WISMO"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Atraso em trânsito NÃO é motivo de transferência para AMZL."},
      {"tag":"AMZL","text":"Item chegou danificado com defeito de fábrica. Transfere para AMZL/SDS?","options":["Sim","Não — fluxo Andon/Substituição"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Item com defeito NÃO é caso AMZL — é fluxo de Política do Andon."},
      {"tag":"AMZL","text":"Cliente alega que motorista roubou encomenda mas não tem provas. Ainda transfere?","options":["Sim — transfere COM OU SEM provas","Não — só com provas"],"correct":0,"trap":True,"explain":"✅ Correto! Alegação de roubo pelo motorista é transferida COM OU SEM provas."},
      {"tag":"CONTA","text":"Conta suspensa SEM nenhum SYSKA indicando transferência. Você transfere para Conta Suspensa?","options":["Sim, toda conta suspensa transfere","Não — só com SYSKA indicando"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Conta suspensa só é transferida quando há SYSKA explícito."},
      {"tag":"MÚSICA","text":"Cliente pergunta sobre Amazon Music Unlimited. Para onde vai?","options":["Transferência / Música digital","Transferência / Prime Video"],"correct":0,"trap":True,"explain":"✅ Correto! Amazon Music segue fluxo próprio de Música digital — diferente de Prime Video."},
      {"tag":"KDP","text":"Autor quer publicar livro IMPRESSO na Amazon.com.br. Você transfere para KDP?","options":["Sim, é sobre publicação","Não — KDP é só para Kindle/digital"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Livros impressos NÃO vão para KDP — use fluxo de Catálogo/Autores."},
      {"tag":"PAUSA","text":"Você pergunta 'Deu certo, chegou o e-mail?' e pausa o contato. É uma pausa válida?","options":["Sim — pergunta de ação válida","Não, nunca se pode pausar"],"correct":0,"trap":False,"explain":"✅ Correto! Perguntar se algo específico aconteceu é uma pergunta de ação válida."},
      {"tag":"PAUSA","text":"'Ajudo em algo mais?' + pausar o contato esperando resposta. É pausa válida?","options":["Sim, é pergunta de ação","Não — não é pergunta de ação"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Perguntas genéricas de encerramento NÃO são perguntas de ação."},
      {"tag":"CHAT","text":"Chat cai e você AINDA NÃO tinha permissão do cliente para alterar a conta. O que fazer?","options":["Alterar e encerrar o contato","Não alterar, follow-up por e-mail + ESTACIONAR"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Sem permissão: não altere a conta, envie e-mail e ESTACIONE — nunca encerre."},
      {"tag":"CHAT","text":"Cliente para de responder. Após quanto tempo você pode estacionar o chat?","options":["Imediatamente","Só após 3 min — com aviso após 2 min"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Chat inativo: avise após 2 min, estacione só após mais 1 min sem resposta."},
      {"tag":"CHAMADA","text":"Você pode simplesmente desligar na cara do cliente para agilizar o atendimento?","options":["Sim, se o atendimento foi resolvido","Não — pode gerar processo disciplinar"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Desconectar fora das situações previstas pode resultar em processo disciplinar."},
    ]
  },
  {
    "file":"Jogo_ClienteDificil_CDC_Equipe.html","title":"Cliente Difícil & CDC","emoji":"⚖️",
    "sub":"Como lidar com clientes que citam o CDC, ameaçam processar ou tentam pressionar por soluções fora da política.",
    "key":"cdc_equipe_v1","color":"#7c3aed","color2":"#c4b5fd",
    "Q":[
      {"tag":"AMEAÇA","text":"Cliente diz 'Vou processar a Amazon!' Qual a atitude correta?","options":["Oferecer reembolso em dobro para evitar processo","Reconhecer o direito e focar em resolver pela política","Discutir a lei com ele","Transferir para DART imediatamente"],"correct":1,"trap":False,"explain":"✅ Correto! Ameaça de processo não cria obrigação nova. Reconheça o direito e resolva pela política."},
      {"tag":"CDC ART 49","text":"Cliente cita Art. 49 dizendo que pode devolver quando quiser, sem prazo. Correto?","options":["Sim, o Art. 49 não tem prazo","Não — Art. 49 tem prazo de 7 dias corridos após recebimento","Sim, mas só para compras online","Não, Art. 49 é sobre outro assunto"],"correct":1,"trap":False,"explain":"✅ Correto! Direito de arrependimento = 7 dias corridos. Não é indefinido."},
      {"tag":"CDC ART 42","text":"Cliente diz 'Vocês têm que devolver em DOBRO, é o Art. 42!' Quando isso se aplica?","options":["Em qualquer devolução de produto","Sempre que o cliente pedir","Apenas quando há cobrança INDEVIDA comprovada","Nunca se aplica a e-commerce"],"correct":2,"trap":False,"explain":"✅ Correto! Art. 42 é só para cobrança indevida comprovada — não para qualquer devolução."},
      {"tag":"CDC GARANTIA","text":"Cliente afirma que o produto tem GARANTIA VITALÍCIA pelo CDC. É verdade?","options":["Sim, todo produto","Não — garantia legal tem prazo definido (30 ou 90 dias)","Sim, para eletrônicos","Depende do valor"],"correct":1,"trap":False,"explain":"✅ Correto! Mito comum. Garantia legal = 30 dias (não duráveis) ou 90 dias (duráveis). Não existe vitalícia no CDC."},
      {"tag":"AMEAÇA REDES","text":"Cliente ameaça 'Vou destruir a reputação de vocês nas redes sociais!' Como reagir?","options":["Ceder para evitar a exposição","Ameaçar de volta","Manter foco na resolução prática, sem debater a ameaça","Encerrar o chat imediatamente"],"correct":2,"trap":False,"explain":"✅ Correto! Ameaça de exposição pública é pressão emocional, não jurídica. Não cria obrigação nova."},
      {"tag":"MARKETPLACE","text":"Amazon tem responsabilidade sobre itens de vendedores parceiros (marketplace)?","options":["Não — somos só plataforma","Sim — Art. 34 CDC: responsabilidade solidária","Depende do valor","Só se o item for FBA"],"correct":1,"trap":True,"explain":"✅ Correto! Amazon tem responsabilidade solidária (Art. 34). NUNCA dizer 'somos só plataforma'."},
      {"tag":"REGRA DE OURO","text":"Qual é a REGRA DE OURO para qualquer situação de intimidação no atendimento?","options":["Sempre ceder para evitar conflito","Nunca prometer indenização, admitir culpa ou fornecer dados pessoais por pressão","Discutir a lei ponto a ponto","Encerrar sempre que houver ameaça"],"correct":1,"trap":False,"explain":"✅ Correto! A regra de ouro: resolver o problema real com calma, nunca ceder por medo."},
      {"tag":"NEGATIVAÇÃO","text":"Cliente foi negativado indevidamente por cobrança já paga e ameaça processar. Como agir?","options":["Dizer que não é problema da Amazon","Verificar com prioridade — se confirmado, corrigir rapidamente","Prometer indenização imediata","Ignorar e seguir o script"],"correct":1,"trap":False,"explain":"✅ Correto! Negativação indevida é situação grave e real. Verifique e corrija com urgência."},
      {"tag":"PROCON","text":"Cliente ameaça 'Vou denunciar ao Procon e Anatel!' Isso muda o andamento do caso?","options":["Sim — deve ser resolvido do jeito que o cliente quiser","Não — é direito do cidadão, não altera o mérito","Sim se for ao MP, não à Anatel","Não, mas precisa de pedido de desculpas formal"],"correct":1,"trap":False,"explain":"✅ Correto! Ameaça de canal externo não muda o mérito. O caso segue pela política vigente."},
      {"tag":"EQUIPARAÇÃO","text":"CDC obriga a Amazon a igualar o preço de um produto em loja concorrente?","options":["Sim, o CDC obriga","Não — CDC obriga cumprir a PRÓPRIA oferta, não igualar concorrentes","Sim se diferença > 20%","Depende da categoria"],"correct":1,"trap":False,"explain":"✅ Correto! Art. 30/35 obriga cumprir o que a empresa MESMA anunciou. Equiparação de concorrentes é política comercial, não lei."},
    ]
  },
  {
    "file":"Jogo_Encerramento_Equipe.html","title":"Operação Encerramento","emoji":"🔍",
    "sub":"Padrões de falha identificados nas auditorias W33–W35: encerramento, KYC, CDC, tom e muito mais.",
    "key":"encerr_equipe_v1","color":"#22d3ee","color2":"#67e8f9",
    "Q":[
      {"tag":"ENCERRAMENTO","text":"Encerrar sem confirmar resolução é aceitável quando a informação foi fornecida.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Gap #1 W33-W35: sempre confirmar resolução antes de encerrar."},
      {"tag":"ENCERRAMENTO","text":"Encerramento de qualidade = (1) confirmação de resolução + (2) próximo passo + (3) abertura para dúvidas.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Esses 3 elementos garantem que o cliente sai com clareza."},
      {"tag":"TOM","text":"Tom celebratório ao encerrar um contato onde o produto ainda não foi entregue é adequado.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Tom celebratório em problema não resolvido = desconexão crítica. Gap W35 Contato 25."},
      {"tag":"KYC","text":"Encerrar o contato assim que o KYC for enviado ao cliente é correto.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! KYC é só um passo. Após KYC, retorne ao problema original e resolva."},
      {"tag":"KYC BLOQUEADOR","text":"KYC pode ser usado para encerrar um contato sem resolver o problema do cliente.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! KYC como bloqueador é Gap #2 da equipe W33-W35."},
      {"tag":"CDC","text":"O CSA pode dizer que a Amazon 'não consegue intervir' em disputas com vendedores parceiros.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ GRAVE! Amazon tem responsabilidade solidária (CDC Art. 7). Nunca dizer 'somos só plataforma'."},
      {"tag":"PEDIR AVALIAÇÃO","text":"Dizer 'Vou pedir pra você dar uma olhadinha até o final' é solicitar avaliação indiretamente.","options":["Verdadeiro","Falso"],"correct":0,"trap":True,"explain":"✅ TRAP! Solicitação indireta é tão inadequada quanto a direta. Viola orientação do time."},
      {"tag":"RECONTATO","text":"Ler histórico de contatos anteriores antes de abordar o cliente em um recontato é opcional.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Ler histórico ANTES é obrigatório. Ignorar = descaso."},
      {"tag":"DIAGNÓSTICO","text":"O CSA pode processar o cancelamento sem confirmar o motivo com o cliente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Sempre confirmar o motivo antes de agir. Gap de diagnóstico W34."},
      {"tag":"SIC","text":"SIC deve ser preenchido no final do contato, após todas as ações concluídas.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! SIC no MOMENTO da identificação do motivo — antes de transferir, pausar ou encerrar."},
      {"tag":"CONTA BLOQUEADA","text":"Cliente recebeu SMS de tentativas excedidas no KYC. CSA deve continuar enviando links KYC padrão?","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Tentativas excedidas = estado diferente. Escalar via canal interno."},
      {"tag":"CUPOM","text":"Limite mínimo para cupons promocionais Amazon BR é atualmente R$40,00.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Atualizado para R$60,00 em 27/02/2026. R$40 não é mais vigente."},
      {"tag":"PLATAFORMA","text":"Para produtos de marketplace, a Amazon é apenas intermediária e pode redirecionar o cliente diretamente para o vendedor.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Amazon tem responsabilidade solidária (CDC Art. 7). Nunca redirecionar sem tentar resolver."},
      {"tag":"ABANDONO","text":"Um contato com 5+ transferências e sem demanda identificada deve ser tratado como contato novo.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Contato com múltiplas transferências sem demanda = abandono estrutural. CSA DEVE identificar a demanda."},
      {"tag":"ENCERRAMENTO PREMATURO","text":"Cliente não respondeu por 2 minutos. CSA pode encerrar o contato.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ TRAP! Silêncio não é confirmação. Sempre perguntar antes de encerrar."},
    ]
  },
  {
    "file":"Jogo_Pagamentos_Equipe.html","title":"Pagamentos CS BR","emoji":"💳",
    "sub":"Pagamentos é o motivo com MAIOR AHT do time (14,9 min). Domine os fluxos e reduza o tempo de atendimento.",
    "key":"pagamentos_equipe_v1","color":"#10b981","color2":"#6ee7b7",
    "Q":[
      {"tag":"CARTÃO RECUSADO","text":"Quando o cartão é recusado, a Amazon consegue ver o motivo exato da recusa.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! A recusa vem do banco emissor — a Amazon não tem acesso ao motivo específico."},
      {"tag":"REEMBOLSO","text":"O reembolso pode ser feito em um cartão DIFERENTE do usado na compra.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! O reembolso SEMPRE retorna ao mesmo método de pagamento original."},
      {"tag":"REEMBOLSO","text":"Cartão de crédito pode levar de 1 a 2 faturas para o reembolso aparecer.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Crédito: até 1-2 faturas (~10 dias úteis). Alinhar expectativa evita recontato."},
      {"tag":"REEMBOLSO PIX","text":"O reembolso via Pix pode ser feito para qualquer chave que o cliente informar.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pix só para chave vinculada ao CPF do TITULAR do pedido."},
      {"tag":"REEMBOLSO PIX","text":"O prazo do reembolso via Pix, após validação do CPF do titular, é de até 3 dias úteis.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Pix: até 3 dias úteis após validar CPF do titular."},
      {"tag":"VALE-PRESENTE","text":"O time CS BR pode vender vale-presente ao cliente durante o atendimento.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! CS BR NÃO vende vale-presente — apenas processa RESGATES e reembolso em vale-presente."},
      {"tag":"VALE-PRESENTE","text":"Reembolso em vale-presente Amazon fica disponível na conta do cliente em poucos minutos.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Reembolso em vale-presente é quase imediato — ótima alternativa."},
      {"tag":"COBRANÇA","text":"Uma cobrança de renovação automática (ex: Prime) contestada pelo cliente deve ser tratada sempre como fraude.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Antes de tratar como fraude, confirme se é RENOVAÇÃO AUTOMÁTICA."},
      {"tag":"PENDENTE","text":"Conta retida por pagamento pendente deve ser tratada como Conta Retida — Pagamento Pendente, não como abuso.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Pagamento pendente NÃO é abuso. Classificar certo evita transferência indevida."},
      {"tag":"DART/DUR","text":"Em dúvidas comuns de pagamento (cartão recusado, prazo de reembolso), o esperado é resolver sem acionar o DART.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Baixo DUR é POSITIVO. Contatos com DART levam ~2x mais tempo (18,6 vs 9,3 min)."},
      {"tag":"ESTORNO","text":"Conta retida por estorno/contestação (chargeback) segue o MESMO fluxo de conta retida por pagamento pendente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! São fluxos DISTINTOS. Encaminhe para a fila correta após confirmar o motivo."},
      {"tag":"CONFIRMAÇÃO","text":"Antes de executar um reembolso ou estorno, é boa prática confirmar a ação com o cliente em uma frase objetiva.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Confirmar antes de agir evita retrabalho e reclamação."},
    ]
  },
]

for g in GAMES:
    qjson = json.dumps(g["Q"], ensure_ascii=False)
    html = team_html(g["title"], g["sub"], qjson, g["key"], g["color"], g["color2"], g["emoji"])
    path = os.path.join(BASE, g["file"])
    with open(path, 'wb') as f:
        f.write(html.encode('utf-8'))
    print(f"OK {g['file']} ({len(html)//1024}KB)")

print("BATCH_1_DONE")
