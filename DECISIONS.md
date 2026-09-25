# Rozhodnutí

- 2026-09-25 / X-D001: samostatný projekt Xenonauts 2, společné zadání v1.
- X-D002: do založení vzdáleného repozitáře je autoritou verzovaný zdrojový ZIP.
  Důvod: připojené GitHub rozhraní umí práci se soubory, ale nevytváří repozitáře.
- X-D003: kandidát cílí netstandard2.1 podle upstream csproj, blob
  c76126a927faad0f28c34aa921f4abec67493c7f. Textový návod uvádí .NET 4.8.
  Ověřit proti uživatelově buildu; nepovažovat rozpor za vyřešenou kompatibilitu.
- X-D004: knihovna se po sestavení umisťuje do assembly/common podle novějšího
  Mod Definition a build šablony. Starý tutorial zmiňuje DLL vedle manifestu.
- X-D005: první kód pouze loguje životní cyklus. Nemění kampaň ani stav pozic.
  Napojení expedice musí být samostatný doložený experiment.
- 2026-09-25 / X-D006: pro expedici zachovat nativní přenos kampaně do taktiky
  a zpět. CreateMissionEffect je doložený vstup pro vytvoření mise, nikoli hotový
  spouštěč brány. LaunchStrikeTeam bez známé vazby na misi ani samostatné
  -startScreen=GroundCombat neprokazují návrat správných vojáků. Neimplementovat
  propojení odhadem a neklonovat hráčův tým jako anonymní nové jednotky.
  Podklady a přesné mezery: docs/XSG-004A-MISSION-ENTRY.md.
- X-D007: UOO-1 Sabotage používat pouze jako primárně doložený příklad vytvoření
  mise výzkumem. Nepřebírat jeho pozdní příběhové podmínky do první planety.
  X-D003/004 zůstávají nevyřešené vůči cílové instalaci; žádná změna frameworku,
  DLL cesty ani runtime závislostí v tomto běhu.
- 2026-09-25 / X-D008: po založení repozitáře uživatelem přejít na
  `Horus-3-Echo/xenonauts2-stargate`, větev `main`, jako jedinou pracovní autoritu.
  Toto nahrazuje dočasné X-D002. Přenést poslední ZIP v1 včetně prvního běhu;
  starý ZIP dále nerozvíjet. Zachovat oddělení projektů a zadání v1.
