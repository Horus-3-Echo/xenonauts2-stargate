# Stav — Xenonauts 2

Aktualizováno: 2026-09-25, Europe/Prague.
Fáze: M0, příprava loaderu, doložené mechanismy mise/tlaku a export grafiky.
Zdrojový loader: 0.1.1, nesestavený.
Ruční zaváděcí běhy: 1. Dokončené plánované běhy: 3. Běhy bez pokroku: 0.
Počet platí až po úspěšném uložení commitu obsahujícího report 003.
Dokončení rozpracovaného běhu se počítá jednou; bootstrap a migrace se nepočítají.

- Připraveno: samostatný projekt, loader s logováním, konfigurace a testovací scénář.
- XSG-004A: doložen CreateMissionEffect a oddělené vstupy nasazení/přechodu.
  Vazba mise–tým–kampaň bez letounu a signatury čekají na cílové DLL/data;
  BLOCKED, viz docs/XSG-004A-MISSION-ENTRY.md.
- Read-only vyhledávač definic a jeho syntetické testy jsou beze změny.
- XSG-007A: doložena veřejná mapa časové osy, scheduleru, fází a tlaku.
  BLOCKED na skutečných klíčích, podmínkách a obsluze z cílových dat/DLL.
  Odklad invaze není implementován; viz docs/XSG-007A-CAMPAIGN-PRESSURE.md.
- XSG-011A: docs/XSG-011A-ASSET-EXPORT.md + editorový zdroj
  tools/unity/Editor/XsgBundleExport.cs. Doloženo exportní API a rozlišení
  manifestů; přesná instalace/editor a X2 adresy neověřeny. Stav BLOCKED.
- Loader 0.1.1 přidává [XSG] unity-version pomocí Application.unityVersion.
  Žádný runtime patch ani nová závislost; framework a cesty DLL se nemění.
  Verze aktualizována současně v projektu, manifestu a build postupu.
- T00: PASS, python3 tools/check_source.py, exit 0. Jen struktura, JSON a XML.
- T00A: PASS, 12/12 syntetických testů vyhledávače, exit 0. Nejde o test
  exportéru, C# loaderu, skutečných herních dat ani runtime hry.
- Audit XSG-011A: oficiální wiki HEAD znovu ověřen, pět použitých wiki
  blobů identifikováno v docs/SOURCES.md; rozhraní Unity porovnána
  s dokumentací 2022.3. Není to důkaz kompatibility cílové instalace.
- T01–T05 a T10–T14: NOT_RUN. Není dostupný C# kompilátor/SDK, cílové
  knihovny ani hra. Testovaná verze hry: nezjištěna.
- T20 (Unity export) a T21 (indexace/zobrazení v X2): NOT_RUN.
  Unity Editor není dostupný; nevznikl AssetBundle ani model instalovaný ve hře.
- Herní expedice, extrakce, trvalá odměna a odklad invaze nejsou implementované.
- Jediná pracovní autorita: Horus-3-Echo/xenonauts2-stargate, main.
  Vstupní SHA: fabc79de128068abdc0881cda09d49655b727488.
  Načteno 25 vzdálených souborů; bajty ověřeny proti Git blobům.
- Nové build/herní protokoly: žádné ve vzdáleném main; přečteny všechny reports/.
  Obnovený místní návrh porovnán s tímto vzdáleným základem, nikoli použit jako autorita.
- Poslední práce: reports/2026-09-25-003.md. Společné zadání v1 beze změny.

V backlogu nezbývá nezávislý READY krok. Jediná další priorita: XSG-001 —
získat verzi/build, platformu a větev instalace, poté zajistit build prostředí
pro loader dle BUILD.md. Přesná Unity verze bude naměřena jeho logem.
Bez těchto vstupů neopakovat stejnou rešerši jako nový pokrok. Běh 003 přinesl
nové zdroje/nález; hranice tří běhů bez pokroku zatím nebyla dosažena.
