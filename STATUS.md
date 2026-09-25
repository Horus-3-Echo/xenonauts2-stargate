# Stav — Xenonauts 2

Aktualizováno: 2026-09-25, Europe/Prague.
Fáze: M0, příprava načtení módu + doložené vstupy pro misi. Zdrojový loader: 0.1.0.
Ruční zaváděcí běhy: 1. Dokončené plánované běhy: 1. Běhy bez pokroku: 0.
Počet se vztahuje na úspěšně uložené kanonické revize; ne na lokální přípravu.
Ruční migrace na GitHub se do plánovaných běhů nepočítá.

- Připraveno: samostatný projekt, loader s logováním, konfigurace a testovací scénář.
- XSG-004A: ověřen datový vstup CreateMissionEffect a samostatné vstupy nasazení/přechodu.
  Přesná vazba mise–tým–kampaň bez letounu a signatury parametrů čekají na cílové DLL/data;
  úkol je BLOCKED, nikoli DONE. Viz docs/XSG-004A-MISSION-ENTRY.md.
- Připraven read-only vyhledávač herních definic; C# loader, manifest a build nastavení beze změny.
- Statická kontrola T00: PASS, python3 tools/check_source.py, exit code 0.
- T00A: PASS, 12 jednotkových testů diagnostického nástroje na syntetických datech, exit code 0.
  Skutečný moddable_content.zip nebyl dostupný; testy nejsou ověřením herního formátu/runtime.
- Kompilace T01: NOT_RUN, hra/SDK a kompilátor nejsou v pracovním prostředí.
- Hra T02–T05: NOT_RUN. Testovaná verze hry: nezjištěna.
- Herní výprava T10–T14: neimplementována.
- GitHub: `Horus-3-Echo/xenonauts2-stargate`, větev `main`, je pracovní autorita.
  Importována poslední verze zdrojového ZIPu v1 včetně prvního plánovaného běhu.
  Záznam migrace: reports/2026-09-25-github-migration.md.
- Nové herní/build protokoly: žádné v načteném zdrojovém ZIPu ani v projektové složce.
- Poslední práce a kontroly: reports/2026-09-25-001.md. Společné zadání v1 beze změny.

Nejbližší práce bez instalace: XSG-007A, konkrétní spouštěče invaze a časového tlaku.
Po zpřístupnění instalace má přednost XSG-001 a T01–T04. Pro dořešení XSG-004A:
skutečná definice CreateMissionEffect, konstruktory parametrů přechodu a volající
nasazení ne-UFO mise v doloženém buildu. Postup získání je v nálezu XSG-004A.
