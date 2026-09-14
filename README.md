# 🎮 Jogos de Treinamento — CS Ops VAR BR

**Jogos_Treinamento** is a library of single-file, offline-first browser games, quizzes, reference "flyers," and an internal authoring toolkit, built to train customer-service agents (and team leaders) on the main operational topics of a support operation: AHT, quality, DART escalation, transfers, and order-tracking (WISMO) investigation. Every game is a standalone HTML file — no build step, no backend, no installation. Most games also have a matching one-page visual reference ("flyer") and a **team-mode ("Equipe")** version meant to be played together as a group, e.g. projected during a training session.

> ⚠️ **Disclaimer:** This is an unofficial, community-built training package. It is **not** an official Amazon product. All content is in Brazilian Portuguese (pt-BR) and reflects internal workflows/metrics of a specific support operation (CS Ops VAR BR); some figures (e.g. audit results, weekly stats) are operation-specific and should be updated or removed before reuse elsewhere.

---

## Folder structure

```
Jogos_Treinamento/
├── AHT/                  — Average Handle Time training
├── CCX_Qualidade/        — Quality & CDC (consumer law) training
├── DUR_DART/             — DART escalation decision training
├── HRR_Transferencias/   — Transfer-rate (HRR) training
├── SIC/                  — Closing-code / order-investigation training
│   └── WISMO/            — Chat-based WISMO simulator
└── TIME/                 — Team-mode games, flyers, and generator scripts
```

### AHT — Average Handle Time

| File | What it is |
|---|---|
| `Jogo_AHT_Operacao.html` | **"Operação AHT: Caso Arquivado"** — a detective-style mystery game. The support center's metrics are dropping and the trainee (playing a "service detective") must solve 15 phases to find out why, with a HUD, lives, and phase counter. |
| `Jogo_AHT_Operacao_F6-10.html` | Continuation of the mystery — phases 6–10, introducing classification puzzles, real call sequences, and chained challenges. |
| `Jogo_AHT_v8_SIGMA7.html` | An updated/alternate build of the "Operação AHT" mystery game (same premise, revised content/logic). |
| `Jogo_AHT_Time.html` | A straightforward 35-question practical quiz with real day-to-day scenarios for reducing AHT on both Chat and Phone, without sacrificing quality. |

### CCX_Qualidade — Quality & consumer law

| File | What it is |
|---|---|
| `Jogo_QualidadeCS_v2.html` | A 42-question quiz **based on a real quality audit of 39 contacts** (Jul 2026) — tests recognition of what auditors flag as good/bad practice. |
| `Jogo_ClienteDificil_CDC.html` | A challenge game on handling difficult customers while staying compliant with Brazil's Consumer Defense Code (CDC). |
| `Jogo_Encerramento_v1.html` | A game focused on closing contacts with quality (clear resolution, correct wrap-up steps). |
| `Jogo_Pagamentos.html` | A scenario game covering payment-related cases (refund methods, timelines, disputes). |
| `Dossie_Pagamento.html` | *Not a game* — a static one-page reference sheet summarizing payment/refund policies (e.g. refund timelines per payment method) as of Aug/2026. |

### DUR_DART — DART escalation

| File | What it is |
|---|---|
| `Quiz_DART.html` | **"DART ou não DART?"** — 35 real-world situations; the trainee decides whether the agent should contact the DART (escalation) team or resolve the case alone. |
| `Jogo_casuisab.html` | *"Encerramento & Múltiplos Problemas"* — a 30-question true/false game on closing contacts with quality and organizing multi-order cases. |
| `Jogo_ejoseago.html` | *"Retomada & Resolução"* — real scenarios about chat pauses, resuming conversations, complex payments, and quality closing. |
| `Jogo_msoarfra.html` | *"Pagamento Complexo & Resolução"* — cases involving coupons, price matching, canceled orders, and high-value situations. |

*(Note: the three `Jogo_*` filenames above use internal case-reference codenames rather than descriptive names — the actual topic of each is shown in the table.)*

### HRR_Transferencias — Transfer rate (HRR)

| File | What it is |
|---|---|
| `Jogo_Transferencias.html` / `Jogo_TransferenciasV2.html` | **"Transfere ou Não? — O Jogo"** — identical decision-training games on when a case should be transferred vs. resolved directly (V2 is a duplicate copy of the same content). |
| `Flyer_Guia_Transferencias.html` | A one-page visual reference poster with real team stats (weekly transfer count, transfer %, HRR vs. target, share of restricted-rule categories). |
| `Email_Transferencias_Pausas.html` | An HTML email/newsletter template communicating transfer and break/pause policy updates to the team. |

### SIC — Closing codes & order investigation

