# Stav — Xenonauts 2

Aktualizováno: 2026-09-25, Europe/Prague.
Fáze: M0, příprava loaderu + doložené mechanismy mise a tlaku kampaně. Zdrojový loader: 0.1.0.
Ruční zaváděcí běhy: 1. Dokončené plánované běhy: 2. Běhy bez pokroku: 0.
Počet se vztahuje na úspěšně uložené kanonické revize; ne na lokální přípravu.
Ruční migrace na GitHub se do plánovaných běhů nepočítá.

- Připraveno: samostatný projekt, loader s logováním, konfigurace a testovací scénář.
- XSG-004A: ověřen datový vstup CreateMissionEffect a samostatné vstupy nasazení/přechodu.
  Přesná vazba mise–tým–kampaň bez letounu a signatury parametrů čekají na cílové DLL/data;
  úkol je BLOCKED, nikoli DONE. Viz docs/XSG-004A-MISSION-ENTRY.md.
- Připraven read-only vyhledávač herních definic; C# loader, manifest a build nastavení beze změny.
- XSG-007A: doloženy časová osa, scheduler, fázové projekty, bombardování,
  Doomsday/regionální efekty a omezení úprav obtížnosti při save/load.
  Mapa v docs/XSG-007A-CAMPAIGN-PRESSURE.md; úkol je BLOCKED na skutečných
  klíčích, podmínkách, hodnotách a obsluze z cílových dat/DLL. Žádný odklad
  není implementován. X-D009 vymezuje cílený zásah se zachováním společného času.
- Statická kontrola T00: PASS, python3 tools/check_source.py, exit code 0.
- T00A: PASS, 12 jednotkových testů diagnostického nástroje na syntetických datech, exit code 0.
  Skutečný moddable_content.zip nebyl dostupný; testy nejsou ověřením herního formátu/runtime.
- Audit XSG-007A: primární wiki načtena z git snapshotu; 10 použitých stránek
  identifikováno blob SHA. Doložené typy/pole a odkazy ověřeny proti snapshotu.
- Kompilace T01: NOT_RUN, cílové knihovny a herní/SDK prostředí nejsou dostupné.
- Hra T02–T05: NOT_RUN. Testovaná verze hry: nezjištěna.
- Herní výprava T10–T14: neimplementována.
- GitHub: `Horus-3-Echo/xenonauts2-stargate`, větev `main`, je pracovní autorita.
  Importována poslední verze zdrojového ZIPu v1 včetně prvního plánovaného běhu.
  Záznam migrace: reports/2026-09-25-github-migration.md.
- Nové herní/build protokoly: žádné v aktuálním vzdáleném main; přečteny všechny
  dosavadní reports/. Vstupní SHA: 3fa739f3eb37aa273491d5e3832fa2449fa02160.
- Poslední práce a kontroly: reports/2026-09-25-002.md. Společné zadání v1 beze změny.

Nejbližší práce bez instalace: XSG-011A, ověřitelný postup exportu dočasné brány a verze Unity.
Po zpřístupnění instalace má přednost XSG-001 a T01–T04. Pro dořešení XSG-004A:
skutečná definice CreateMissionEffect, konstruktory parametrů přechodu a volající
nasazení ne-UFO mise v doloženém buildu. Postup získání je v nálezu XSG-004A.
Pro dořešení XSG-007A: konkrétní časové osy/fronty/fázové projekty a původci změn
tlaku; přesný rozsah chybějících dat je v nálezu XSG-007A. Bez nového vstupu
neopakovat již provedený veřejný audit.
