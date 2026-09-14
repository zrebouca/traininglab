import os

BASE = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME'

AUTHOR = 'Mateus Rebou\u00e7as (zrebouca \u2014 Team Manager)'

FLYERS = [
    {
        'file': 'Flyer_AHT.html',
        'title': 'Como Reduzir o AHT',
        'subtitle': 'Efici\u00eancia no Atendimento',
        'emoji': '\u23f1\ufe0f',
        'grad': 'linear-gradient(135deg,#4f46e5,#7c3aed)',
        'border': '#4f46e5',
        'accent': '#4f46e5',
        'desc': 'O AHT (Average Handle Time) mede o tempo m\u00e9dio de cada atendimento. Reduzi-lo sem perder qualidade \u00e9 um dos principais desafios do CS — e poss\u00edvel com as t\u00e9cnicas certas.',
        'topics': [
            'O que \u00e9 o AHT e como ele \u00e9 calculado',
            'Principais causas de AHT elevado',
            'Investiga\u00e7\u00e3o diagn\u00f3stica antes de agir',
            'Uso eficiente das ferramentas (AC3, CorujãoCS)',
            'Encerramento objetivo e sem repeti\u00e7\u00f5es',
        ],
        'tips': [
            '\u2705 Leia o hist\u00f3rico do cliente <b>antes</b> de cumprimentar',
            '\u2705 Identifique a demanda nas primeiras mensagens',
            '\u2705 Use blurbs prontos — n\u00e3o escreva do zero',
            '\u2705 Confirme a resolu\u00e7\u00e3o em <b>uma</b> mensagem clara',
        ],
    },
    {
        'file': 'Flyer_Transferencias.html',
        'title': 'Transfere ou N\u00e3o?',
        'subtitle': 'Pol\u00edtica de Transfer\u00eancias CS BR',
        'emoji': '\ud83d\udd00',
        'grad': 'linear-gradient(135deg,#0284c7,#0ea5e9)',
        'border': '#0284c7',
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
            '\u2705 CAP: s\u00f3 ap\u00f3s data TRACES + solicitação do cliente',
            '\u2705 AMZL: apenas dano, les\u00e3o, roubo ou acidente',
            '\u2705 Em d\u00favida, resolva voc\u00ea mesmo antes de transferir',
            '\u2705 Cada transfer\u00eancia inv\u00e1lida custa pontos de CCX',
        ],
    },
    {
        'file': 'Flyer_ClienteDificil_CDC.html',
        'title': 'Cliente Dif\u00edcil & CDC',
        'subtitle': 'Gest\u00e3o Emocional e Legisla\u00e7\u00e3o',
        'emoji': '\u2696\ufe0f',
        'grad': 'linear-gradient(135deg,#7c3aed,#a855f7)',
        'border': '#7c3aed',
        'accent': '#7c3aed',
        'desc': 'Clientes agitados, ameaças ao Procon e cita\u00e7\u00f5es do CDC s\u00e3o sit\u00ade\u00e7\u00f5es que exigem preparo t\u00e9cnico e equil\u00edbrio emocional. Saber responder corretamente evita escala\u00e7\u00f5es e protege o time.',
        'topics': [
            'C\u00f3digo de Defesa do Consumidor — artigos principais',
            'Responsabilidade da Amazon em itens de parceiros',
            'Como responder a ameaças sem escalar o conflito',
            'Linguagem de acolhimento em situa\u00e7\u00f5es graves',
            'Encerramento correto ap\u00f3s cli\u00ebnte hostil',
        ],
        'tips': [
            '\u2705 Amazon tem responsabilidade solidária pela cadeia de fornecimento',
            '\u2705 Nunca diga "n\u00e3o conseguimos intervir" em casos CDC',
            '\u2705 Reconhe\u00e7a o sentimento antes de explicar a pol\u00edtica',
            '\u2705 Se o cliente ameaça Procon: n\u00e3o recue, tampouco confronte',
        ],
    },
    {
        'file': 'Flyer_Encerramento.html',
        'title': 'Opera\u00e7\u00e3o Encerramento',
        'subtitle': 'Encerramentos que Geram CCX Positivo',
        'emoji': '\ud83c\udfc1',
        'grad': 'linear-gradient(135deg,#0891b2,#06b6d4)',
        'border': '#0891b2',
        'accent': '#0891b2',
        'desc': 'O encerramento \u00e9 o \u00faltimo contato do cliente com a Amazon — e o que ele mais lembra. Um encerramento mal feito pode anular todo o atendimento anterior e gerar BTB mesmo com o problema resolvido.',
        'topics': [
            'Confirma\u00e7\u00e3o de resolu\u00e7\u00e3o antes de fechar',
            'Linguagem de encerramento memorável e personalizada',
            'Erros cl\u00e1ssicos: encerramento prematuro e robótico',
            'Pedir avalia\u00e7\u00e3o: o que nunca fazer',
            'Encerramento ap\u00f3s problema parcialmente resolvido',
        ],
        'tips': [
            '\u2705 Sempre confirme: "Consegui te ajudar com isso?"',
            '\u2705 Use o nome do cliente no encerramento',
            '\u2705 Nunca pe\u00e7a avalia\u00e7\u00e3o — direta ou indiretamente',
            '\u2705 Tom do encerramento deve refletir o estado do problema',
        ],
    },
    {
        'file': 'Flyer_Pagamentos.html',
        'title': 'Pagamentos CS BR',
        'subtitle': 'Cart\u00f5es, Pix e Reembolsos',
        'emoji': '\ud83d\udcb3',
        'grad': 'linear-gradient(135deg,#059669,#10b981)',
        'border': '#059669',
        'accent': '#059669',
        'desc': 'D\u00favidas sobre pagamento est\u00e3o entre os contatos de maior complexidade. Conhecer os fluxos de reembolso, as regras do Pix e a pol\u00edtica de cart\u00f5es recusados reduz AHT e aumenta a resolu\u00e7\u00e3o no primeiro contato.',
        'topics': [
            'Reembolso: prazos por forma de pagamento',
            'Pix: restri\u00e7\u00f5es tempor\u00e1rias e como comunicar',
            'Cart\u00e3o recusado: diagn\u00f3stico antes de encaminhar',
            'Cupons vs. descontos autom\u00e1ticos — diferen\u00e7a cr\u00edtica',
            'Vale-presente: resgate e cr\u00e9dito em conta',
        ],
        'tips': [
            '\u2705 Reembolso no cart\u00e3o: at\u00e9 2 faturas (n\u00e3o prometa data exata)',
            '\u2705 Pix bloqueado: use "tempor\u00e1rio, n\u00e3o grave" + alternativa',
            '\u2705 Cupom ≠ desconto PIX autom\u00e1tico — saiba a diferen\u00e7a',
            '\u2705 Nunca diga "o cart\u00e3o \u00e9 aceito" se o cliente j\u00e1 provou que n\u00e3o',
        ],
    },
    {
        'file': 'Flyer_QualidadeCS.html',
        'title': 'Qualidade no CS',
        'subtitle': 'O que Gera CCX Positivo e Negativo',
        'emoji': '\u2b50',
        'grad': 'linear-gradient(135deg,#d97706,#f59e0b)',
        'border': '#d97706',
        'accent': '#d97706',
        'desc': 'CCX n\u00e3o \u00e9 sorte — \u00e9 resultado de escolhas durante o atendimento. Entender o que gera BTB (Bottom Box) e o que gera TTB (Top Box) permite que cada CSA controle sua pr\u00f3pria avalia\u00e7\u00e3o.',
        'topics': [
            'As 6 dimens\u00f5es do BTB: Conhecimento, Efici\u00eancia, Prestatividade, Empatia, Cortesia, Clareza',
            'Comportamentos que geram BTB mesmo com problema resolvido',
            'O papel do encerramento na avalia\u00e7\u00e3o final',
            'Como o contato estacionado (parked) afeta seu CCX',
            'Padr\u00f5es de linguagem que aumentam TTB',
        ],
        'tips': [
            '\u2705 Empatia expl\u00edcita reduz BTB mesmo em situa\u00e7\u00f5es negativas',
            '\u2705 Contato estacionado = ponto de CCX perdido para outro CSA',
            '\u2705 Clareza > velocidade: respostas objetivas valem mais',
            '\u2705 Acolhimento no in\u00edcio define o tom de toda a intera\u00e7\u00e3o',
        ],
    },
    {
        'file': 'Flyer_Encerramento_Multiplos.html',
        'title': 'M\u00faltiplos Problemas & Encerramento',
        'subtitle': 'Priorizando e Resolvendo com Clareza',
        'emoji': '\ud83d\udccb',
        'grad': 'linear-gradient(135deg,#6d28d9,#8b5cf6)',
        'border': '#6d28d9',
        'accent': '#6d28d9',
        'desc': 'Quando um cliente chega com v\u00e1rias demandas ao mesmo tempo, o CSA precisa priorizar, estruturar e confirmar cada resolu\u00e7\u00e3o — sem deixar nada em aberto e sem encerrar prematuramente.',
        'topics': [
            'Como identificar a demanda principal rapidamente',
            'T\u00e9cnicas de prioriza\u00e7\u00e3o de m\u00faltiplas demandas',
            'Confirma\u00e7\u00e3o individual de cada problema antes de fechar',
            'Encerramento prematuro: o erro mais comum',
            'Leitura de hist\u00f3rico como ponto de partida obrigat\u00f3rio',
        ],
        'tips': [
            '\u2705 Liste os problemas em voz alta para o cliente logo no in\u00edcio',
            '\u2705 Resolva um por um — n\u00e3o misture fluxos',
            '\u2705 Confirme cada resolu\u00e7\u00e3o antes de passar para o pr\u00f3ximo',
            '\u2705 S\u00f3 encerre ap\u00f3s confirmar TODOS os itens pendentes',
        ],
    },
    {
        'file': 'Flyer_Retomada.html',
        'title': 'Retomada & Resolu\u00e7\u00e3o',
        'subtitle': 'Continuidade no Atendimento',
        'emoji': '\ud83d\udd04',
        'grad': 'linear-gradient(135deg,#0e7490,#06b6d4)',
        'border': '#0e7490',
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
            '\u2705 Antes de cumprimentar, leia o hist\u00f3rico completo',
            '\u2705 Mencione o que j\u00e1 foi tratado — o cliente n\u00e3o quer repetir',
            '\u2705 Ap\u00f3s pausa: reengage com resumo do que foi discutido',
            '\u2705 Diagn\u00f3stico antes de a\u00e7\u00e3o — nunca presuma a causa',
        ],
    },
    {
        'file': 'Flyer_PagamentoComplexo.html',
        'title': 'Pagamento Complexo & Resolu\u00e7\u00e3o',
        'subtitle': 'Casos de Alta Complexidade Financeira',
        'emoji': '\ud83d\udd0d',
        'grad': 'linear-gradient(135deg,#c2410c,#f97316)',
        'border': '#c2410c',
        'accent': '#c2410c',
        'desc': 'Alguns casos de pagamento envolvem m\u00faltiplas vari\u00e1veis: KYC bloqueado, reembolso urgente, conta com restri\u00e7\u00e3o e prazo prometido n\u00e3o cumprido. Esses casos exigem investiga\u00e7\u00e3o estruturada e postura de resolu\u00e7\u00e3o ativa.',
        'topics': [
            'KYC como ferramenta de segurança — nunca como bloqueador',
            'Reembolso urgente: quando e como explorar alternativas',
            'Conta com restri\u00e7\u00e3o de Pix vs. conta bloqueada por seguran\u00e7a',
            'Como comunicar prazos sem criar expectativas falsas',
            'Escala\u00e7\u00e3o correta vs. encerramento indevido',
        ],
        'tips': [
            '\u2705 KYC n\u00e3o encerra o contato — \u00e9 uma etapa, n\u00e3o uma sa\u00edda',
            '\u2705 Cliente urgente: explore alternativas antes do prazo padr\u00e3o',
            '\u2705 Conta bloqueada ≠ senha esquecida — fluxos completamente diferentes',
            '\u2705 Confirme o entendimento do cliente antes de encerrar',
        ],
    },
    {
        'file': 'Flyer_DART.html',
        'title': 'DART — Transfere ou Resolve?',
        'subtitle': 'Decis\u00e3o Correta no Contato Complexo',
        'emoji': '\ud83c\udfaf',
        'grad': 'linear-gradient(135deg,#b91c1c,#ef4444)',
        'border': '#b91c1c',
        'accent': '#b91c1c',
        'desc': 'DART n\u00e3o \u00e9 uma sa\u00edda — \u00e9 um recurso espec\u00edfico. Acionar o DART sem necessidade dobra o AHT do contato e transfere o problema sem resolv\u00ea-lo. Saber quando acionar e quando resolver por conta pr\u00f3pria \u00e9 fundamental.',
        'topics': [
            'O que \u00e9 o DART e quando ele se aplica de verdade',
            'Crit\u00e9rios obrigat\u00f3rios antes de acionar',
            'Casos que parecem DART mas t\u00eam resolu\u00e7\u00e3o direta',
            'Impacto do DUR no desempenho individual e do time',
            'Documenta\u00e7\u00e3o correta do SIC antes de transferir',
        ],
        'tips': [
            '\u2705 Antes de acionar: "eu consigo resolver isso sem DART?"',
            '\u2705 DART com SIC em branco = contato inv\u00e1lido',
            '\u2705 DUR alto = AHT alto — cada acionamento conta',
            '\u2705 Use o DART Decisor no CorujãoCS para checar antes de transferir',
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
  .topics li::before{{content:"\u25b8";color:{accent};font-size:.85rem;margin-top:2px;flex-shrink:0}}
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
    topics_html = '\n      '.join(f'<li>{t}</li>' for t in fl['topics'])
    tips_html   = '\n        '.join(f'<li>{t}</li>' for t in fl['tips'])
    html = FLYER_TPL.format(
        title=fl['title'], subtitle=fl['subtitle'],
        emoji=fl['emoji'], grad=fl['grad'],
        accent=fl['accent'], border=fl['border'],
        desc=fl['desc'],
        topics_html=topics_html, tips_html=tips_html,
        author=AUTHOR,
    )
    path = os.path.join(BASE, fl['file'])
    open(path, 'wb').write(html.encode('utf-8'))
    print('OK', fl['file'])

print('Done: %d flyers written' % len(FLYERS))