| File | What it is |
|---|---|
| `Simulador_AC3.html` | The full **AC3 console simulator** — a high-fidelity replica of Amazon's internal CS tool with 40 complete case scenarios (order details, chat, resource panel, tabs, policy search, action flows, closing-code selection). See its own detailed README for a full breakdown. |
| `SIC_Detective_JOGO.html` | **"SIC Detective — Arquivo Confidencial"** — a case-file style game: the trainee reviews a case "dossier" and must identify the correct closing code (SIC) that classifies it. |
| `WISMO/Chat_WISMO.html` (= `Chat_WISMO_v6.html`, identical) | A live **chat simulator** focused specifically on WISMO ("Where Is My Order") conversations, with a live timer and scoring — the current/latest version. |
| `WISMO/Chat_WISMO_v5.html` | A previous iteration of the WISMO chat simulator, kept for reference. |
| `WISMO/Chat_WISMO_v3_backup.html` | An older backup from before a round of timer/scoring fixes (see `patch_log.txt`). |
| `WISMO/fix_dupes.py`, `WISMO/patch_timer.py`, `WISMO/patch_log.txt`, `WISMO/test.txt` | Internal maintenance scripts and notes used while iterating on the WISMO chat simulator — **development artifacts, not meant to be opened by trainees.** |

### TIME — Team mode, flyers, and generator scripts

This folder holds **group-play adaptations** of the games above, plus the visual references and the Python scripts used to generate/maintain them.

- **`Jogo_*_Equipe.html`** — "Team mode" versions of the AHT, quality, DART, and transfer games above, restyled for group sessions (e.g. projected on a screen so a team can answer together), each ending with the same credit footer.
- **`Flyer_*.html`** — 10 one-page visual posters, one per topic, meant as quick-reference material or as a companion to the matching game:
  `Flyer_AHT`, `Flyer_ClienteDificil_CDC`, `Flyer_DART`, `Flyer_Encerramento`, `Flyer_Encerramento_Multiplos`, `Flyer_PagamentoComplexo`, `Flyer_Pagamentos`, `Flyer_QualidadeCS`, `Flyer_Retomada`, `Flyer_Transferencias`.
- **Generator scripts** (`gen_flyers.py`, `gen_flyers2.py`, `gen_flyers3.py`, `gen_flyers4.py`, `gen_games.py`, `gen_games2.py`) — Python scripts that programmatically build the flyer and team-mode HTML files from shared templates (title, subtitle, question data, color scheme, etc.), so new topics can be added consistently without hand-writing HTML/CSS each time.
- **Maintenance scripts** (`fix_corujao.py`, `fix_footer.py`) — one-off scripts used to batch-edit the generated files: `fix_corujao.py` scrubs references to a separate internal knowledge-base tool from the team-mode games (replacing them with a generic mention), and `fix_footer.py` updates the credit footer text across all generated HTML files.

> These Python scripts reference a local Windows path (`C:\Users\...\Desktop\Jogos_Treinamento\TIME`) and are authoring tools for whoever maintains this content — they are **not** part of the trainee-facing experience and don't need to be run to use the games.

---

## How it works (technical overview)

- Every trainee-facing file is a **single self-contained HTML file**: vanilla JavaScript, inline CSS, no frameworks, no build step, no external dependencies beyond an occasional Google Fonts import.
- Games follow a consistent pattern: an intro/start screen → a HUD or progress indicator → one question/case at a time → immediate feedback (correct/incorrect + explanation) → a final score/summary screen.
- Some games (the AHT mystery, `SIC_Detective`, `Simulador_AC3`) add a lives/HUD system and multi-step case investigation; others (`Quiz_DART`, `Jogo_AHT_Time`, quality quizzes) are straightforward multiple-choice/true-false quizzes.
- The **Flyer** files are static (non-interactive) styled HTML pages meant to be viewed or printed, not played.
- The **generator scripts** are ordinary Python (no third-party packages beyond the standard library) that emit the HTML files as formatted strings — they are development tooling, run locally by whoever authors new content, not part of the shipped training material.

---

## Getting started

1. Extract the archive.
2. Open any game's `.html` file directly in a modern browser — no installation or server required.
3. For group sessions, use the matching `_Equipe.html` version from `TIME/` and the matching `Flyer_*.html` as a leave-behind reference.
4. `Simulador_AC3.html` and the `WISMO/Chat_WISMO*.html` simulators are the most in-depth items in the set — see the dedicated README for `Simulador_AC3` for a full feature breakdown.

---

## License / usage notes

No license file is currently included. Content is specific to a particular support operation's internal policies, metrics, and terminology (AHT/HRR targets, audit results, team names) — review and adapt before reusing outside that context. The generator scripts (`gen_*.py`, `fix_*.py`) are internal authoring tools and reference local file paths that will need to be updated for any other environment.
