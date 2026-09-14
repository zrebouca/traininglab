import os

BASE = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME'
AUTHOR = 'Mateus Rebou\u00e7as (zrebouca \u2014 Team Manager)'

# Emojis as HTML entities to avoid surrogate encoding issues
FLYERS = [
    {
        'file': 'Flyer_AHT.html',
        'title': 'Como Reduzir o AHT',
        'subtitle': 'Efici\u00eancia no Atendimento',
        'emoji': '&#x23F1;&#xFE0F;',
        'grad': 'linear-gradient(135deg,#4f46e5,#7c3aed)',
        'accent': '#4f46e5',
        'desc': 'O AHT (Average Handle Time) mede o tempo m\u00e9dio de cada atendimento. Reduzi-lo sem perder qualidade \u00e9 um dos principais desafios do CS \u2014 e poss\u00edvel com as t\u00e9cnicas certas.',
        'topics': [
            'O que \u00e9 o AHT e como ele \u00e9 calculado',
            'Principais causas de AHT elevado',
            'Investiga\u00e7\u00e3o diagn\u00f3stica antes de agir',
            'Uso eficiente das ferramentas (AC3, CorujãoCS)',
            'Encerramento objetivo e sem repeti\u00e7\u00f5es',
        ],
        'tips': [
            '&#x2705; Leia o hist\u00f3rico do cliente <b>antes</b> de cumprimentar',
            '&#x2705; Identifique a demanda nas primeiras mensagens',
            '&#x2705; Use blurbs prontos \u2014 n\u00e3o escreva do zero',
            '&#x2705; Confirme a resolu\u00e7\u00e3o em <b>uma</b> mensagem clara',
        ],
    },
    {
        'file': 'Flyer_Transferencias.html',
        'title': 'Transfere ou N\u00e3o?',
        'subtitle': 'Pol\u00edtica de Transfer\u00eancias CS BR',
        'emoji': '&#x1F500;',
        'grad': 'linear-gradient(135deg,#0284c7,#0ea5e9)',
        'accent': '#0284c7',
        'desc': 'Transferir sem necessidade \u00e9 uma das principais causas de HRR elevado e perda de CCX. Conhecer as regras de cada destino evita transfer\u00eancias inv\u00e1lidas e mant\u00e9m o cliente satisfeito.',
        'topics': [
            'Crit\u00e9rios obrigat\u00f3rios para CAP, AMZL e especialistas',
            'Quando o AC3 sugere transfer\u00eancia e ele est\u00e1 errado',
            'Destinos v\u00e1lidos: QLA, APEX, Prime Video, Kindle e outros',
            'Transfer\u00eancias que nunca s\u00e3o v\u00e1lidas',
            'Impacto do HRR no CCX do time',
        ],
        'tips': [
            '&#x2705; CAP: s\u00f3 ap\u00f3s data TRACES + solicita\u00e7\u00e3o do cliente',
            '&#x2705; AMZL: apenas dano, les\u00e3o, roubo ou acidente',
            '&#x2705; Em d\u00favida, resolva voc\u00ea mesmo antes de transferir',
            '&#x2705; Cada transfer\u00eancia inv\u00e1lida custa pontos de CCX',
        ],
    },
    {
        'file': 'Flyer_ClienteDificil_CDC.html',
        'title': 'Cliente Dif\u00edcil & CDC',
        'subtitle': 'Gest\u00e3o Emocional e Legisla\u00e7\u00e3o',
        'emoji': '&#x2696;&#xFE0F;',
        'grad': 'linear-gradient(135deg,#7c3aed,#a855f7)',
        'accent': '#7c3aed',
        'desc': 'Clientes agitados, amea\u00e7as ao Procon e cita\u00e7\u00f5es do CDC s\u00e3o situa\u00e7\u00f5es que exigem preparo t\u00e9cnico e equil\u00edbrio emocional. Saber responder corretamente evita escala\u00e7\u00f5es e protege o time.',
        'topics': [
            'C\u00f3digo de Defesa do Consumidor \u2014 artigos principais',
            'Responsabilidade da Amazon em itens de parceiros',
            'Como responder a amea\u00e7as sem escalar o conflito',
            'Linguagem de acolhimento em situa\u00e7\u00f5es graves',
            'Encerramento correto ap\u00f3s cliente hostil',
        ],
        'tips': [
            '&#x2705; Amazon tem responsabilidade solid\u00e1ria pela cadeia de fornecimento',
            '&#x2705; Nunca diga &#34;n\u00e3o conseguimos intervir&#34; em casos CDC',
            '&#x2705; Reconhe\u00e7a o sentimento antes de explicar a pol\u00edtica',
            '&#x2705; Se o cliente amea\u00e7a Procon: n\u00e3o recue, tampouco confronte',
        ],
    },
    {
        'file': 'Flyer_Encerramento.html',
        'title': 'Opera\u00e7\u00e3o Encerramento',
        'subtitle': 'Encerramentos que Geram CCX Positivo',
        'emoji': '&#x1F3C1;',
        'grad': 'linear-gradient(135deg,#0891b2,#06b6d4)',
        'accent': '#0891b2',
        'desc': 'O encerramento \u00e9 o \u00faltimo contato do cliente com a Amazon \u2014 e o que ele mais lembra. Um encerramento mal feito pode anular todo o atendimento anterior e gerar BTB mesmo com o problema resolvido.',
        'topics': [
            'Confirma\u00e7\u00e3o de resolu\u00e7\u00e3o antes de fechar',
            'Linguagem de encerramento memor\u00e1vel e personalizada',
            'Erros cl\u00e1ssicos: encerramento prematuro e rob\u00f3tico',
            'Pedir avalia\u00e7\u00e3o: o que nunca fazer',
            'Encerramento ap\u00f3s problema parcialmente resolvido',
        ],
        'tips': [
            '&#x2705; Sempre confirme: &#34;Consegui te ajudar com isso?&#34;',
            '&#x2705; Use o nome do cliente no encerramento',
            '&#x2705; Nunca pe\u00e7a avalia\u00e7\u00e3o \u2014 direta ou indiretamente',
            '&#x2705; Tom do encerramento deve refletir o estado do problema',
        ],
    },
    {
        'file': 'Flyer_Pagamentos.html',
        'title': 'Pagamentos CS BR',
        'subtitle': 'Cart\u00f5es, Pix e Reembolsos',
        'emoji': '&#x1F4B3;',
        'grad': 'linear-gradient(135deg,#059669,#10b981)',
        'accent': '#059669',
        'desc': 'D\u00favidas sobre pagamento est\u00e3o entre os contatos de maior complexidade. Conhecer os fluxos de reembolso, as regras do Pix e a pol\u00edtica de cart\u00f5es recusados reduz AHT e aumenta a resolu\u00e7\u00e3o no primeiro contato.',
        'topics': [
            'Reembolso: prazos por forma de pagamento',
            'Pix: restri\u00e7\u00f5es tempor\u00e1rias e como comunicar',
            'Cart\u00e3o recusado: diagn\u00f3stico antes de encaminhar',
            'Cupons vs. descontos autom\u00e1ticos \u2014 diferen\u00e7a cr\u00edtica',
            'Vale-presente: resgate e cr\u00e9dito em conta',
        ],
        'tips': [
            '&#x2705; Reembolso no cart\u00e3o: at\u00e9 2 faturas (n\u00e3o prometa data exata)',
            '&#x2705; Pix bloqueado: use &#34;tempor\u00e1rio, n\u00e3o grave&#34; + alternativa',
            '&#x2705; Cupom &#x2260; desconto PIX autom\u00e1tico \u2014 saiba a diferen\u00e7a',
            '&#x2705; Nunca diga &#34;o cart\u00e3o \u00e9 aceito&#34; se o cliente j\u00e1 provou que n\u00e3o',
        ],
    },
    {
        'file': 'Flyer_QualidadeCS.html',
        'title': 'Qualidade no CS',
        'subtitle': 'O que Gera CCX Positivo e Negativo',
        'emoji': '&#x2B50;',
        'grad': 'linear-gradient(135deg,#d97706,#f59e0b)',
        'accent': '#d97706',
        'desc': 'CCX n\u00e3o \u00e9 sorte \u2014 \u00e9 resultado de escolhas durante o atendimento. Entender o que gera BTB (Bottom Box) e o que gera TTB (Top Box) permite que cada CSA controle sua pr\u00f3pria avalia\u00e7\u00e3o.',
        'topics': [
            'As 6 dimens\u00f5es do BTB: Conhecimento, Efici\u00eancia, Prestatividade, Empatia, Cortesia, Clareza',
            'Comportamentos que geram BTB mesmo com problema resolvido',
            'O papel do encerramento na avalia\u00e7\u00e3o final',
            'Como o contato estacionado (parked) afeta seu CCX',
            'Padr\u00f5es de linguagem que aumentam TTB',
        ],
        'tips': [
            '&#x2705; Empatia expl\u00edcita reduz BTB mesmo em situa\u00e7\u00f5es negativas',
            '&#x2705; Contato estacionado = ponto de CCX perdido para outro CSA',
            '&#x2705; Clareza > velocidade: respostas objetivas valem mais',
            '&#x2705; Acolhimento no in\u00edcio define o tom de toda a intera\u00e7\u00e3o',
        ],
    },
    {
        'file': 'Flyer_Encerramento_Multiplos.html',
        'title': 'M\u00faltiplos Problemas & Encerramento',
        'subtitle': 'Priorizando e Resolvendo com Clareza',
        'emoji': '&#x1F4CB;',
        'grad': 'linear-gradient(135deg,#6d28d9,#8b5cf6)',
        'accent': '#6d28d9',
        'desc': 'Quando um cliente chega com v\u00e1rias demandas ao mesmo tempo, o CSA precisa priorizar, estruturar e confirmar cada resolu\u00e7\u00e3o \u2014 sem deixar nada em aberto e sem encerrar prematuramente.',
        'topics': [
            'Como identificar a demanda principal rapidamente',
            'T\u00e9cnicas de prioriza\u00e7\u00e3o de m\u00faltiplas demandas',
            'Confirma\u00e7\u00e3o individual de cada problema antes de fechar',
            'Encerramento prematuro: o erro mais comum',
            'Leitura de hist\u00f3rico como ponto de partida obrigat\u00f3rio',
        ],
        'tips': [
            '&#x2705; Liste os problemas em voz alta para o cliente logo no in\u00edcio',
            '&#x2705; Resolva um por um \u2014 n\u00e3o misture fluxos',
            '&#x2705; Confirme cada resolu\u00e7\u00e3o antes de passar para o pr\u00f3ximo',
            '&#x2705; S\u00f3 encerre ap\u00f3s confirmar TODOS os itens pendentes',
        ],
    },
    {
        'file': 'Flyer_Retomada.html',
        'title': 'Retomada & Resolu\u00e7\u00e3o',
        'subtitle': 'Continuidade no Atendimento',
        'emoji': '&#x1F504;',
        'grad': 'linear-gradient(135deg,#0e7490,#06b6d4)',
        'accent': '#0e7490',
        'desc': 'Quando um atendimento \u00e9 interrompido ou retomado ap\u00f3s uma pausa, o cliente n\u00e3o deve sentir que come\u00e7ou do zero. A retomada eficaz demonstra aten\u00e7\u00e3o e reduz o tempo total de resolu\u00e7\u00e3o.',
        'topics': [
            'Como fazer uma retomada que demonstra leitura do contexto',
            'Leitura do hist\u00f3rico de recontato antes de responder',
            'Sinais de que o cliente j\u00e1 entrou em contato antes',
            'Retomada ap\u00f3s pausa longa no chat',
            'Investiga\u00e7\u00e3o estruturada antes de qualquer a\u00e7\u00e3o',
        ],
        'tips': [
            '&#x2705; Antes de cumprimentar, leia o hist\u00f3rico completo',
            '&#x2705; Mencione o que j\u00e1 foi tratado \u2014 o cliente n\u00e3o quer repetir',
            '&#x2705; Ap\u00f3s pausa: reengage com resumo do que foi discutido',
            '&#x2705; Diagn\u00f3stico antes de a\u00e7\u00e3o \u2014 nunca presuma a causa',
        ],
    },
    {
        'file': 'Flyer_PagamentoComplexo.html',
        'title': 'Pagamento Complexo & Resolu\u00e7\u00e3o',
        'subtitle': 'Casos de Alta Complexidade Financeira',
        'emoji': '&#x1F50D;',
        'grad': 'linear-gradient(135deg,#c2410c,#f97316)',
        'accent': '#c2410c',
        'desc': 'Alguns casos de pagamento envolvem m\u00faltiplas vari\u00e1veis: KYC bloqueado, reembolso urgente, conta com restri\u00e7\u00e3o e prazo prometido n\u00e3o cumprido. Esses casos exigem investiga\u00e7\u00e3o estruturada e postura de resolu\u00e7\u00e3o ativa.',
        'topics': [
            'KYC como ferramenta de seguran\u00e7a \u2014 nunca como bloqueador',
            'Reembolso urgente: quando e como explorar alternativas',
            'Conta com restri\u00e7\u00e3o de Pix vs. conta bloqueada por seguran\u00e7a',
            'Como comunicar prazos sem criar expectativas falsas',
            'Escala\u00e7\u00e3o correta vs. encerramento indevido',
        ],
        'tips': [
            '&#x2705; KYC n\u00e3o encerra o contato \u2014 \u00e9 uma etapa, n\u00e3o uma sa\u00edda',
            '&#x2705; Cliente urgente: explore alternativas antes do prazo padr\u00e3o',
            '&#x2705; Conta bloqueada &#x2260; senha esquecida \u2014 fluxos completamente diferentes',
            '&#x2705; Confirme o entendimento do cliente antes de encerrar',
        ],
    },
    {
        'file': 'Flyer_DART.html',
        'title': 'DART \u2014 Transfere ou Resolve?',
        'subtitle': 'Decis\u00e3o Correta no Contato Complexo',
        'emoji': '&#x1F3AF;',
        'grad': 'linear-gradient(135deg,#b91c1c,#ef4444)',
        'accent': '#b91c1c',
        'desc': 'DART n\u00e3o \u00e9 uma sa\u00edda \u2014 \u00e9 um recurso espec\u00edfico. Acionar o DART sem necessidade dobra o AHT do contato e transfere o problema sem resolv\u00ea-lo. Saber quando acionar e quando resolver por conta pr\u00f3pria \u00e9 fundamental.',
        'topics': [
            'O que \u00e9 o DART e quando ele se aplica de verdade',
            'Crit\u00e9rios obrigat\u00f3rios antes de acionar',
            'Casos que parecem DART mas t\u00eam resolu\u00e7\u00e3o direta',
            'Impacto do DUR no desempenho individual e do time',
            'Documenta\u00e7\u00e3o correta do SIC antes de transferir',
        ],
        'tips': [
            '&#x2705; Antes de acionar: &#34;eu consigo resolver isso sem DART?&#34;',
            '&#x2705; DART com SIC em branco = contato inv\u00e1lido',
            '&#x2705; DUR alto = AHT alto \u2014 cada acionamento conta',
            '&#x2705; Use o DART Decisor no Coruj\u00e3oCS para checar antes de transferir',
        ],
    },
]

