
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

GAMES2 = [
  {
    "file":"Jogo_QualidadeCS_Equipe.html","title":"Quiz Qualidade CS","emoji":"🎯",
    "sub":"Baseado na auditoria real de 39 contatos — KYC, empatia, encerramento, handoff, resposta robótica e muito mais.",
    "key":"qualidade_equipe_v1","color":"#f59e0b","color2":"#fcd34d",
    "Q":[
      {"tag":"KYC","text":"Quando o link de KYC está com erro técnico, o associate deve pedir para o cliente tentar mais tarde e encerrar.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Problema técnico no KYC: escale internamente e ofereça alternativa antes de encerrar."},
      {"tag":"KYC","text":"Quando o cliente questiona 'na hora de comprar não pediram identidade, agora estão pedindo', o correto é explicar claramente o motivo (segurança/antifraude).","options":["Verdadeiro","Falso"],"correct":0,"trap":True,"explain":"✅ Correto! O papel do associate é explicar o PORQUÊ da política, não apenas repeti-la."},
      {"tag":"ENCERRAMENTO","text":"Um associate encerrou enquanto o cliente perguntava sobre a Ouvidoria. Isso está correto?","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! NUNCA encerrar com pedido de Ouvidoria, supervisor, ação em andamento ou dúvida aberta."},
      {"tag":"ENCERRAMENTO","text":"A pergunta correta antes de encerrar deve ser explícita, tipo 'Posso encerrar nosso atendimento?', aguardando confirmação.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Regra inviolável: nunca encerrar sem confirmação explícita do cliente."},
      {"tag":"EMPATIA","text":"Uma cliente relatou que o produto era para uma pessoa que faleceu. O correto é seguir o fluxo técnico padrão sem alterar o tom.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Antes de qualquer resolução técnica, reconheça e valide a dimensão emocional."},
      {"tag":"EMPATIA","text":"Frases genéricas como 'sinto muito pela situação' já são suficientes para demonstrar empatia real.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Empatia real menciona o produto/situação específica do cliente."},
      {"tag":"ROBÓTICO","text":"Um Nintendo Switch 2 sem envio há 2 meses — a única resposta é cancelamento, sem mais opções.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Antes de cancelamento, verifique disponibilidade, escale ou ofereça compensação."},
      {"tag":"ROBÓTICO","text":"A postura ideal é 'resolvo, não informo': buscar ativamente uma alternativa antes de devolver o problema ao cliente.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Quando o script não resolve, o papel é buscar uma saída — não só comunicar a limitação."},
      {"tag":"HANDOFF","text":"Quando um contato passa por um segundo associate, o mais profissional é iniciar com saudação padrão ('Olá! Como posso ajudar?').","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Em contato já em andamento, saudação genérica faz o cliente repetir tudo."},
      {"tag":"HANDOFF","text":"Template de retomada recomendado: '[Nome], vi que você estava com [X]. Vou continuar a partir daqui.'","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Demonstra que o histórico foi lido — cliente não precisa re-explicar nada."},
      {"tag":"CONHECIMENTO","text":"Vale-presente de reembolso existe e é processado, mas a Amazon BR CS não vende mais vale-presente como produto.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! CS processa redenções e reembolso-em-vale-presente — não vende o produto."},
      {"tag":"AUTORIZACAO","text":"Um associate pode iniciar uma devolução diretamente, já que devolução é o caminho mais comum nesses casos.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Sempre confirmar a resolução desejada com o cliente antes de qualquer ação irreversível."},
      {"tag":"CUPONS","text":"Um cliente relata que o cupom não foi aplicado no checkout. O correto é negar diretamente, pois cupons têm regras fixas.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! O associate deve verificar o histórico e as condições de elegibilidade ANTES de responder."},
      {"tag":"CUPONS","text":"Negar cupons sem investigação adequada cria risco de 'percepção de propaganda enganosa', com alto risco de chargeback e PROCON.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Texto literal do Gap #8 do relatório de auditoria."},
    ]
  },
  {
    "file":"Jogo_casuisab_Equipe.html","title":"Encerramento & Múltiplos Problemas","emoji":"🎯",
    "sub":"Revisa como fechar contatos com qualidade, organizar casos com vários pedidos e transformar situações difíceis em experiências positivas.",
    "key":"casuisab_equipe_v1","color":"#8b5cf6","color2":"#c4b5fd",
    "Q":[
      {"tag":"ENCERRAMENTO","text":"Usar o mesmo blurb genérico de encerramento em todos os contatos difíceis é sinal de profissionalismo.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Blurbs genéricos são percebidos como copy-paste automático."},
      {"tag":"ENCERRAMENTO","text":"Um bom encerramento deve incluir: (1) confirmação de resolução, (2) próximo passo, (3) abertura para dúvidas.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Esses 3 elementos garantem que o cliente sai com clareza."},
      {"tag":"ENCERRAMENTO","text":"Quando o problema não pôde ser resolvido completamente, o encerramento deve incluir uma âncora clara de próximo passo.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! A âncora de próximo passo cria compromisso e reduz incerteza."},
      {"tag":"MULTI-PROBLEMA","text":"Criar um mini-resumo no início de contato com múltiplos pedidos é considerado boa prática.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! O mini-resumo alinha expectativas e evita retrabalho."},
      {"tag":"MULTI-PROBLEMA","text":"Em contatos com múltiplos pedidos, confirmar o nome do produto antes de executar qualquer ação aumenta desnecessariamente o AHT.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Confirmar o produto reduz AHT — evita ação no pedido errado."},
      {"tag":"EQUIPARAÇÃO","text":"Após emitir um vale-presente para equiparação, você pode encerrar sem verificar se o cliente recebeu o crédito.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Sempre confirme: 'Consegue verificar no app se o vale já aparece?' Isso fecha o ciclo."},
      {"tag":"FEEDBACK CLIENTE","text":"Quando o cliente diz que vai parar de comprar na Amazon, o correto é reconhecer a frustração, registrar formalmente e oferecer uma âncora.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Churn declarado é sinal de alerta máximo — reconheça, registre e ofereça âncora."},
      {"tag":"TRANSPORTADORA","text":"Dizer 'não tenho como contatar a transportadora' + 'só aguardar' é uma resposta completa para pedido atrasado.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Sempre explore o sistema antes de concluir que não há o que fazer."},
      {"tag":"EMPATIA","text":"Empatia genérica ('Lamento pelo transtorno') tem o mesmo impacto de empatia específica na percepção do cliente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Empatia específica menciona produto, situação real e impacto para o cliente."},
      {"tag":"QUALIDADE CCX","text":"As dimensões CCX avaliadas pelos clientes incluem: Conhecimento, Eficiência, Prestatividade, Empatia, Cortesia e Clareza.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Essas são as 6 dimensões do CCX."},
      {"tag":"QUALIDADE CCX","text":"Um contato resolvido tecnicamente mas onde o cliente não entendeu o que foi feito sempre receberá avaliação positiva.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Clareza é uma das 6 dimensões do CCX. Se o cliente não entendeu, avaliará negativamente."},
      {"tag":"CHECK ORDER","text":"Verificar as atualizações de rastreio antes de informar o cliente sobre o status do pedido é passo obrigatório.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Nunca informe um status sem verificar o rastreio atualizado no sistema."},
    ]
  },
  {
    "file":"Jogo_ejoseago_Equipe.html","title":"Retomada & Resolução","emoji":"🔄",
    "sub":"Pausas, retomada de chat, pagamentos complexos e encerramento com qualidade — situações reais do dia a dia.",
    "key":"ejoseago_equipe_v1","color":"#06b6d4","color2":"#67e8f9",
    "Q":[
      {"tag":"RETOMADA","text":"Ao pegar um chat pausado, a primeira coisa a fazer é perguntar ao cliente qual é o problema.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Primeiro leia TODO o histórico. Retomada ideal: 'Vi que você tem [problema X], vou continuar de onde paramos.'"},
      {"tag":"RETOMADA","text":"Durante verificação longa, enviar atualizações intermediárias a cada 2 minutos reduz a chance de o chat ser pausado por inatividade.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! O chat é pausado após 2 min sem interação. Atualização rápida mantém o cliente presente."},
      {"tag":"PAGAMENTO","text":"Se o sistema mostra que o cupom foi aplicado, você pode encerrar, mesmo que o cliente apresente prints com valor diferente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! O sistema é uma ferramenta, não o árbitro final. Analise as evidências do cliente."},
      {"tag":"ENCERRAMENTO","text":"Encerrar com 'bom dia' e 'já fiz o que pude' quando o cliente pediu supervisor é prática aceitável.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pedido de supervisão deve ser registrado formalmente — nunca encerrar unilateralmente."},
      {"tag":"PROMISES","text":"Se atendimento anterior prometeu equiparação de preço e o cliente retorna para executar, isso deve ser prioridade máxima.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Trair uma promessa gera BTB negativo quase certo."},
      {"tag":"MULTI-PROBLEMA","text":"Quando o cliente tem dois problemas simultâneos, resolva um, encerre, e ele contacta novamente para o segundo.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Identifique todos os problemas no início e trate em sequência dentro do mesmo contato."},
      {"tag":"PARKED","text":"Um cliente diz 'já é o terceiro atendente' — isso requer reconhecimento imediato antes de qualquer ação.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Quando o cliente menciona número de atendentes, ele está comunicando desgaste."},
      {"tag":"PARKED","text":"Se um contato passou por 3+ associates diferentes, o próximo deve perguntar 'qual é o problema?' para garantir entendimento.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pedir para o cliente re-explicar após 3 atendimentos é extremamente frustrante."},
      {"tag":"ESCALADA","text":"Se o cliente pede supervisor e você acha que a resposta será a mesma, pode informar isso e negar a escalada.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! O cliente tem direito a solicitar escalada. Registre formalmente e siga o processo correto."},
      {"tag":"CHECK ORDER","text":"Quando nenhuma ação imediata está disponível para pedido atrasado, oferecer uma âncora de próximo passo é prática recomendada.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! A âncora cria compromisso — o cliente sabe o que vai acontecer e quando retornar."},
      {"tag":"QUALIDADE","text":"Usar o mesmo blurb de empatia genérico em todos os contatos difíceis é suficiente para boas notas em Empatia no CCX.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Empatia genérica é percebida como automática. Empatia de qualidade é específica."},
      {"tag":"QUALIDADE","text":"Um contato de qualidade pode ser encerrado sem o problema resolvido, desde que o associate demonstrou empatia.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Empatia é necessária mas não suficiente. O mínimo: próximo passo + cliente ciente + canal de retorno."},
    ]
  },
  {
    "file":"Jogo_msoarfra_Equipe.html","title":"Pagamento Complexo & Resolução","emoji":"💰",
    "sub":"Cupons, equiparações, pedidos cancelados e situações de alto valor — onde organizar o raciocínio faz toda a diferença.",
    "key":"msoarfra_equipe_v1","color":"#f97316","color2":"#fdba74",
    "Q":[
      {"tag":"CUPOM","text":"Quando cliente reclama de valor diferente com cupom, a primeira ação é verificar no sistema se o cupom foi aplicado.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Primeiro confirme com o cliente o que ele entendeu sobre o cupom. O sistema pode mostrar 'aplicado' por um motivo diferente do problema real."},
      {"tag":"CUPOM","text":"Um cupom de 'R$25 em compras acima de R$100' pode ser dividido automaticamente entre dois produtos de um mesmo pedido.","options":["Verdadeiro","Falso"],"correct":0,"trap":True,"explain":"✅ Correto! O sistema pode dividir o desconto proporcionalmente entre os itens."},
      {"tag":"LINKS","text":"Enviar um link para o cliente sem verificar se está funcionando é prática aceitável para agilizar o atendimento.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Um link quebrado em momento tenso deteriora imediatamente a confiança do cliente."},
      {"tag":"ÂNCORA","text":"Quando nenhuma solução imediata está disponível em caso de alto valor, encerrar informando o motivo sem oferecer próximo passo é suficiente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Em casos de alto valor, sempre ofereça âncora de próximo passo."},
      {"tag":"ÂNCORA","text":"Em caso com múltiplas unidades canceladas, não conseguir a solução completa significa que o associate não pode oferecer nada.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Sempre há pelo menos um gesto possível antes de encerrar sem nada."},
      {"tag":"CHURN","text":"Quando cliente diz que será sua última compra, o associate deve apenas encerrar educadamente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Churn declarado exige: (1) empatia específica, (2) registro interno, (3) comunicar ao cliente, (4) oferecer âncora."},
      {"tag":"CHURN","text":"Registrar a insatisfação E comunicar ao cliente que fez isso tem mais impacto do que apenas registrar silenciosamente.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! O cliente não sabe o que acontece 'por dentro'. Comunicar a ação demonstra que a Amazon age."},
      {"tag":"PAGAMENTO","text":"Ao processar equiparação via vale-presente, o associate deve informar o prazo de chegada do vale E como aplicar no checkout.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Vale sem instrução de uso gera novo contato de dúvida."},
      {"tag":"CHECK ORDER","text":"Para pedido em trânsito sem atualização de data, 'aguardar até o prazo final' é a única opção disponível.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Verifique: nota à transportadora? chamado interno de logística? cliente prefere cancelar?"},
      {"tag":"CHECK ORDER","text":"Informar o prazo final sem âncora ('você tem até dia X') é uma resposta completa para pedido atrasado.","options":["Verdadeiro","Falso"],"correct":1,"trap":False,"explain":"❌ Errado! Complete com: o que acontece se não chegar, como retornar, registro comunicado ao cliente."},
      {"tag":"EMPATIA","text":"Reconhecer a emoção do cliente ANTES de explicar a política aumenta a receptividade às informações.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Quando o cliente está frustrado, o cérebro prioriza a emoção. Reconheça primeiro, explique depois."},
      {"tag":"QUALIDADE","text":"Um pedido de alto valor (acima de R$500) cancelado sem culpa do cliente deve ter nível de atenção igual a qualquer outro.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pedidos de alto valor requerem atenção redobrada — risco de BTB, Procon e churn é muito maior."},
    ]
  },
  {
    "file":"Jogo_QuizDART_Equipe.html","title":"Quiz DART — Transfere ou Resolve?","emoji":"🎯",
    "sub":"DART: quando escalar, quando resolver na fila. Cada contato com DART leva ~2x mais tempo (18,6 vs 9,3 min).",
    "key":"dart_equipe_v1","color":"#ef4444","color2":"#fca5a5",
    "Q":[
      {"tag":"DART","text":"Em dúvidas comuns de pagamento (cartão recusado, prazo de reembolso), o esperado é resolver com autonomia, sem acionar o DART.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Baixo DUR é POSITIVO. DART duplica o tempo de handle (18,6 vs 9,3 min)."},
      {"tag":"DART","text":"Quando você tem dúvida sobre uma ação, escalar imediatamente é sempre a opção mais segura.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Antes de escalar, verifique no CS Assistant ou fluxo AC3. A maioria das dúvidas tem resposta no sistema."},
      {"tag":"DART","text":"Conhecer bem os fluxos do AC3 e políticas de reembolso permite resolver mais contatos sem DART.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Conhecimento técnico sólido é o maior redutor de DUR individual."},
      {"tag":"DART","text":"Escalar para outro setor situações que você já tem autorização para resolver aumenta o AHT sem necessidade.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! Escaladas desnecessárias adicionam tempo de espera e risco de perda de contato."},
      {"tag":"CAP","text":"Cliente pede reembolso, AC3 sugere CAP, mas a data TRACES ainda NÃO passou. Você transfere?","options":["Sim, o sistema sugeriu","Não — TRACES vencido é condição obrigatória"],"correct":1,"trap":True,"explain":"❌ Pegadinha! TRACES vencido é condição obrigatória para CAP. Sistema sugerindo não é suficiente."},
      {"tag":"AMZL","text":"Item chegou danificado com defeito de fábrica. Caso de transferência para AMZL/SDS?","options":["Sim, transfiro","Não — fluxo de Política do Andon"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Item com defeito NÃO é caso AMZL — é fluxo de Política do Andon."},
      {"tag":"AMZL","text":"Motorista da AMZL bateu o carro do cliente durante entrega. Caso de transferência para SDS AMZL?","options":["Sim, transfiro","Não, resolvo direto"],"correct":0,"trap":False,"explain":"✅ Correto! Dano à propriedade causado pela entrega DEVE ir para AMZL/SDS."},
      {"tag":"DUR","text":"Um contato com DART leva em média 18,6 min, enquanto sem DART leva 9,3 min — diferença de aproximadamente o dobro.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! DART duplica o handle time. Usar DART quando não necessário impacta diretamente o AHT."},
      {"tag":"DART","text":"Se o cliente cita CDC Art. 35 e você não sabe a resposta exata, o correto é escalar para DART imediatamente.","options":["Verdadeiro","Falso"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Pesquise no CS Assistant primeiro. A maioria das dúvidas tem resposta no sistema antes de precisar do DART."},
      {"tag":"QLA","text":"Anotação no pedido indica 'exceeding QL'. O encaminhamento correto é transferir para CAP.","options":["Sim, CAP é o destino correto","Não — QLA é fluxo próprio: e-mail para qla@amazon.com.br"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Limite de compra excedido (QLA) tem fluxo próprio separado da CAP."},
      {"tag":"CONTA","text":"Conta suspensa SEM SYSKA indicando transferência — você transfere para Conta Suspensa?","options":["Sim, toda conta suspensa transfere","Não — só transfere COM SYSKA indicando"],"correct":1,"trap":True,"explain":"❌ Pegadinha! Conta suspensa só é transferida quando há SYSKA explícito."},
      {"tag":"DART","text":"Contatos sobre pedidos/contas com anotações recentes de ECR seguem o fluxo dedicado de Transferir/ECR.","options":["Verdadeiro","Falso"],"correct":0,"trap":False,"explain":"✅ Correto! ECR tem fluxo dedicado — não siga o fluxo padrão."},
    ]
  },
]

for g in GAMES2:
    qjson = json.dumps(g["Q"], ensure_ascii=False)
    html = team_html(g["title"], g["sub"], qjson, g["key"], g["color"], g["color2"], g["emoji"])
    path = os.path.join(BASE, g["file"])
    with open(path, 'wb') as f:
        f.write(html.encode('utf-8'))
    print(f"OK {g['file']} ({len(html)//1024}KB)")

print("BATCH_2_DONE")
