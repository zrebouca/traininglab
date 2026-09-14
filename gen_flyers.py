
# -*- coding: utf-8 -*-
import os

BASE = r"C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME"
FOOTER = "Desenvolvido por Paulo Mateus Rebouças de Oliveira · 2026"

def flyer(title, subtitle, emoji, desc, topics, tips, color, color2, game_file):
    topics_html = ''.join(f'<li>{t}</li>' for t in topics)
    tips_html = ''.join(f'<div class="tip"><span class="tip-icon">💡</span><span>{t}</span></div>' for t in tips)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flyer — {title}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#f1f5f9;font-family:'Inter',system-ui,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px}}
.card{{background:#fff;border-radius:24px;max-width:600px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.12);overflow:hidden}}
.header{{background:linear-gradient(135deg,{color},{color2});padding:40px 36px 32px;color:#fff;text-align:center;position:relative}}
.header-emoji{{font-size:3.5rem;margin-bottom:12px;display:block}}
.header h1{{font-size:1.9rem;font-weight:900;margin-bottom:6px;line-height:1.2}}
.header .sub{{font-size:0.95rem;opacity:.88;line-height:1.55}}
.badge{{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.22);border:1px solid rgba(255,255,255,.4);border-radius:20px;padding:6px 16px;font-size:0.78rem;font-weight:700;margin-top:14px}}
.body{{padding:32px 36px}}
.desc{{font-size:0.95rem;color:#475569;line-height:1.7;margin-bottom:24px}}
.section-title{{font-size:0.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:{color};margin-bottom:12px}}
.topics{{list-style:none;display:flex;flex-direction:column;gap:8px;margin-bottom:24px}}
.topics li{{display:flex;align-items:center;gap:10px;background:#f8fafc;border-left:3px solid {color};border-radius:0 10px 10px 0;padding:10px 14px;font-size:0.9rem;color:#334155;font-weight:500}}
.topics li::before{{content:'✓';color:{color};font-weight:800;font-size:0.85rem;flex-shrink:0}}
.tips{{display:flex;flex-direction:column;gap:10px;margin-bottom:24px}}
.tip{{display:flex;align-items:flex-start;gap:10px;background:linear-gradient(135deg,{color}0d,{color}06);border:1px solid {color}22;border-radius:12px;padding:12px 14px}}
.tip-icon{{font-size:1.1rem;flex-shrink:0;margin-top:1px}}
.tip span:last-child{{font-size:0.88rem;color:#475569;line-height:1.6}}
.cta{{background:linear-gradient(135deg,{color},{color2});border-radius:16px;padding:20px 24px;color:#fff;display:flex;align-items:center;justify-content:space-between;gap:16px}}
.cta-text{{font-size:0.9rem;line-height:1.5}}
.cta-text b{{font-size:1rem}}
.cta-badge{{background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.4);border-radius:12px;padding:10px 16px;font-size:0.85rem;font-weight:700;white-space:nowrap;text-align:center}}
.divider{{height:1px;background:#e2e8f0;margin:24px 0}}
footer{{font-size:0.72rem;color:#94a3b8;text-align:center;padding:0 36px 24px}}
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <span class="header-emoji">{emoji}</span>
    <h1>{title}</h1>
    <div class="sub">{subtitle}</div>
    <div class="badge">🏆 Modo Equipe · Timer 5s · CS BR</div>
  </div>
  <div class="body">
    <p class="desc">{desc}</p>
    <div class="section-title">📋 Temas cobertos</div>
    <ul class="topics">{topics_html}</ul>
    <div class="section-title">🔑 Pontos-chave</div>
    <div class="tips">{tips_html}</div>
    <div class="divider"></div>
    <div class="cta">
      <div class="cta-text">
        <b>Pronto para jogar?</b><br>
        Abra o arquivo <code style="background:rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:0.82rem">{game_file}</code> no navegador.
      </div>
      <div class="cta-badge">🎮<br>Jogar<br>Agora</div>
    </div>
  </div>
  <footer>{FOOTER}</footer>
</div>
</body>
</html>"""

FLYERS = [
  {
    "file":"Flyer_AHT.html","game":"Jogo_AHT_Time_Equipe.html",
    "title":"Como Reduzir o AHT","subtitle":"Chat & Fone — Dicas práticas de eficiência",
    "emoji":"⚡","color":"#6366f1","color2":"#818cf8",
    "desc":"O AHT (Average Handle Time) é um dos KPIs mais impactantes do atendimento. Este jogo cobre os principais hábitos que reduzem o tempo de contato sem comprometer a qualidade — válidos para Chat MU e Fone.",
    "topics":["Leitura e uso do histórico de contatos","Abertura enxuta e eficiente","Diagnóstico correto antes de agir","Verificação paralela no Chat","Uso adequado de pausa e hold no Fone","Encerramento direto e específico","Autonomia: quando resolver vs. escalar"],
    "tips":["Ler o histórico economiza 5 min de retrabalho","No Chat: verificar enquanto o cliente digita","Hold com aviso = cliente mais paciente","Encerramento genérico aumenta AHT, não reduz"],
  },
  {
    "file":"Flyer_Transferencias.html","game":"Jogo_Transferencias_Equipe.html",
    "title":"Transfere ou Não?","subtitle":"Regras oficiais de transferência CS BR 2026",
    "emoji":"🔀","color":"#0ea5e9","color2":"#38bdf8",
    "desc":"103 transferências registradas em W29 — 36,9% para Abuse Prevention e 14,6% para AMZL. Muitas poderiam ser evitadas. Este jogo cobre as regras atualizadas de CAP, AMZL, pausas, contas e muito mais.",
    "topics":["CAP: 3 condições obrigatórias + TRACES","AMZL: casos válidos vs. inválidos","Conta Suspensa + SYSKA","Limites de compra (QLA)","Dispositivos: Alexa, Fire TV, Kindle, Music","Pausa válida: critério de 'pergunta de ação'","Chat abandonado e inatividade"],
    "tips":["TRACES vencido é condição obrigatória para CAP","Dano à propriedade = AMZL; defeito de fábrica = Andon","Conta suspensa só transfere COM SYSKA","'Ajudo em algo mais?' + pausar NÃO é pausa válida"],
  },
  {
    "file":"Flyer_ClienteDificil_CDC.html","game":"Jogo_ClienteDificil_CDC_Equipe.html",
    "title":"Cliente Difícil & CDC","subtitle":"Intimidação, ameaças e artigos do Código de Defesa do Consumidor",
    "emoji":"⚖️","color":"#7c3aed","color2":"#a78bfa",
    "desc":"Clientes que citam o CDC, ameaçam processar ou tentam pressionar por soluções fora da política são uma realidade diária. Este jogo treina como responder com segurança, empatia e sem ceder indevidamente.",
    "topics":["Ameaças de processo e Procon","Art. 49 — direito de arrependimento (7 dias)","Art. 42 — cobrança indevida em dobro","Garantia legal (30/90 dias) vs. contratual","Responsabilidade solidária (Art. 34) no marketplace","Negativação indevida (Art. 43)","Regra de Ouro do atendimento CDC"],
    "tips":["Ameaça de processo não cria obrigação nova","Art. 42 (dobro) só vale para cobrança INDEVIDA","Nunca dizer 'somos só plataforma'","Empatia + resolução pela política = resposta correta"],
  },
  {
    "file":"Flyer_Encerramento.html","game":"Jogo_Encerramento_Equipe.html",
    "title":"Operação Encerramento","subtitle":"Gaps sistêmicos das auditorias W33, W34 e W35",
    "emoji":"🔍","color":"#22d3ee","color2":"#67e8f9",
    "desc":"As auditorias W33–W35 confirmaram padrões sistêmicos de falha no encerramento. Este jogo cobre os 8 principais gaps identificados — do encerramento prematuro ao KYC como bloqueador.",
    "topics":["Encerramento com confirmação de resolução","Tom calibrado ao estado da resolução","KYC como bloqueador (Gap #2)","KYC tentativas excedidas — estado diferente","Pedir avaliação (direto e indireto)","Abandono estrutural (5+ transferências)","CDC Art. 7 — responsabilidade solidária","Atualização de cupons: R$60 (não R$40)"],
    "tips":["Nunca encerrar sem: confirmação + próximo passo + abertura","Tom celebratório em problema não resolvido = gap crítico","SIC: preencher NO MOMENTO da identificação","Tentativas excedidas no KYC: escalar, não reenviar link"],
  },
  {
    "file":"Flyer_Pagamentos.html","game":"Jogo_Pagamentos_Equipe.html",
    "title":"Pagamentos CS BR","subtitle":"O motivo com MAIOR AHT do time — 14,9 minutos",
    "emoji":"💳","color":"#10b981","color2":"#34d399",
    "desc":"Pagamentos é o SIC com mais alto AHT médio (14,9 min). Dominar esses fluxos derruba o tempo de atendimento e melhora o DUR. Cada pergunta é um cenário real do dia a dia.",
    "topics":["Cartão recusado: papel do banco vs. Amazon","Reembolso: método original obrigatório","Reembolso Pix: CPF do titular, até 3 dias úteis","Reembolso cartão: 1–2 faturas (~10 dias úteis)","Vale-presente: CS BR não VENDE, só processa","Conta Retida: Pagamento Pendente vs. Chargeback","Compra não reconhecida: segurança da conta","DART/DUR: quando resolver na fila vs. escalar"],
    "tips":["Pix de reembolso: sempre para chave do CPF titular","Reembolso em vale-presente: quase imediato","Banco emissor define parcelamento — não a Amazon","DART duplica o handle time (18,6 vs 9,3 min)"],
  },
  {
    "file":"Flyer_QualidadeCS.html","game":"Jogo_QualidadeCS_Equipe.html",
    "title":"Quiz Qualidade CS","subtitle":"Baseado na auditoria real de 39 contatos — Julho 2026",
    "emoji":"🎯","color":"#f59e0b","color2":"#fcd34d",
    "desc":"Este quiz é um diagnóstico baseado em casos reais auditados em Jul/2026. Cobre os 8 gaps mais frequentes: KYC, encerramento sem confirmação, empatia, resposta robótica, handoff, autorização, conhecimento de produto e cupons.",
    "topics":["KYC: comunicação clara + alternativa quando falha","Encerramento: 5 situações onde NUNCA se encerra","Empatia específica vs. empatia genérica","Resposta robótica: 'resolvo, não informo'","Handoff: template de retomada correto","Ação sem autorização prévia do cliente","Conhecimento de produto: P&P, missões, vale-presente","Cupons: investigação antes de negar"],
    "tips":["KYC com erro técnico: escale, não repita o link","Empatia de qualidade menciona produto/situação real","Retomada: leia o histórico ANTES de escrever","Negar cupom sem investigar = risco de propaganda enganosa"],
  },
  {
    "file":"Flyer_Encerramento_Multiplos.html","game":"Jogo_casuisab_Equipe.html",
    "title":"Encerramento & Múltiplos Problemas","subtitle":"Qualidade no fechamento e organização de casos complexos",
    "emoji":"🎯","color":"#8b5cf6","color2":"#c4b5fd",
    "desc":"Como fechar um contato com qualidade, organizar casos com vários pedidos e transformar situações difíceis em experiências positivas para o cliente.",
    "topics":["Encerramento com 3 elementos: confirmação + próximo passo + abertura","Mini-resumo para múltiplos pedidos","Equiparação de preço: instrução de uso do vale","Churn declarado: reconhecer + registrar + âncora","Feedback de transportadora: abrir chamado e comunicar","6 dimensões CCX: Conhecimento, Eficiência, Prestatividade, Empatia, Cortesia, Clareza","Parked%: como impacta CCX e pontuação"],
    "tips":["Confirmar produto antes de agir reduz AHT (não aumenta)","Churn declarado: não encerre sem gesto","Clareza: cliente precisa entender o que foi feito","Parked = perda de avaliação positiva"],
  },
  {
    "file":"Flyer_Retomada.html","game":"Jogo_ejoseago_Equipe.html",
    "title":"Retomada & Resolução","subtitle":"Pausas, handoff, promessas e encerramento com qualidade",
    "emoji":"🔄","color":"#06b6d4","color2":"#67e8f9",
    "desc":"Situações reais de atendimento: pausas, retomada de chat pausado, pagamentos complexos, promessas de atendimentos anteriores e encerramento com qualidade.",
    "topics":["Retomada de chat pausado: ler histórico primeiro","Atualização intermediária durante verificação longa","Cupom dividido entre itens: entender antes de verificar","Links: sempre verificar antes de enviar","Contato com 3+ associates: reconhecimento de desgaste","Escalada: direito do cliente + registro formal","Âncora de próximo passo para pedidos atrasados","Empatia específica vs. genérica no CCX"],
    "tips":["Abertura mascarada (•••): reescreva imediatamente","Sempre ler histórico ANTES de escrever qualquer mensagem","Pedido de supervisor: registre formalmente, nunca negue","Promessa do atendimento anterior: prioridade máxima"],
  },
  {
    "file":"Flyer_PagamentoComplexo.html","game":"Jogo_msoarfra_Equipe.html",
    "title":"Pagamento Complexo & Resolução","subtitle":"Cupons, equiparações, alto valor e churn",
    "emoji":"💰","color":"#f97316","color2":"#fb923c",
    "desc":"Casos de alto valor onde organizar o raciocínio e fechar com solução concreta faz toda a diferença para o cliente — e para o seu CCX.",
    "topics":["Cupom dividido: confirmar entendimento antes de verificar","Tarifa de forma de pagamento (parcelamento)","Equiparação via vale-presente: âncora + instrução de uso","Churn declarado: empatia específica + ação concreta","Cancelamento sistêmico: explicar + opções + âncora","Pedido de alto valor (>R$500): atenção redobrada","Empatia: reconhecer antes de explicar a política","Passing values: sempre contextualizar os números"],
    "tips":["Sistema mostrando 'cupom aplicado' não encerra a análise","Churn: 'lamento pelo transtorno' genérico não basta","Alto valor = maior risco BTB, Procon e churn","Âncora de próximo passo transforma contato sem solução em contato gerenciado"],
  },
  {
    "file":"Flyer_DART.html","game":"Jogo_QuizDART_Equipe.html",
    "title":"DART — Transfere ou Resolve?","subtitle":"Quando escalar e quando resolver na fila",
    "emoji":"🎯","color":"#ef4444","color2":"#f87171",
    "desc":"DART duplica o handle time (18,6 vs 9,3 min). Cada vez que você aciona o DART desnecessariamente, o DUR sobe e o AHT aumenta. Este jogo treina quando escalar e quando resolver com autonomia.",
    "topics":["DART: quando é necessário vs. quando evitar","DUR: baixo DUR é POSITIVO para o time","CAP: TRACES vencido como condição obrigatória","AMZL: dano a propriedade vs. defeito de fábrica","QLA: fluxo separado (e-mail qla@amazon.com.br)","Conta Suspensa: SYSKA obrigatório","ECR: fluxo dedicado de transferência","CS Assistant e AC3: consultar antes de escalar"],
    "tips":["DART = 18,6 min; sem DART = 9,3 min — diferença enorme","TRACES vencido é condição, não apenas sugestão do AC3","Defeito de fábrica NÃO é caso AMZL","Pesquise no CS Assistant antes de escalar"],
  },
]

for f in FLYERS:
    html = flyer(f["title"], f["subtitle"], f["emoji"], f["desc"], f["topics"], f["tips"], f["color"], f["color2"], f["game"])
    path = os.path.join(BASE, f["file"])
    with open(path, 'wb') as fp:
        fp.write(html.encode('utf-8'))
    print(f"OK {f['file']} ({len(html)//1024}KB)")

print("FLYERS_DONE")
