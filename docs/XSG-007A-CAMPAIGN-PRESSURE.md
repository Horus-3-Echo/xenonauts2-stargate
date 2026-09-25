# XSG-007A — spouštěče invaze a časového tlaku

Ověřeno 2026-09-25 proti oficiální wiki Goldhawk Interactive, commit
`7232e8b8988496f78de492639c4fce48ca8cc60e`. Přesné revize stránek jsou v
[SOURCES.md](SOURCES.md#rešerše-xsg-007a--2026-09-25).
Jde o doloženou mapu mechanismů, nikoli o odloženou invazi. **XSG-007A zůstává
BLOCKED** na identifikaci skutečných spouštěčů v cílových datech/DLL.

## Výsledek, který mění další postup

Strategický tlak nemá v přečtených podkladech jeden doložený vypínač. Časové
podmínky, fronta událostí, dokončení projektů a změny globálních/regionálních
hodnot mají samostatná rozhraní. Z toho odvozujeme, že samotná úprava rychlosti
Doomsday není důkazem odkladu misí, bombardování ani příběhových událostí.
Zastavení společného času zase není vhodným řešením pro fungující SGC s výzkumem
a léčením. To je návrhový závěr z mapy níže, nikoli výsledek testu hry.

## Mapa závislostí

Šipky vyjadřují dokumentovanou funkci mechanismu. Nejde o zjištěný call stack
první invazní vlny. Poslední sloupec uvádí chybějící vazbu na konkrétní kampaň.

| Vstup / podmínka | Doložená návaznost | Co ještě musí určit cílová instalace |
| --- | --- | --- |
| Krok strategického času | `ClockStepReport` → vyhodnocování archetypu `Timeline`; `PqClockStepEffect` větví efekty podle podmínky. [Události](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference#time-and-clock-events), [archetyp Timeline](https://github.com/GoldhawkInteractive/X2-Modding/wiki/archetypes-reference#timeline), [efekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference). | Která časová osa obsahuje invazní větev; její klíč, datum/interval, `Active`, `Repeatable` a chování při nesplněné podmínce. |
| Datum nebo pravidelný interval | `GeoscapeDateTimeRangePq` / `GeoscapeDateTimeIntervalPq` testují čas; mohou sloužit jako podmínka efektů. [Podmínky](https://github.com/GoldhawkInteractive/X2-Modding/wiki/prerequisite-reference). | Skutečné místo použití, časová základna a hodnoty. Není doloženo, že každá invazní vlna používá právě tyto podmínky. |
| Naplánovaná úloha | `ScheduleTaskEffect` → geoscape scheduler; `DeltaOffsetScheduledTask` mění její čas a `UnScheduleTaskEffect` odstraňuje úlohu podle taxonomie. [Efekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference), [Timing](https://github.com/GoldhawkInteractive/X2-Modding/wiki/archetypes-reference#timing-1). | Přesný `Taxonomy`, vlastník fronty, formát `Task`, registrátor, opakování a případné nové naplánování při načtení. Nezaměňovat tento klíč s `Key` časové osy. |
| Dokončený projekt / příběhová fáze | `ProjectPq` kontroluje stav projektu; `ProjectStateMachineComponent` má efekty při vstupu do `Finished`. Doloženým příkladem je vytvoření mise výzkumem UOO-1 Sabotage. [Projekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-adding_projects). | Které skryté fázové projekty řídí úvod kampaně a které zároveň odemykají výzkum. Doklad o Phase 4 neurčuje spouštěč první invaze. |
| Vytvoření hrozby | `CreateMissionEffect` vytvoří misi, `CreateActivityEffect` aktivitu na misi. `TriggerOrbitalBombardmentCommand` je samostatný příkaz pro bombardování; `OrbitalBombardmentSystem` je registrovaný strategický systém. [Efekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference), [příkazy](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference#strategy-commands), [systémy](https://github.com/GoldhawkInteractive/X2-Modding/wiki/x2-101-strategy-screen-systems#regional-and-global-management). | Konkrétní definice, volající a obsluha; není doložen řetězec „CreateMissionEffect vždy vytvoří UFO“ ani vazba všech těchto vstupů na stejný časovač. |
| Doomsday | `DoomsdayCounterSystem` počítá denní modifikátor. Obtížnost nastavuje počáteční hodnotu a sazbu; `DeltaDoomsdayCounterMissionEffect` může měnit hodnotu výsledkem mise. [GameAPI](https://github.com/GoldhawkInteractive/X2-Modding/wiki/gameapi-reference#other-strategy-systems), [obtížnost](https://github.com/GoldhawkInteractive/X2-Modding/wiki/technical-design#available-difficulty-settings), [efekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference). | Všichni zapisovatelé, znaménka změn, mezní hodnoty a skutečná podmínka porážky. Nulová sazba sama nedokládá zastavení ostatních zápisů. |
| Regiony, finance a ukončení kampaně | Doloženy efekty změn regionálních vztahů, `RegionalRelationsSystem`, `FundingSystem`, archetyp `PoliticalGeoRegion` a `StartGameOverCommand`. [Efekty](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference), [archetypy](https://github.com/GoldhawkInteractive/X2-Modding/wiki/archetypes-reference#georegions), [události](https://github.com/GoldhawkInteractive/X2-Modding/wiki/event-reference#mission-and-objective-events). | Které ignorované mise či lhůty způsobují pokles vztahů/příjmů; skutečné porážkové podmínky. Existence `StartGameOverCommand` nedokládá, který ukazatel jej spouští. |

## Přesné doložené typy a pole pro následný audit

Následující názvy jsou přepsány z referencí; nejde o kompletní schéma JSON.
Typy/defaulty polí, konstruktor a metoda provedení efektu nejsou těmito tabulkami
ověřeny. Záměrně neobsahují připravený patch s vymyšlenými hodnotami.

| Klíč | Typ v primárním zdroji | Relevantní doložená pole |
| --- | --- | --- |
| `PqClockStepEffect` | `Strategy.Data.EntityEffects.PrerequisiteClockStepEffect` | `Key`, `Active`, `Repeatable`, `ClockStep`, `Prerequisite`, `SuccessEffects`, `FailureEffects` |
| `ScheduleTaskEffect` | `Xenonauts.Strategy.Data.EntityEffects.ScheduleTaskEffect` | `Taxonomy`, `Task` |
| `DeltaOffsetScheduledTask` | `Xenonauts.Strategy.Data.EntityEffects.DeltaOffsetScheduledTask` | `Taxonomy`, `Operation`, `Delta` |
| `UnScheduleTaskEffect` | `Xenonauts.Strategy.Data.EntityEffects.UnScheduleTaskEffect` | `Taxonomy` |
| `GeoscapeDateTimeIntervalPq` | `Xenonauts.Strategy.Data.Prerequisites.GeoscapeDateTimeIntervalPrerequisite` | `Modifiers`, `Base`, `Offset`, `Interval`, `TriggerAtStart`, `Variant` |
| `GeoscapeDateTimeRangePq` | `Xenonauts.Strategy.Data.Prerequisites.GeoscapeDateTimeRangePrerequisite` | `Modifiers`, `Min`, `Max`, `InclusiveMin`, `InclusiveMax`, `Randomize`, `Variant` |
| `ProjectPq` | `Xenonauts.Strategy.Data.Prerequisites.ProjectPrerequisite` | `Project`, `Status`, `Variant` |
| `CreateActivityEffect` | `Xenonauts.Strategy.Data.EntityEffects.CreateActivityEffect` | `Key`, `TemplateRef`, `Resources` |
| `DeltaDoomsdayCounterMissionEffect` | `Strategy.Data.DeltaDoomsdayCounterMissionEffect` | `_value`, `Value`, `IsVisible`, `Tags` |

Namespace začínající pouze `Strategy` neopravovat automaticky na `Xenonauts.Strategy`.
Zdroje: [Effects Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/effect-reference)
a [Prerequisites Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/prerequisite-reference).

Pro identifikaci vlastníků stavu jsou doloženy tyto komponenty:

- `Xenonauts.Strategy.Components.AlienInvasionTag` a
  `Xenonauts.Strategy.Components.MissionSpawnCategoryBookkeepingComponent` tvoří
  povinné komponenty singletonu `AlienInvasion`. Jeho existence není přepínač
  „invaze zapnuta“; nemažeme jej jako náhradu cíleného odkladu.
- `Xenonauts.Strategy.Components.TimelineComponent` obsahuje seznam `IEntityEffect`.
  Archetyp `Timeline` zahrnuje také `ActiveComponent`, `TimelineMetaComponent`
  a `TimelineCounterComponent`.
- `Xenonauts.Strategy.Components.MainBase.GeoscapeSchedulerComponent` uchovává
  scheduler; `GeoscapeScheduleTargetComponent` ve stejném namespace uvádí
  `Target`, `Key`, `ScheduledTask`. `DurationComponent` tam uvádí `current`,
  `target`, `active`; `TimerActivity` je aktivita s touto komponentou.
- `Xenonauts.Strategy.Components.DoomsdayCounter` a `RegionalRelations` jsou
  rozsahové komponenty. Číselné meze konkrétní kampaně v referenci uvedeny nejsou.

Zdroj: [Component Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/component-reference)
a [Archetypes Reference](https://github.com/GoldhawkInteractive/X2-Modding/wiki/archetypes-reference).

## Obtížnost není globální vypínač invaze

[Difficulty & Balance](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-difficulty)
dokládá adresář šablon `template/common/difficulty/`, definice v `setting/` a
presety v `config/`. Jde o cesty obsahového balíku, nikoli o lokální instalaci.
`starting_doomsday_counter` a `doomsday_counter_modifier` mají typ `Single`.
`mission_timers` má typ `Integer` a upravuje limity kol v taktice; není to časovač
strategické invaze. Žádnou konkrétní číselnou hodnotu nyní nenastavujeme.

[Technical Design](https://github.com/GoldhawkInteractive/X2-Modding/wiki/technical-design#gameapi-methods)
dokládá metody `DifficultyConfigSystem.ExportActiveDifficultyConfig()` (výsledek
`IReference<Template>`), `ApplyDifficultySettingsToTarget(Entity)` a
`RevertDifficultySettingsToTarget(Entity)`. U posledních dvou zde není uveden
návratový typ ani úplná C# signatura. Nejde o doložené API pro pozastavení invaze.
Souhrnná GameAPI tabulka uvádí u `DoomsdayCounterSystem` počet metod, ale název
metody pro výpočet sazby neuvádí; nevymýšlíme tedy Harmony patch na její název.

Aktivní konfigurace obtížnosti podle dokumentace přetrvává v pozicích.
`StrategyDifficultyConfigSystem` při načtení znovu vyvolá
`DifficultyInitializationReport`; aplikované změny sleduje
`DifficultyModifiedComponent`. Budoucí přepnutí úvod/obrana Země proto musí
ověřit i načtenou pozici a opakovanou inicializaci. Pouhá úprava výchozího presetu
neprokazuje změnu již rozehrané kampaně.
[Save/Load](https://github.com/GoldhawkInteractive/X2-Modding/wiki/technical-design#saveload-event-lifecycle).

## Konkrétní mezery před implementací XSG-007B

V tomto běhu nejsou dostupné cílové herní šablony, DLL ani build/test protokol.
Prošel jsem také strom veřejného repozitáře X2-Modding na commitu
`2214d043e35e56c0cdb02bf83ce08645b029b648`: ukázky obsahují krytí a zdraví MARS,
nikoli definice úvodní invaze. Následující vstupy tedy nelze získat opakováním
téže wiki rešerše.

1. V konkrétním buildu propojit první nežádoucí misi a bombardování s jejich
   původcem: položka skutečného obsahového archivu, hash, JSON Pointer, vyřešený
   `Parent`, podmínka, efekty a odkazovaná definice. Zaznamenat skutečné klíče
   časové osy/fronty a fázové projekty. Názvy souborů podle účelu neodhadovat.
2. Stejným způsobem určit všechny zdroje změn Doomsday a vztahů, časované
   neúspěchy a podmínky ukončení. U každého uvést hodnotu, interval, případné
   obtížnostní modifikátory a příslušnou fázi. Stávající
   `inspect_mission_content.py` hledá pouze `CreateMissionEffect`; negativní
   nález tímto nástrojem není audit časové osy ani invaze.
3. Z DLL získat úplné signatury a volající/obsluhu nalezené větve, zejména
   vyhodnocení časové osy, scheduleru a bombardování. Ověřit, zda zavřená
   podmínka událost odloží, spotřebuje, nebo vyvolá `FailureEffects`, a zda
   odemčení po mnoha dnech nevytvoří všechny zmeškané události najednou.
4. Ověřit serializaci konkrétního stavu fronty, počítadel a budoucího přepnutí
   fáze. Dokumentace obecného ECS save nezaručuje uložení každé komponenty:
   existují vyloučené i podmíněně serializované komponenty a obnova ze šablon.
   Předat jen zjištění, identifikátory a potřebné krátké výřezy; DLL, celý herní
   archiv, lokální cesty a pozice nepatří do zdrojového repozitáře.

Následná implementace má cílit na doložené původce hrozeb a umožnit jejich
pozdější obnovení. `TimelineSystem`, společný čas, výzkum, léčení, financování
a letecké systémy nesmí být plošně odstraněny. Přesný způsob přepnutí a návratu
událostí se zvolí až podle uvedených dat; nepřidáváme nový runtime framework.

## Stav ověření

Veřejný nález: doložené typy, pole a závislosti; konkrétní spouštěče cílové hry
stále chybí. Loader 0.1.0, manifest, framework a DLL reference jsou beze změny.
Kompilace i T14: **NOT_RUN**. Není sestavená implementace odkladu, proto nyní
nepožadujeme herní test. Budoucí T14 musí dostat přesný ovladač fáze a měřený
interval z implementace; ověří odklad i obnovení po načtení, pokračující výzkum
a léčení a nepřítomnost duplicit či návalu zmeškaných událostí. Samotný screenshot
prázdné mapy bez záznamu skutečného stavu spouštěčů nebude důkazem.
