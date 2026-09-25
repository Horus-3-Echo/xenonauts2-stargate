# Jediný backlog Xenonauts 2

| ID | Stav | Úkol a podmínka dokončení |
| --- | --- | --- |
| XSG-000 | DONE | Založit startér, ověřit formáty a trvale uložit zdroje. |
| XSG-001 | BLOCKED | Zapsat skutečnou verzi hry/platformu/OS/cesty; čeká na instalaci uživatele. |
| XSG-002 | BLOCKED | Načtení manifestu: mód je vidět ve hře; závisí na 001. |
| XSG-003 | BLOCKED | Sestavit loader a doložit log nové i načtené kampaně; zdroj připraven, chybí knihovny/kompilátor/hra. |
| XSG-004A | BLOCKED | Veřejná část doložena 2026-09-25: CreateMissionEffect, LaunchStrikeTeam a parametry přechodu; viz docs/XSG-004A-MISSION-ENTRY.md. Zbývá z cílových DLL/dat ověřit spojení mise–tým–kampaň bez letounu, konstruktor/volající přechodu a skutečnou definici; není to hotová výprava. Připraven cílený vyhledávač, T00A PASS 12/12. |
| XSG-004B | BLOCKED | Implementovat nejmenší pokus spuštění mise; nejdříve 003 a doložený 004A. |
| XSG-005 | BLOCKED | Přenos a návrat správných čtyř vojáků včetně výbavy a zranění; po 004B. |
| XSG-006 | BLOCKED | Artefakt, extrakce, ústup a neúspěch, T10–T12; po 005. |
| XSG-007A | BLOCKED | Veřejná mapa doložena 2026-09-25 v docs/XSG-007A-CAMPAIGN-PRESSURE.md: časová osa, scheduler, fázové projekty, bombardování, Doomsday a regionální tlak. Ověřeny typy/pole i omezení obtížnosti a save/load. Z cílových dat/DLL zbývá určit skutečné klíče, podmínky, zapisovatele, meze a obsluhu úvodních hrozeb; nejde o implementovaný odklad. |
| XSG-007B | BLOCKED | Cíleně odložit doložené spouštěče a ověřit T14 včetně obnovení obrany Země po save/load bez duplicit a návalu zmeškaných událostí; po dořešení 007A a fungujícím loaderu. Zachovat společný čas, výzkum, léčení a letecké systémy (X-D009). |
| XSG-008 | BLOCKED | Uložení/načtení a jednorázové přiznání výsledku, T13; po 006. |
| XSG-009 | BLOCKED | Vyhodnotit technickou proveditelnost na skutečných důkazech. |
| XSG-010 | BLOCKED | Artefakt odemkne testovací výzkum/adresu; po 008. |
| XSG-011A | READY | Určit verzi Unity a ověřitelný exportní postup pro jednoduchou vlastní bránu. |
| XSG-011B | BLOCKED | Import a test vlastní geometrie; po 011A a funkčním M1. |
| XSG-012 | BLOCKED | Opakovatelný testovací instalační balíček a návod; po sestavení a herních testech. |

Nejbližší nezablokovaná práce: 011A. XSG-004A a 007A obnovit po dodání nových
herních dat nebo konkrétního nového primárního zdroje; neopakovat stejnou rešerši.
Po zpřístupnění instalace mají přednost 001 → 002/003 a potvrzení loaderu.
Rozšíření dokumentace je hotové jen tehdy, když odstraňuje konkrétní technickou nejasnost.
