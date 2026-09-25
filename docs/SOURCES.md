# Primární zdroje — ověřeno 2026-09-25

- Loader a názvy API: https://github.com/GoldhawkInteractive/X2-Modding/blob/main/code-skeleton-mod/X2-Example-Mod/X2ExampleModLifecycle.cs
  Blob a5951d723dd402e006b59c6ae352769443a6686a.
- Framework a knihovny: https://github.com/GoldhawkInteractive/X2-Modding/blob/main/code-skeleton-mod/X2-Example-Mod/X2-Example-Mod.csproj
  Blob c76126a927faad0f28c34aa921f4abec67493c7f.
- Manifest a assembly/common: https://github.com/GoldhawkInteractive/X2-Modding/wiki/mod-definition
- Doprovodný návod: https://github.com/GoldhawkInteractive/X2-Modding/wiki/xenonauts-2-tutorial-code
  Text má odlišnosti od projektu, zaznamenané v DECISIONS.md.
- Vstup do dalšího průzkumu: https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-missions
- Strategická vrstva: https://github.com/GoldhawkInteractive/X2-Modding/wiki/x2-101-strategy-screen-systems

Zdrojový kandidát používá veřejně popsaná rozhraní; není výsledkem testu místní instalace.
Herní DLL nejsou součástí projektu.

## Rešerše XSG-004A — 2026-09-25

Primární autor: Goldhawk Interactive. Načten web i skutečné Markdown bajty oficiální
wiki přes její git zdroj. Snapshot wiki: commit
`7232e8b8988496f78de492639c4fce48ca8cc60e`, datum commitu 2026-08-21.
Nejde o verzi hry ani záruku shody s instalací uživatele. Git blob ID níže určují
přesný přečtený obsah; celé stránky se do zdrojového balíčku nekopírují.

| Zdroj | Použitá část | Git blob |
| --- | --- | --- |
| [Research & Engineering Projects](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-adding_projects) | Dokončení výzkumu, příklad UOO-1 Sabotage | `6b0d72bce41bc1582a9bea80fb3b5434b381e539` |
| [Effects Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference) | Typ a pole CreateMissionEffect | `2c8fcf5539b14b96dc3d3a9154a99a9389c53f65` |
| [GameAPI Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/gameapi-reference) | StrikeTeamSystem; tabulka Other Strategy Systems | `7ac2beebf93d268b7e2b7406c13150f7df2b2a87` |
| [High Level Lifecycle](https://github.com/GoldhawkInteractive/X2-Modding/wiki/high-level-lifecycle) | Parametry Strategy ↔ GroundCombat a RequestMoveTo | `b3d61859d4a3f38d2e5e0c3f09994ccfafeec63f` |
| [Event Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference) | StartGroundCombatCommand; neúplný popis payloadu | `e290f3cf20a292cb882222453014bc3f3979770c` |
| [Mission Scripting](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-missions) | §2.4 přenos výbavy, §3.1/3.6 vazba definice a cílů | `eae876392be7bc541b51cd8b0d60b17e1fecf0e3` |
| [Component Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/component-reference) | MissionDefinitionReference a vazby mise | `611a3d2957301c6d9e894b5361e8fd1e604785a7` |
| [Debugging](https://github.com/GoldhawkInteractive/X2-Modding/wiki/debugging) | Logy, parametry spuštění, moddable_content.zip | `a15cf860a84ed36be2204309818c624d720b499b` |

Přečtený veřejný popis neposkytuje kompletní konstruktor parametrů, payload
StartGroundCombatCommand ani úplné schéma CreateMissionEffect. Nedoplňujeme
namespace, datové typy či volací řetězec podle názvů. Souhrnná GameAPI stránka
také není důkaz, že MissionSystem poskytuje veřejnou metodu CreateMission.

## Rešerše XSG-007A — 2026-09-25

Primární wiki znovu načtena přímo přes její git zdroj, HEAD
`7232e8b8988496f78de492639c4fce48ca8cc60e` (2026-08-21). Revize se od XSG-004A
nezměnila; nový je audit spouštěčů kampaně, nikoli tvrzení o novější hře.
Webový čteč stránky neposkytl; rozhodující byly skutečné Markdown bajty
oficiálního wiki repozitáře. Herní data ani DLL tím nebyly získány.

| Zdroj | Nově použitá část | Git blob |
| --- | --- | --- |
| [Strategy Screen Systems](https://github.com/GoldhawkInteractive/X2-Modding/wiki/x2-101-strategy-screen-systems) | Čas, globální tlak, mise a ekonomika | `ba3e753e5aa288a4c56331d217481f8434ccbb58` |
| [Archetypes Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/archetypes-reference) | Timeline, Timing, AlienInvasion, DoomsdayCounter, PoliticalGeoRegion | `7aedaba7200f13496ec94c2680dbe223b4c987e1` |
| [Component Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/component-reference) | Časová osa, fronta, Duration, invazní a tlakové komponenty | `611a3d2957301c6d9e894b5361e8fd1e604785a7` |
| [Effects Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference) | Podmíněné efekty, plánování, posun/rušení úloh, změny tlaku | `2c8fcf5539b14b96dc3d3a9154a99a9389c53f65` |
| [Prerequisites Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/prerequisite-reference) | Datum, interval, dokončený projekt | `f13e36b94b0e58ca71028bcd165e0b1c1342e9c6` |
| [Event Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference) | ClockStepReport, bombardování, StartGameOverCommand | `e290f3cf20a292cb882222453014bc3f3979770c` |
| [Difficulty & Balance](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-difficulty) | Definice/presety, strategické a taktické nastavení | `e85818b95ade2ebba801e896da7eef2f4c4f8d73` |
| [Technical Design](https://github.com/GoldhawkInteractive/X2-Modding/wiki/technical-design) | DifficultyConfigSystem API, inicializace po load, serializace/výjimky | `411e78eb0123f083d6671f61b083ee6bcb606cda` |
| [GameAPI Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/gameapi-reference) | DoomsdayCounterSystem uvádí účel a počet metod, nikoli signaturu | `7ac2beebf93d268b7e2b7406c13150f7df2b2a87` |
| [Research & Engineering Projects](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-adding_projects) | ProjectPq, skryté fázové projekty, Finished/EntryEffects | `6b0d72bce41bc1582a9bea80fb3b5434b381e539` |

Zkontrolován úplný strom [oficiálních příkladů](https://github.com/GoldhawkInteractive/X2-Modding/tree/2214d043e35e56c0cdb02bf83ce08645b029b648/example-mods)
na commitu `2214d043e35e56c0cdb02bf83ce08645b029b648`; obsahové příklady jsou
krytí a zdraví MARS. Konkrétní data úvodní invaze v tomto stromu nejsou.
Nález a jeho hranice: [XSG-007A-CAMPAIGN-PRESSURE.md](XSG-007A-CAMPAIGN-PRESSURE.md).
