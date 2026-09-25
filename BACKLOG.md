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
| XSG-011A | BLOCKED | Veřejná část a zdroj exportéru připraveny v docs/XSG-011A-ASSET-EXPORT.md. Doložena řada Unity 2022.3 a rozlišení manifestů po 7.24; loader 0.1.1 vypisuje Application.unityVersion. Přesný runtime/editor, platforma, kanonická adresa assetu a podsložka balíčků čekají na cílovou instalaci. Editorový build/export T20 ani hra T21 neproběhly. |
| XSG-011B | BLOCKED | Import a test vlastní geometrie; po 011A a funkčním M1. |
| XSG-012 | BLOCKED | Opakovatelný testovací instalační balíček a návod; po sestavení a herních testech. |

V aktuálním backlogu nezbývá nezávislý READY krok. Jediná další priorita: XSG-001,
získat verzi/platformu cílové instalace a zpřístupnit prostředí pro build loaderu.
Poté 002/003 a naměření Unity verze. XSG-004A, 007A a 011A obnovit po dodání
nových herních dat nebo konkrétního nového primárního zdroje; neopakovat stejnou rešerši.
Rozšíření dokumentace je hotové jen tehdy, když odstraňuje konkrétní technickou nejasnost.

Kontrola 2026-09-25 / 004: nové vstupy ani výsledky testů nejsou dostupné;
všechny stavy zůstávají beze změny. První běh bez pokroku, nikoli dokončení XSG-001.
Záznam: reports/2026-09-25-004.md. Nezakládat náhradní READY práci jen kvůli běhu.

Kontrola 2026-09-25 / 005: ani vzdálený `main`, čistá pracovní kopie a dostupné
prostředí neposkytly novou konfiguraci, herní knihovny, SDK, kompilátor ani log.
Stavy se nemění; jde o druhý po sobě jdoucí běh bez pokroku. Záznam:
reports/2026-09-25-005.md. Při třetí stejné kontrole bez nového vstupu navrhnout
pozastavení, nikoli vyrábět náhradní úkol nebo opakovat hotové rešerše.

Kontrola 2026-09-25 / 006: nové vstupy XSG-001 ani testovací výsledky nepřibyly;
jde o třetí po sobě jdoucí běh bez pokroku. Záznam:
reports/2026-09-25-006.md. Doporučení: pozastavit plánované běhy, dokud
nebude dostupná skutečná verze/platforma/OS hry, odpovídající DLL a build
prostředí. Projekt ani rozvrh se tímto záznamem automaticky nemění.
