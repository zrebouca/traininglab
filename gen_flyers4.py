import os

BASE = r'C:\Users\zrebouca\Desktop\Jogos_Treinamento\TIME'
AUTHOR = 'Mateus Rebou\u00e7as (zrebouca \u2014 Team Manager)'

FLYERS = [
    {
        'file': 'Flyer_AHT.html',
        'title': 'Como Reduzir o AHT',
        'subtitle': 'Efici\u00eancia no Atendimento',
        'emoji': '&#x23F1;&#xFE0F;',
        'grad': 'linear-gradient(135deg,#4f46e5,#7c3aed)',
        'accent': '#4f46e5',
        'desc': 'O AHT (Average Handle Time) mede o tempo m\u00e9dio de cada atendimento. Reduzi-lo sem perder qualidade \u00e9 um dos principais desafios do CS \u2014 e poss\u00edvel com as t\u00e9cnicas certas.',
        'accordions': [
            {
                'title': 'O que \u00e9 o AHT e como \u00e9 calculado?',
                'body': 'O AHT \u00e9 calculado somando o tempo de conversa ativa com o tempo de p\u00f3s-atendimento (wrap-up), dividido pelo n\u00famero de contatos. Mesmo uma pausa desnecess\u00e1ria de 2 minutos por contato, multiplicada por 40 contatos/dia, representa mais de 1h20 de tempo improdutivo.',
            },
            {
                'title': 'Quais s\u00e3o as principais causas de AHT elevado?',
                'body': 'As causas mais comuns s\u00e3o: n\u00e3o ler o hist\u00f3rico antes de come\u00e7ar, fazer perguntas j\u00e1 respondidas pelo cliente, redigir respostas do zero em vez de usar templates, pausas excessivas sem comunica\u00e7\u00e3o, e encerramento longo ou repetitivo. DART desnecessário tamb\u00e9m dobra o AHT do contato.',
            },
            {
                'title': 'Como o AHT se correlaciona com outras m\u00e9tricas?',
                'body': 'AHT alto geralmente acompanha HRR alto (muitas pausas/transfer\u00eancias) e pode reduzir o CCX quando o cliente sente demora sem progresso. Por outro lado, reduzir AHT demais com encerramentos prematuros gera BTB. O equil\u00edbrio \u00e9: resolver r\u00e1pido sem cortar o atendimento antes da hora.',
            },
            {
                'title': 'T\u00e9cnicas pr\u00e1ticas para reduzir o AHT',
                'body': '<b>1.</b> Leia o hist\u00f3rico completo antes de cumprimentar.<br><b>2.</b> Identifique a demanda nas 2 primeiras mensagens.<br><b>3.</b> Use templates e blurbs prontos \u2014 n\u00e3o escreva do zero.<br><b>4.</b> Comunique pausas: "Vou verificar aqui, um momento."<br><b>5.</b> Confirme a resolu\u00e7\u00e3o em uma \u00fanica mensagem clara antes de encerrar.',
            },
            {
                'title': 'O que NÃO fazer ao tentar reduzir o AHT',
                'body': 'N\u00e3o encerre o contato antes de confirmar a resolu\u00e7\u00e3o. N\u00e3o transfira para diminuir seu pr\u00f3prio tempo \u2014 isso aumenta o HRR do time. N\u00e3o ignore demandas secund\u00e1rias apenas para fechar mais r\u00e1pido. Velocidade sem qualidade gera recontato, que \u00e9 o pior inimigo do AHT m\u00e9dio.',
            },
        ],
    },
    {
        'file': 'Flyer_Transferencias.html',
        'title': 'Transfere ou N\u00e3o?',
        'subtitle': 'Pol\u00edtica de Transfer\u00eancias CS BR',
        'emoji': '&#x1F500;',
        'grad': 'linear-gradient(135deg,#0284c7,#0ea5e9)',
        'accent': '#0284c7',
        'desc': 'Transferir sem necessidade \u00e9 uma das principais causas de HRR elevado e perda de CCX. Conhecer os crit\u00e9rios corretos de cada destino evita transfer\u00eancias inv\u00e1lidas e mant\u00e9m o cliente satisfeito.',
        'accordions': [
            {
                'title': 'O que \u00e9 o HRR e como transfer\u00eancias o afetam?',
                'body': 'O HRR (Handle Rate Ratio) mede quantas vezes um contato passou por pausas, transfer\u00eancias ou filas antes da resolu\u00e7\u00e3o. Cada transfer\u00eancia desnecessária aumenta o HRR do time e reduz a experi\u00eancia do cliente, que precisa se repetir. O HRR ideal \u00e9 \u2264 125%. Acima disso, o time perde CCX.',
            },
            {
                'title': 'Quando transferir para o CAP?',
                'body': 'O CAP s\u00f3 deve receber a transfer\u00eancia quando <b>todos</b> os 3 crit\u00e9rios forem atendidos: (1) o cliente solicitou reembolso ou substitui\u00e7\u00e3o, (2) o fluxo AC3 foi iniciado, e (3) a data TRACES j\u00e1 passou. O AC3 \u00e0s vezes sugere a transfer\u00eancia antes da data TRACES \u2014 nesse caso, ignore a sugest\u00e3o e aguarde.',
            },
            {
                'title': 'Quando transferir para a AMZL?',
                'body': 'A AMZL s\u00f3 aceita transfer\u00eancias em casos de: dano \u00e0 propriedade, les\u00e3o f\u00edsica, acidente com ve\u00edculo, roubo ou fatalidade. <b>N\u00e3o</b> s\u00e3o motivos v\u00e1lidos: atrasos, tentativas de entrega n\u00e3o realizadas, itens danificados na embalagem ou coment\u00e1rios negativos sobre o entregador.',
            },
            {
                'title': 'Outros destinos e quando usar',
                'body': 'Destinos v\u00e1lidos incluem: QLA, Conta Suspensa, APEX, Prime Video, Kindle, KDP, Music, Audible, Vendedores Parceiros, Internacional e outros. Cada um tem crit\u00e9rios espec\u00edficos. Quando em d\u00favida, tente resolver voc\u00ea mesmo antes de transferir. Transfer\u00eancia sem crit\u00e9rio \u00e9 sempre a pior op\u00e7\u00e3o.',
            },
            {
                'title': 'Transfer\u00eancia e CCX: a conex\u00e3o direta',
                'body': 'Cada transfer\u00eancia inv\u00e1lida tem duplo impacto: aumenta o HRR do time <b>e</b> reduz a chance de CCX positivo do contato. O cliente transferido para o lugar errado recontata, gerando novo AHT. Um contato resolvido na primeira tentativa vale muito mais do que tr\u00eas contatos distribu\u00eddos.',
            },
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
        'accordions': [
            {
                'title': 'O que diz o CDC sobre a responsabilidade da Amazon?',
                'body': 'Pelo C\u00f3digo de Defesa do Consumidor (Lei 8.078/1990), a Amazon tem responsabilidade solid\u00e1ria na cadeia de fornecimento \u2014 mesmo em itens vendidos por parceiros. Isso significa que dizer "n\u00e3o conseguimos intervir" ou "somos s\u00f3 plataforma" \u00e9 juridicamente incorreto e configura risco de escala\u00e7\u00e3o ao Procon.',
            },
            {
                'title': 'Artigos mais citados pelos clientes',
                'body': '<b>Art. 30:</b> Oferta vincula \u2014 o que foi anunciado deve ser cumprido.<br><b>Art. 35:</b> Descumprimento da oferta d\u00e1 ao consumidor o direito de exigir o cumprimento for\u00e7ado, aceitar produto equivalente ou cancelar com reembolso.<br><b>Art. 18:</b> Respons\u00e1bilidade solid\u00e1ria por v\u00edcios do produto.<br>Quando o cliente cita esses artigos, n\u00e3o ignore \u2014 reconhe\u00e7a e trate com seriedade.',
            },
            {
                'title': 'Como responder a um cliente hostil sem escalar',
                'body': 'N\u00e3o confronte diretamente nem recue imediatamente. A seq\u00fc\u00eancia eficaz \u00e9: (1) reconhe\u00e7a o sentimento sem concordar com a hostilidade, (2) demonstre que entendeu o problema, (3) apresente o caminho de resolu\u00e7\u00e3o com clareza. Clientes hostis geralmente acalmam quando sentem que foram ouvidos de verdade.',
            },
            {
                'title': 'CDC e CCX: como est\u00e3o conectados?',
                'body': 'Contatos com cita\u00e7\u00e3o de CDC que s\u00e3o mal tratados t\u00eam alta probabilidade de gerar BTB e escala\u00e7\u00e3o. Um atendimento que reconhece a legisla\u00e7\u00e3o e oferece a solu\u00e7\u00e3o correta tende a gerar TTB mesmo em situa\u00e7\u00f5es de conflito. Conhecer o CDC \u00e9 uma vantagem direta na sua avalia\u00e7\u00e3o de qualidade.',
            },
            {
                'title': 'Linguagem recomendada em situa\u00e7\u00f5es graves',
                'body': 'Use: "Entendo como essa situa\u00e7\u00e3o \u00e9 frustrante, e quero te ajudar a resolver isso agora." Evite: "Infelizmente n\u00e3o posso fazer nada" ou "Isso n\u00e3o \u00e9 com a gente." Sempre ofere\u00e7a um caminho, mesmo que o caminho seja um prazo ou um escalonamento formal \u2014 o cliente precisa sair com uma pr\u00f3xima etapa clara.',
            },
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
        'accordions': [
            {
                'title': 'Por que o encerramento impacta tanto o CCX?',
                'body': 'Estudos de experi\u00eancia do cliente mostram que as \u00faltimas intera\u00e7\u00f5es t\u00eam peso desproporcional na avalia\u00e7\u00e3o final (efeito "peak-end"). Isso significa que um atendimento bom pode ser avaliado negativamente se o encerramento for frio, apressado ou incompleto. O BTB de "Clareza" e "Prestatividade" s\u00e3o os mais afetados por encerramentos ruins.',
            },
            {
                'title': 'O erro mais comum: encerramento prematuro',
                'body': 'Encerrar prematuro significa fechar o contato ap\u00f3s entregar a informa\u00e7\u00e3o \u2014 sem confirmar se o problema foi resolvido. O CSA sente que "fez sua parte", mas o cliente ainda tem d\u00favidas. Resultado: recontato (AHT extra) + BTB. A confirma\u00e7\u00e3o antes do encerramento \u00e9 obrigat\u00f3ria, n\u00e3o opcional.',
            },
            {
                'title': 'Como estruturar um encerramento eficaz',
                'body': '<b>1.</b> Confirme: "Consegui te ajudar com isso?" ou "Ficou alguma d\u00favida?"<br><b>2.</b> Personalize: use o nome do cliente.<br><b>3.</b> Oriente: informe pr\u00f3ximo passo se houver (ex: prazo de reembolso).<br><b>4.</b> Encerre com cordialidade genuína \u2014 sem f\u00f3rmulas rob\u00f3ticas.<br><b>5.</b> Nunca pe\u00e7a avalia\u00e7\u00e3o \u2014 nem direta nem indiretamente.',
            },
            {
                'title': 'Encerramento ap\u00f3s problema n\u00e3o totalmente resolvido',
                'body': 'Quando o problema continua em aberto (ex: item ainda em tr\u00e2nsito), o tom do encerramento deve refletir isso. N\u00e3o use linguagem comemorativa nem "fico feliz em ter resolvido". Use: "Registrei aqui e acompanharei o andamento. Assim que houver atualiza\u00e7\u00e3o, voc\u00ea ser\u00e1 notificado." Tom correto = empático e forward-looking.',
            },
            {
                'title': 'Pedir avalia\u00e7\u00e3o: por que \u00e9 proibido?',
                'body': 'Solicitar avalia\u00e7\u00e3o \u2014 direta ("d\u00ea uma nota 5") ou indiretamente ("fique at\u00e9 o final") \u2014 viola as diretrizes CCX. O motivo \u00e9 que avalia\u00e7\u00f5es solicitadas s\u00e3o enviesadas e n\u00e3o refletem a experi\u00eancia real. A meta \u00e9 que o cliente avalie <b>espontaneamente</b> porque o atendimento foi excelente.',
            },
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
        'accordions': [
            {
                'title': 'Prazos de reembolso por forma de pagamento',
                'body': '<b>Cart\u00e3o de cr\u00e9dito:</b> at\u00e9 2 faturas ap\u00f3s o processamento \u2014 nunca prometa data exata.<br><b>Boleto/Pix:</b> 3 a 5 dias \u00fateis ap\u00f3s a aprova\u00e7\u00e3o do reembolso.<br><b>Vale-presente:</b> creditado imediatamente ap\u00f3s processamento.<br>Aten\u00e7\u00e3o: informar o prazo errado gera recontato e BTB de "Conhecimento".',
            },
            {
                'title': 'Pix: restri\u00e7\u00f5es e como comunicar corretamente',
                'body': 'Quando a conta tem restri\u00e7\u00e3o de Pix, o framing correto \u00e9: "sua conta est\u00e1 com uma restri\u00e7\u00e3o tempor\u00e1ria no Pix, mas n\u00e3o \u00e9 nada grave \u2014 voc\u00ea pode usar cart\u00e3o de cr\u00e9dito normalmente." Nunca use os termos "abuso", "abusador" ou "bloqueio por abuso". A restri\u00e7\u00e3o \u00e9 sempre enquadrada como tempor\u00e1ria e com alternativa.',
            },
            {
                'title': 'Cart\u00e3o recusado: como diagnosticar antes de agir',
                'body': 'N\u00e3o afirme que o cart\u00e3o \u00e9 aceito se o cliente j\u00e1 tentou e falhou. Primeiro investigue: (1) o sistema mostra o cart\u00e3o como ativo? (2) h\u00e1 limite dispon\u00edvel? (3) \u00e9 uma bandeira aceita? Se o sistema diz "aceito" mas o cliente tem evid\u00eancia do contr\u00e1rio, trate como conflito de informa\u00e7\u00e3o e escale em vez de contradizer o cliente.',
            },
            {
                'title': 'Cupom vs. desconto autom\u00e1tico: a diferen\u00e7a cr\u00edtica',
                'body': 'Um <b>cupom</b> \u00e9 um c\u00f3digo aplicado manualmente pelo cliente. Um <b>desconto autom\u00e1tico</b> (como o desconto PIX de R$4,20) \u00e9 aplicado pelo sistema sem c\u00f3digo. Confundir os dois e dizer "tem cupom sim" quando o cliente est\u00e1 descrevendo um desconto autom\u00e1tico \u00e9 um erro de conhecimento que gera conflito desnecess\u00e1rio.',
            },
            {
                'title': 'Vale-presente: resgate e cr\u00e9dito em conta',
                'body': 'O vale-presente \u00e9 resgatado via c\u00f3digo na p\u00e1gina de conta do cliente. O saldo vai direto para a conta Amazon e pode ser usado em qualquer compra. A Amazon BR n\u00e3o vende mais vale-presente \u2014 apenas processa resgates e reembolsos em forma de cr\u00e9dito. Oriente o cliente sobre como verificar o saldo em "Minha conta > Vale-Presente".',
            },
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
        'accordions': [
            {
                'title': 'O que s\u00e3o TTB, BTB e como s\u00e3o calculados?',
                'body': '<b>TTB (Top Two Box):</b> percentual de avalia\u00e7\u00f5es 4 ou 5 estrelas. Meta: \u2265 92,92%.<br><b>BTB (Bottom Box):</b> percentual de avalia\u00e7\u00f5es de 1 ou 2 estrelas. Quanto menor, melhor.<br>O CCX \u00e9 medido em 6 dimens\u00f5es: Conhecimento, Efici\u00eancia, Prestatividade, Empatia, Cortesia e Clareza. Um BTB alto em "Empatia" indica falta de acolhimento; em "Conhecimento", indica informa\u00e7\u00e3o incorreta.',
            },
            {
                'title': 'Comportamentos que geram BTB mesmo com problema resolvido',
                'body': 'O problema pode ter sido resolvido e ainda assim gerar BTB se: o cliente sentiu que foi tratado como um n\u00famero, o encerramento foi frio ou apressado, o CSA usou linguagem defensiva ou rob\u00f3tica, ou o cliente precisou repetir informa\u00e7\u00f5es j\u00e1 fornecidas. Resolu\u00e7\u00e3o t\u00e9cnica n\u00e3o garante TTB \u2014 a experi\u00eancia emocional tamb\u00e9m conta.',
            },
            {
                'title': 'Como o contato estacionado (parked) afeta o CCX?',
                'body': 'Quando um contato \u00e9 estacionado, outro CSA pode finaliz\u00e1-lo \u2014 e o ponto de CCX positivo vai para quem encerrou, n\u00e3o para quem fez o trabalho. Al\u00e9m disso, o cliente que espera sem atualiza\u00e7\u00e3o tem alta chance de avaliar negativamente. Parked% alto impacta tanto a m\u00e9trica individual quanto a do time.',
            },
            {
                'title': 'O que aumenta o TTB de forma consistente?',
                'body': 'Empatia expl\u00edcita no in\u00edcio do contato, uso do nome do cliente, confirma\u00e7\u00e3o clara da resolu\u00e7\u00e3o, encerramento personalizado e tom coerente com o estado do problema. Clientes que sentem que foram ouvidos de verdade \u2014 mesmo quando a solu\u00e7\u00e3o n\u00e3o \u00e9 ideal \u2014 tendem a avaliar positivamente.',
            },
            {
                'title': 'CCX e as outras m\u00e9tricas: como se correlacionam?',
                'body': 'AHT alto nem sempre significa CCX ruim. Transfer\u00eancia excessiva (HRR alto) sim. Recontato (cliente voltando pelo mesmo problema) \u00e9 o maior preditor de BTB. DUR alto indica contatos que demoram porque o CSA n\u00e3o sabe resolver sozinho. Cuidar do CCX indiretamente significa: reduzir recontato, evitar transfer\u00eancias, e encerrar com confirma\u00e7\u00e3o.',
            },
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
        'accordions': [
            {
                'title': 'Por que m\u00faltiplas demandas aumentam o BTB?',
                'body': 'Quando o CSA n\u00e3o organiza explicitamente as demandas, o cliente percebe falta de controle e aten\u00e7\u00e3o. Uma demanda esquecida ou parcialmente tratada \u00e9 suficiente para gerar BTB em "Prestatividade" e "Efici\u00eancia", mesmo que as outras demandas tenham sido resolvidas corretamente.',
            },
            {
                'title': 'Como identificar e priorizar as demandas rapidamente',
                'body': 'Logo no in\u00edcio, liste as demandas em voz alta para o cliente: "Entendi que voc\u00ea tem duas situa\u00e7\u00f5es: [A] e [B]. Vou resolver [A] primeiro e depois [B]." Isso demonstra escuta ativa, organiza o atendimento e reduz o risco de deixar algo para tr\u00e1s. Demanda principal = a mais urgente ou com impacto financeiro.',
            },
            {
                'title': 'Leitura de hist\u00f3rico como ponto de partida',
                'body': 'Antes de qualquer intera\u00e7\u00e3o, leia o hist\u00f3rico de contatos anteriores. Se o cliente j\u00e1 entrou em contato antes sobre o mesmo assunto, mencione: "Vejo que voc\u00ea j\u00e1 nos contactou sobre isso." Isso elimina a necessidade de o cliente repetir tudo, reduz AHT e aumenta a percep\u00e7\u00e3o de qualidade.',
            },
            {
                'title': 'Encerramento com m\u00faltiplas demandas: o checklist mental',
                'body': 'Antes de encerrar, fa\u00e7a internamente: (1) Resolvi a demanda A? (2) Resolvi a demanda B? (3) Confirmei com o cliente que ambas est\u00e3o ok? S\u00f3 ent\u00e3o encerre. Um "Tem mais alguma coisa que eu possa te ajudar?" antes do encerramento garante que nenhuma demanda ficou em aberto.',
            },
            {
                'title': 'Impacto no AHT e como equilibrar',
                'body': 'Contatos com m\u00faltiplas demandas naturalmente t\u00eam AHT maior. Isso n\u00e3o \u00e9 um problema \u2014 \u00e9 esperado. O problema \u00e9 quando o CSA encerra precipitadamente para reduzir o AHT e deixa demandas em aberto, gerando recontato. Um contato mais longo e completo \u00e9 sempre prefer\u00edvel a dois contatos curtos sobre o mesmo problema.',
            },
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
        'accordions': [
            {
                'title': 'O que \u00e9 recontato e por que ele importa?',
                'body': 'Recontato acontece quando o cliente precisa entrar em contato mais de uma vez pelo mesmo problema. \u00c9 o maior preditor de BTB e um dos principais fatores que eleva o AHT m\u00e9dio do time. Ler o hist\u00f3rico antes de come\u00e7ar \u00e9 a forma mais eficaz de evitar que o cliente sinta que est\u00e1 come\u00e7ando do zero.',
            },
            {
                'title': 'Como fazer uma retomada que demonstra contexto',
                'body': 'Uma boa retomada come\u00e7a com: "Vejo que voc\u00ea j\u00e1 nos contactou sobre [X]. Vou continuar de onde paramos." Isso dispensa o cliente de repetir tudo, demonstra que o atendimento anterior foi registrado e cria confian\u00e7a imediata. O cliente que sente continuidade tem muito mais chance de avaliar positivamente.',
            },
            {
                'title': 'Retomada ap\u00f3s pausa longa no chat',
                'body': 'Quando o cliente demora para responder e o chat "esfria", ao retomar use: "Ol\u00e1 [Nome], ainda estou aqui para te ajudar com [X]. Voc\u00ea ainda precisa de assist\u00eancia?" Isso reativa o contato sem constranger o cliente e evita o encerramento prematuro por inatividade.',
            },
            {
                'title': 'Investiga\u00e7\u00e3o antes de a\u00e7\u00e3o: por que \u00e9 cr\u00edtico?',
                'body': 'Diagnosticar antes de agir evita a\u00e7\u00f5es erradas que criam novos problemas. Exemplo cl\u00e1ssico: processar cancelamento sem perguntar o motivo \u2014 o cliente queria trocar, n\u00e3o cancelar. A investiga\u00e7\u00e3o estruturada (perguntas abertas primeiro, fechadas depois) reduz erros de interpreta\u00e7\u00e3o e AHT de corre\u00e7\u00e3o.',
            },
            {
                'title': 'Retomada e AHT: a rela\u00e7\u00e3o inversa',
                'body': 'Um contato bem retomado \u00e9 mais curto. Quando o CSA j\u00e1 sabe o que o cliente precisa (via hist\u00f3rico), economiza minutos de diagn\u00f3stico. Isso significa que investir 30 segundos lendo o hist\u00f3rico pode economizar 3\u20134 minutos de conversa repetitiva. Retomada eficaz reduz AHT e aumenta CCX ao mesmo tempo.',
            },
        ],
    },
    {
        'file': 'Flyer_PagamentoComplexo.html',
        'title': 'Pagamento Complexo & Resolu\u00e7\u00e3o',
        'subtitle': 'Casos de Alta Complexidade Financeira',
        'emoji': '&#x1F50D;',
        'grad': 'linear-gradient(135deg,#c2410c,#f97316)',
        'accent': '#c2410c',
        'desc': 'Alguns casos de pagamento envolvem m\u00faltiplas vari\u00e1veis: KYC pendente, reembolso urgente, conta com restri\u00e7\u00e3o e prazo prometido n\u00e3o cumprido. Esses casos exigem investiga\u00e7\u00e3o estruturada e postura de resolu\u00e7\u00e3o ativa.',
        'accordions': [
            {
                'title': 'KYC: ferramenta de seguran\u00e7a, n\u00e3o de encerramento',
                'body': 'O KYC (Know Your Customer) \u00e9 um processo de verifica\u00e7\u00e3o de identidade para proteger a conta do cliente. Ele nunca deve ser usado para encerrar um contato sem resolver o problema. O fluxo correto: (1) informe o cliente sobre a necessidade de verifica\u00e7\u00e3o, (2) ative o processo, (3) continue tratando a demanda principal paralelamente quando poss\u00edvel.',
            },
            {
                'title': 'KYC com tentativas excedidas: como agir',
                'body': 'Quando o cliente relata que recebeu SMS de "quantidade de tentativas excedida", ele est\u00e1 em um estado diferente do KYC pendente comum. Nesse caso, <b>n\u00e3o</b> envie um novo link de KYC padr\u00e3o \u2014 isso n\u00e3o funcionar\u00e1. A a\u00e7\u00e3o correta \u00e9 parar o envio de links e escalar via canais internos espec\u00edficos para esse estado.',
            },
            {
                'title': 'Reembolso urgente: explorando alternativas',
                'body': 'Quando o cliente declara urg\u00eancia (especialmente em produtos de alimenta\u00e7\u00e3o ou uso imediato), o prazo padr\u00e3o de 3 dias \u00fateis pode n\u00e3o ser suficiente. Nesse cen\u00e1rio, antes de oferecer o prazo padr\u00e3o, explore: h\u00e1 alternativa de cr\u00e9dito imediato? Vale-presente pode ser oferecido? H\u00e1 caminho de escala\u00e7\u00e3o dispon\u00edvel? Mostrar que voc\u00ea tentou alternativas conta muito para o CCX.',
            },
            {
                'title': 'Conta bloqueada por seguran\u00e7a vs. senha esquecida',
                'body': 'S\u00e3o dois fluxos completamente diferentes. <b>Senha esquecida</b> \u2192 redefini\u00e7\u00e3o de senha padr\u00e3o. <b>Conta bloqueada por seguran\u00e7a</b> \u2192 fluxo espec\u00edfico de desbloqueio por seguran\u00e7a. Oferecer redefini\u00e7\u00e3o de senha para uma conta bloqueada por seguran\u00e7a \u00e9 um erro de conhecimento que n\u00e3o resolve o problema e gera recontato.',
            },
            {
                'title': 'Como comunicar prazos sem criar expectativas falsas',
                'body': 'Nunca prometa uma data exata para reembolso em cart\u00e3o. Use: "O prazo \u00e9 de at\u00e9 2 faturas ap\u00f3s o processamento \u2014 pode ser na pr\u00f3xima ou na subsequente, dependendo da data de fechamento do seu cart\u00e3o." Isso \u00e9 preciso, honesto e evita recontato por "o reembolso n\u00e3o caiu na data prometida".',
            },
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
        'accordions': [
            {
                'title': 'O que \u00e9 o DART e quando ele realmente se aplica?',
                'body': 'DART \u00e9 o canal de escala\u00e7\u00e3o para casos que genuinamente exigem expertise fora do escopo do atendimento padr\u00e3o. N\u00e3o \u00e9 uma sa\u00edda para contatos dif\u00edceis. Antes de acionar, pergunte: "Eu consigo resolver isso com as ferramentas que tenho?" Se a resposta \u00e9 sim, resolva. O DART \u00e9 para quando a resposta \u00e9 n\u00e3o.',
            },
            {
                'title': 'O que \u00e9 o DUR e como o DART o afeta?',
                'body': 'O DUR (DART Usage Rate) mede a porcentagem de contatos em que o DART foi acionado. Um DUR alto indica que o CSA est\u00e1 dependendo do DART para resolver situa\u00e7\u00f5es que poderia tratar diretamente. Al\u00e9m disso, contatos com DART t\u00eam AHT m\u00e9dio quase duas vezes maior (18,6 min vs 9,3 min sem DART), impactando diretamente a m\u00e9trica individual.',
            },
            {
                'title': 'DUR e CCX: como se correlacionam?',
                'body': 'Contatos que passam pelo DART desnecessariamente costumam ter CCX mais baixo: o cliente \u00e9 transferido, precisa repetir o problema e aguarda mais tempo. Um CSA com DUR alto tende a ter BTB de "Efici\u00eancia" e "Prestatividade" elevados. Reduzir o DUR e resolver mais na primeira tentativa \u00e9 a combina\u00e7\u00e3o mais eficaz para CCX.',
            },
            {
                'title': 'Casos que parecem DART mas t\u00eam resolu\u00e7\u00e3o direta',
                'body': 'Muitos CSAs acionam o DART em casos de: reembolso com prazo vencido, produto com defeito, reclama\u00e7\u00f5es de entrega e problemas com parceiros. A maioria desses casos tem fluxo de resolu\u00e7\u00e3o direta dispon\u00edvel. Conhecer esses fluxos \u00e9 o principal diferencial de um CSA com DUR baixo.',
            },
            {
                'title': 'SIC antes de transferir: por que \u00e9 obrigat\u00f3rio?',
                'body': 'O SIC (Service Issue Code) deve ser preenchido no momento em que a demanda \u00e9 identificada \u2014 n\u00e3o no final do contato. Transferir para o DART com SIC em branco invalida o registro do contato e prejudica os dados de qualidade do time. Sempre preencha o SIC antes de iniciar qualquer escala\u00e7\u00e3o.',
            },
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
  .card{{background:#fff;border-radius:20px;max-width:700px;width:100%;box-shadow:0 8px 40px rgba(0,0,0,.12);overflow:hidden}}
  .header{{background:{grad};padding:36px 32px 28px;color:#fff}}
  .header-emoji{{font-size:2.8rem;margin-bottom:10px;display:block}}
  .header h1{{font-size:1.75rem;font-weight:800;letter-spacing:-.5px;margin-bottom:6px}}
  .header p{{font-size:1rem;opacity:.88;font-weight:500}}
  .tag{{display:inline-block;background:rgba(255,255,255,.22);border-radius:20px;padding:3px 14px;font-size:.78rem;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-bottom:14px}}
  .body{{padding:28px 32px 20px}}
  .desc{{font-size:1rem;color:#334155;line-height:1.65;margin-bottom:24px}}
  .section-label{{font-size:.72rem;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:{accent};margin-bottom:12px}}
  /* Accordion */
  .accordion{{margin-bottom:24px}}
  .acc-item{{border:1px solid #e2e8f0;border-radius:12px;margin-bottom:8px;overflow:hidden}}
  .acc-btn{{width:100%;background:#f8fafc;border:none;padding:14px 18px;text-align:left;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:.93rem;font-weight:600;color:#1e293b;transition:background .2s}}
  .acc-btn:hover{{background:#f1f5f9}}
  .acc-btn.open{{background:{accent};color:#fff}}
  .acc-arrow{{font-size:.8rem;transition:transform .25s;flex-shrink:0}}
  .acc-btn.open .acc-arrow{{transform:rotate(180deg)}}
  .acc-body{{max-height:0;overflow:hidden;transition:max-height .3s ease,padding .3s ease;padding:0 18px;font-size:.9rem;color:#334155;line-height:1.65;background:#fff}}
  .acc-body.open{{max-height:400px;padding:14px 18px}}
  .footer{{border-top:1px solid #f1f5f9;padding:14px 32px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
  .footer-brand{{font-size:.75rem;color:#94a3b8;font-weight:600}}
  .footer-author{{font-size:.72rem;color:#cbd5e1}}
  @media print{{body{{background:#fff;padding:0}} .card{{box-shadow:none;border-radius:0;max-width:100%}} .acc-body{{max-height:none!important;padding:14px 18px!important}}}}
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
    <p class="section-label">Explore os T\u00f3picos</p>
    <div class="accordion" id="acc">
      {accordion_html}
    </div>
  </div>
  <div class="footer">
    <span class="footer-brand">Amazon CS BR &mdash; Time de Qualidade</span>
    <span class="footer-author">Desenvolvido por {author} &middot; 2026</span>
  </div>
</div>
<script>
document.querySelectorAll('.acc-btn').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var body=this.nextElementSibling;
    var isOpen=body.classList.contains('open');
    document.querySelectorAll('.acc-body').forEach(function(b){{b.classList.remove('open')}});
    document.querySelectorAll('.acc-btn').forEach(function(b){{b.classList.remove('open')}});
    if(!isOpen){{body.classList.add('open');this.classList.add('open')}}
  }});
}});
</script>
</body>
</html>'''

ACC_ITEM = '''      <div class="acc-item">
        <button class="acc-btn"><span>{title}</span><span class="acc-arrow">&#x25BC;</span></button>
        <div class="acc-body">{body}</div>
      </div>'''

os.makedirs(BASE, exist_ok=True)
for fl in FLYERS:
    acc_html = '\n'.join(ACC_ITEM.format(title=a['title'], body=a['body']) for a in fl['accordions'])
    html = FLYER_TPL.format(
        title=fl['title'], subtitle=fl['subtitle'],
        emoji=fl['emoji'], grad=fl['grad'],
        accent=fl['accent'], desc=fl['desc'],
        accordion_html=acc_html,
        author=AUTHOR,
    )
    path = os.path.join(BASE, fl['file'])
    open(path, 'wb').write(html.encode('utf-8'))
    print('OK', fl['file'])

print('Done: %d flyers written' % len(FLYERS))
