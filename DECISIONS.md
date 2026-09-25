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
- 2026-09-25 / X-D009: odklad úvodní invaze připravovat jako cílené řízení
  doložených původců hrozeb, nikoli zastavení společného času, plošné odstranění
  TimelineSystem nebo smazání singletonu AlienInvasion. Dokumentace odděluje
  časovou osu, scheduler, projekty a Doomsday/regionální efekty; samotná nulová
  sazba Doomsday neprokazuje odklad ostatních větví. Přesné klíče, obsluha a
  obnovení zatím nejsou známy, proto žádný runtime patch. Budoucí T14 musí
  ověřit i načtení v obou fázích, pokračující výzkum/léčení a jednorázové
  obnovení bez návalu zmeškaných událostí. Nález: docs/XSG-007A-CAMPAIGN-PRESSURE.md.
  X-D003/004 ani společné zadání v1 se nemění; nová runtime závislost nevzniká.
- 2026-09-25 / X-D010: pro XSG-011A oddělit editorový export od runtime loaderu.
  Loader 0.1.1 pouze přidává log Application.unityVersion. Výchozí dokumentovaná
  řada 2022.3 nenahrazuje naměřenou plnou verzi; exportér vyžaduje explicitní
  editor, platformu a ověřené načítací jméno. Pro první pokus požadujeme shodu
  editoru s runtime jako projektové omezení, nikoli prokázanou kompatibilitu.
  Postup s vlastním názvem balíčku podmínit ověřením větve 7.24; zachovat
  kořenový manifest a rozlišovat jej od starého X2 manifestu i výstupů Unity.
  Herní assety později načítat přes X2 ContentManager. Unity Addressables,
  UnityEditor ani další knihovnu do runtime nepřidávat. X-D003/004 beze změny.