FLYER_TPL = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Segoe UI',Arial,sans-serif;background:#f1f5f9;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:32px 16px}}
  .card{{background:#fff;border-radius:20px;max-width:680px;width:100%;box-shadow:0 8px 40px rgba(0,0,0,.12);overflow:hidden}}
  .header{{background:{grad};padding:36px 32px 28px;color:#fff;position:relative}}
  .header-emoji{{font-size:2.8rem;margin-bottom:10px;display:block}}
  .header h1{{font-size:1.75rem;font-weight:800;letter-spacing:-.5px;margin-bottom:6px}}
  .header p{{font-size:1rem;opacity:.88;font-weight:500}}
  .tag{{display:inline-block;background:rgba(255,255,255,.22);border-radius:20px;padding:3px 14px;font-size:.78rem;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-bottom:14px}}
  .body{{padding:30px 32px 24px}}
  .desc{{font-size:1rem;color:#334155;line-height:1.65;margin-bottom:24px}}
  .section-label{{font-size:.72rem;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:{accent};margin-bottom:10px}}
  .topics{{list-style:none;margin-bottom:24px}}
  .topics li{{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid #f1f5f9;font-size:.93rem;color:#1e293b}}
  .topics li:last-child{{border:none}}
  .topics li::before{{content:"\\25b8";color:{accent};font-size:.85rem;margin-top:2px;flex-shrink:0}}
  .tips{{background:#f8fafc;border-left:4px solid {accent};border-radius:0 12px 12px 0;padding:16px 20px;margin-bottom:24px}}
  .tips ul{{list-style:none}}
  .tips ul li{{font-size:.9rem;color:#334155;padding:5px 0;line-height:1.5}}
  .footer{{border-top:1px solid #f1f5f9;padding:14px 32px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
  .footer-brand{{font-size:.75rem;color:#94a3b8;font-weight:600}}
  .footer-author{{font-size:.72rem;color:#cbd5e1}}
  @media print{{body{{background:#fff;padding:0}} .card{{box-shadow:none;border-radius:0;max-width:100%}}}}
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <span class="tag">Treinamento CS BR</span>
    <span class="header-emoji">{emoji}</span>
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
  <div class="body">
    <p class="desc">{desc}</p>
    <p class="section-label">T\u00f3picos Abordados</p>
    <ul class="topics">
      {topics_html}
    </ul>
    <p class="section-label">Pontos-Chave</p>
    <div class="tips">
      <ul>
        {tips_html}
      </ul>
    </div>
  </div>
  <div class="footer">
    <span class="footer-brand">Amazon CS BR &mdash; Time de Qualidade</span>
    <span class="footer-author">Desenvolvido por {author} &middot; 2026</span>
  </div>
</div>
</body>
</html>'''

os.makedirs(BASE, exist_ok=True)
for fl in FLYERS:
    topics_html = '\n      '.join('<li>' + t + '</li>' for t in fl['topics'])
    tips_html   = '\n        '.join('<li>' + t + '</li>' for t in fl['tips'])
    html = FLYER_TPL.format(
        title=fl['title'], subtitle=fl['subtitle'],
        emoji=fl['emoji'], grad=fl['grad'],
        accent=fl['accent'],
        desc=fl['desc'],
        topics_html=topics_html, tips_html=tips_html,
        author=AUTHOR,
    )
    path = os.path.join(BASE, fl['file'])
    open(path, 'wb').write(html.encode('utf-8'))
    print('OK', fl['file'])

print('Done: %d flyers written' % len(FLYERS))
