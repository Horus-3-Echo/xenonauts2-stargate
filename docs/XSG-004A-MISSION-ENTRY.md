# XSG-004A — vytvoření mise bez sestřelu UFO

Ověřeno 2026-09-25. Jde o technický nález a diagnostický zdroj, nikoli implementaci
výpravy. Stav úkolu: BLOCKED na přesném propojení v cílové instalaci.
Veřejná dokumentace už poskytla konkrétní vstupy; další opakování stejného hledání
bez nových dat není pokrok. Revize primárních zdrojů jsou v SOURCES.md.

## Co jsme zjistili

Dokumentace dokládá vytvoření strategické mise dokončením výzkumu. Z tohoto
mechanismu odvozujeme kandidátní cestu bez nutnosti nového sestřelu UFO, ne
ověření naší expedice. Příkladem je UOO-1 Sabotage a reference
`capture_resources/capture_resources^uoo1.json`. Jde o relativní referenci uvedenou
v dokumentaci, nikoli zde ověřenou úplnou cestu uvnitř herního balíku. UOO-1 je
pozdní příběhový příklad, **ne zvolená první planeta ani doporučení odemknout fázi 4**.
Zdroj: [Research & Engineering Projects, příklady herních dat](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-adding_projects#examples-from-the-base-game-assets).

**Bez sestřelu UFO není totéž co bez výsadkového letounu.** Odstranění letu,
svázání výpravy se SGC a správný návrat posádky zůstávají neověřené.

| Vrstva | Doložený vstup | Přesná hranice důkazu |
| --- | --- | --- |
| Vytvoření strategické mise | `Xenonauts.Strategy.Data.EntityEffects.CreateMissionEffect`; pole `DefinitionRef`, `SpawnRuleOverride` | [Effects Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference). Neuvádí signaturu provedení efektu ani typy/defaulty obou polí. Nedoplňovat je odhadem. |
| Nasazení již sestaveného týmu | `Xenonauts.Strategy.Systems.StrikeTeamSystem.LaunchStrikeTeam(Entity strikeTeam)` → `void` | [GameAPI Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/gameapi-reference#striketeamsystem). Metoda nemá parametr mise. Samotné zavolání proto nedokazuje přiřazení cíle ani otevření taktické mapy. |
| Další stopa pro sledování volání | `StartGroundCombatCommand` odvozený od `PromiseEvent` | [Event Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference#ground-combat-commands). Payload je popsán jen obecně; namespace, konstruktor a příjemce je nutné zjistit z cílových knihoven. |
| Přechod do taktiky | `StrategyToGCMissionStartParameters` a `ScreenManager.RequestMoveTo(GameScreens.GroundCombat, params)` | [High Level Lifecycle](https://github.com/GoldhawkInteractive/X2-Modding/wiki/high-level-lifecycle#major-screens-and-their-lifecycle). Doložený koncept přechodu, nikoli kompletní C# signatura/volatelný konstruktor. |
| Návrat | `GCToStrategyMissionReturnParameters` | Stejný [popis životního cyklu](https://github.com/GoldhawkInteractive/X2-Modding/wiki/high-level-lifecycle#major-screens-and-their-lifecycle). Je třeba zachovat návrat do téže kampaně; přenos identity a zranění zde nebyl testován. |

Tyto řádky nejsou doložený souvislý call stack. Zejména pořadí nasazení týmu,
přípravy parametrů a odeslání příkazu se musí zjistit, ne poskládat podle názvů.

## Data a závislosti, které nesmíme přeskočit

- Mise má vlastní definici a vazby na účastníky. Dokumentovány jsou
  `Xenonauts.Strategy.Components.Missions.MissionDefinitionReferenceComponent`,
  `Xenonauts.Strategy.Components.MissionParticipantsLink` a
  `Xenonauts.Strategy.Components.MissionCreatorLink`. Jejich existence neurčuje
  bezpečný postup ručního sestavení mise.
  [Component Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/component-reference).
- Inventář hráčových vojáků prochází při přechodu přes
  `CreateCombatantBasedOnStrategyCombatantData()`, `EquipLoadoutFrom()` a
  `TranslateToGCItem()`. Nový typ mise se váže na konfiguraci cílů přes
  `MissionDefinition.GenerateGCStateConfiguration()` a `ObjectiveConfig.Spawn(Entity gcMission)`.
  [Mission Scripting, §2.4 a §3.1](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-missions).
- Návrhový důsledek pro XSG: tým vybírat z existující kampaně, nevytvářet čtyři
  nové taktické figurky a následně je nepřepisovat do seznamu vojáků. Zachovat
  nativní cestu přenosu, dokud testy neukážou konkrétní potřebu zásahu.
- Závislosti pro další pokus: známý build hry, ověřený loader (XSG-003), skutečná
  definice mise, platná mapa a účastníci, vazba na výchozí kampaň/SGC. Nová runtime
  knihovna není pro tento nález potřeba. .NET a umístění DLL z X-D003/004 se nemění.

## Cílené zjištění zbývajících dat

Připravený `tools/inspect_mission_content.py` čte **jen zadaný ZIP** a vypíše
nálezy na standardní výstup. Nerozbaluje, nemění soubory, nespouští DLL, nevolá síť.
Potřebuje Python 3; nejde o závislost instalovaného módu.

Z kořene projektu:

```text
python tools/inspect_mission_content.py "CESTA_K_MODDABLE_CONTENT_ZIP"
```

Zástupný argument nahraď skutečným souborem z konkrétní instalace. Dokumentace
uvádí herní `moddable_content.zip`; dostupnost a umístění v cílovém buildu nejprve
ověřit. [Debugging, práce s interními šablonami](https://github.com/GoldhawkInteractive/X2-Modding/wiki/debugging#tips-for-efficient-debugging).

Výstup obsahuje přesný název položky ZIPu, SHA-256 jejích bajtů, JSON Pointer,
oba přítomné typové klíče, nalezená pole a zobrazení hodnot dvou polí efektu.
Název příkladu UOO-1 hledá v archivu bez domýšlení adresářů. Chybějící pole
označuje jako nepřítomná; nedosazuje implicitní hodnoty. Hodnoty v
`field_value_displays` jsou znovu formátované diagnostické řetězce, nikoli
byte-identické zdroje nebo hotová herní konfigurace.

Návratové kódy: 0 = nalezen efekt bez chyby čtení; 1 = nenalezen rozpoznaný
efekt; 2 = chyba/částečné čtení. Ani kód 0 neznamená kompatibilitu hry. Při 1/2
nelze uzavřít, že hra efekt nepodporuje: jiný alias či JSON rozšíření mohou
vyžadovat ruční prohlídku. Limity čtení: 16 MiB/položku a 512 MiB celkem.
Testy používají pouze syntetická data, nikoli skutečný herní ZIP.

Po zpřístupnění instalace získat tyto konkrétní důkazy:

1. Verzi/build, platformu a větev; přednost má úspěšné T01–T04 podle BUILD.md.
2. Výstup vyhledávače a lokálně přečtené nalezené efekty v kontextu jejich
   `EntryEffects`. Ověřit jejich přesný `DefinitionRef` a skutečný formát
   `SpawnRuleOverride`, dědičnost i mapu. Nedávat celý herní obsah do zdrojového ZIPu.
3. Z cílových DLL zjistit konstruktory, členy a volající
   `StrategyToGCMissionStartParameters`, `StartGroundCombatCommand` a provedení
   `CreateMissionEffect`. Sledovat jedno původní nasazení mise bez UFO:
   kdo propojí čtyři vojáky, misi a výchozí kampaň, kdo zahájí přechod a návrat.
   Přiložit textové signatury a call stack s uvedením buildu, ne herní DLL.
4. Teprve z těchto dat implementovat XSG-004B. Do té doby XSG-004A BLOCKED;
   nezávislá nejbližší READY práce je XSG-007A.

## Oddělení diagnostiky od herního důkazu

Přímé spuštění taktiky přes `-startScreen=GroundCombat` s `-parameters=...`
je dokumentováno, ale potřebuje existující soubor parametrů. Není důkazem
přenosu kampaně ani náhradou uvedené vazby. Žádnou fiktivní adresu parametrů
proto nebalíme do módu. [Debugging, argumenty spuštění](https://github.com/GoldhawkInteractive/X2-Modding/wiki/debugging#other-command-line-arguments).

T05 níže **zatím nelze spustit**: chybí sestavený XSG-004B. Jeho provedení má
následovat až s doloženým ovládáním spouštěče, nikoli s domyšleným tlačítkem:

1. V nové testovací kampani po T01–T04 vyber přesně čtyři vojáky; zaznamenej
   jejich stabilní ID, jména, HP a výbavu. Ulož pozici před výpravou.
2. Jednou aktivuj budoucí doložený spouštěč XSG-004B bez sestřelení UFO.
   Očekávání: právě jedna cílová mise, ti samí čtyři vojáci a stejná výbava.
3. Před prvním tahem zachyť screenshot týmu a log přechodu; uložit a načíst
   taktickou pozici. Poté běžně ukončit/ustoupit a ověřit návrat do původní kampaně.
   Očekávání: žádní duplicitní vojáci, žádná druhá výprava při načtení.
4. Důkazy: build hry/módu, vstupní save, screenshot před/po nasazení, `Player.log`
   s `[XSG]`, při zapnutém souborovém logování také `Logs/output.log` a log
   spouštěče s vazbou mise–tým–kampaň. Přesná cesta logů se ověří pro cílový OS.
   [Debugging, logy](https://github.com/GoldhawkInteractive/X2-Modding/wiki/debugging#log-file-locations).

T05 neuzavírá artefakt, odměnu, zranění ani celou M1; ty mají vlastní T10–T14.
