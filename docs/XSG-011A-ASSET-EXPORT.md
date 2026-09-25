# XSG-011A — verze Unity a export dočasné brány

Ověřeno 2026-09-25. Stav: **BLOCKED** na cílové instalaci a Unity Editoru.
Připraven zdroj exportéru, nikoli sestavený AssetBundle nebo herní brána.

## Co je doloženo

| Otázka | Zjištění a primární zdroj | Hranice důkazu |
| --- | --- | --- |
| Řada Unity | Goldhawk uvádí Unity 2022.3 v [Content Manager](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-manager-usage). | Přesný patch uživatelovy hry neznáme. |
| Zjištění runtime | [Application.unityVersion](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Application-unityVersion.html) vrací verzi Unity runtime. Loader 0.1.1 ji vypíše. | Zdroj loaderu není zkompilovaný; žádná hodnota nebyla naměřena. |
| Exportní API | [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) přijímá výstupní adresář, `AssetBundleBuild[]`, možnosti a `BuildTarget`; vrací `AssetBundleManifest`. | Vyžaduje Editor a modul cílové platformy; neprokazuje načtení v X2. |
| Jméno uvnitř balíčku | [AssetBundleBuild.addressableNames](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/AssetBundleBuild-addressableNames.html) dovoluje určit načítací jméno jednotlivého assetu. | Pole vestavěného API není balíček Unity Addressables. Správnou X2 adresu musí dodat ověřený descriptor. |
| Nalezení assetu | [Asset Paths](https://github.com/GoldhawkInteractive/X2-Modding/wiki/asset-structure) rozlišuje pack, typ, screen a jméno. | Neodvozovat celou adresu z pouhého názvu souboru v `Assets/`. |

V [popisu změny 7.24](https://github.com/GoldhawkInteractive/X2-Modding/wiki/content-pack-loading)
Goldhawk dokládá indexování obsahů balíčků a podporu vlastních názvů. Starý
buildový `manifest.json` vedle balíčků se ignoruje; kořenový manifest módu
zůstává povinný. Tato větev postupu platí až po potvrzení odpovídající verze hry.
Starší instrukce z asset-structure proto nepoužíváme jako návod pro 7.24.

Unity `AssetBundleManifest` a jeho výstupní soubory jsou jiná věc než odstraněný
X2 `AssetBundleBuildManifest`. [Unity návod](https://docs.unity3d.com/2022.3/Documentation/Manual/AssetBundles-Building.html)
popisuje také samostatný manifestový bundle pojmenovaný podle výstupního adresáře
a textové `.manifest` soubory. Výstup exportu se nekopíruje celý naslepo do hry.

## Exportér a jeho vstupy

Zdroj: [XsgBundleExport.cs](../tools/unity/Editor/XsgBundleExport.cs).
Patří do `Assets/Editor/` vlastního authoring projektu, ne do herní DLL.
Používá pouze Unity Editor API a standardní C# knihovny. Kontrola existence
prefabu používá [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html).
Samostatné C# skripty v prefabu pro tento pokus nepřidávat; první model má být
statická geometrie s materiálem. Kompatibilitu shaderu musí ověřit hra.

| Parametr `Build` | Požadovaný vstup |
| --- | --- |
| `prefabAssetPath` | Existující importovaný `.prefab` pod `Assets/` authoring projektu. |
| `verifiedAssetName` | Přesné načítací jméno v balíčku, doložené resolverem/descriptorem cílové hry. Exportér jej sám neumí ověřit. |
| `bundleName` | Jedinečný vlastní název malými písmeny s příponou `.assetbundle`; pravidlo tohoto exportéru. |
| `emptyOutputDirectory` | Existující prázdný pracovní adresář mimo herní instalaci a mimo `Assets/`; jiný název než bundle. |
| `expectedUnityVersion` | Plná verze ověřeného Editoru. Pro první pokus volíme shodu s naměřeným runtime; jde o projektové omezení, ne obecnou záruku kompatibility. |
| `targetPlatform` | Explicitní `UnityEditor.BuildTarget` pro skutečnou platformu hry, nikoli automatický odhad podle počítače exportéru. |

## T20 — podmíněný postup exportu, nyní NOT_RUN

1. Podle BUILD.md nejprve doložit build/verzi hry a runtime Unity. Do lokální
   evidence doplnit editor, cílovou platformu, skutečnou adresu prefabu a
   platformní podsložku balíčků. Poslední dvě hodnoty z veřejného popisu nejsou
   pro naši bránu ověřeny; před jejich zjištěním neinstalovat balíček.
2. V odpovídajícím Editoru vytvořit vlastní jednoduchý statický prefab brány,
   uložit jej s jeho geometrií a materiálem. Zkopírovat exportér do `Assets/Editor/`
   a nechat proběhnout kompilaci skriptů. Zachovat případné chyby Console.
3. Z vlastního editorového skriptu zavolat
   `StargateX2.Authoring.XsgBundleExport.Build(prefabAssetPath, verifiedAssetName, bundleName, emptyOutputDirectory, expectedUnityVersion, targetPlatform)`
   s doloženými hodnotami. Výstup zůstává v pracovní složce; exportér nic neinstaluje.
4. Očekáváme nenulový manifest, neprázdný soubor pojmenovaného balíčku a log
   `[XSG-EXPORT]` s verzí, platformou, názvem balíčku a načítacím jménem. Zkontrolovat
   také seznam assetů a závislostí v textovém manifestu; chyba nebo jiný prefab
   znamená FAIL. Uchovat Editor log a manifesty, zaznamenat SHA-256 balíčku.
5. Zopakovat do nového prázdného adresáře. Očekáváme stejný seznam assetů a
   závislostí; bitovou shodu bez měření netvrdíme. Nesprávná verze Editoru a
   neprázdný výstupní adresář musí být odmítnuty před exportem.

## T21 — podmíněná kontrola v X2, nyní NOT_RUN

Vyžaduje T01–T04, T20 a ověřené umístění i propojení assetu (XSG-011B).
Teprve potom vložit pojmenovaný bundle do doložené platformní podsložky
testovacího módu, zachovat kořenový manifest, restartovat hru a povolit mód.
V logu 7.24 hledat souhrn `ContentPackState`: `filesIndexed >= 1`,
`totalAssets > 0`, `filesFailed = 0`. Dodat souhrn i okolní chyby.
Po načtení připravené testovací scény musí být vidět správná geometrie a materiál;
důkazem je screenshot brány a celý relevantní log včetně verze hry a Unity.
Souhrn indexu samotný viditelný prefab ani funkční extrakci nedokládá.
Spouštěč scény ještě nemáme, proto se tento herní test nyní nevyžaduje.

## Zbývající konkrétní vstup

Verze/platforma cílové hry, naměřená plná verze Unity, dostupný odpovídající
Editor s build modulem, kanonické jméno našeho assetu a platformní cesta
z cílového resolveru. Runtime nadále používá vlastní ContentManager X2;
nepřidáváme Unity Addressables ani přímé načítání balíčku v loaderu.
Přesné revize primárních podkladů jsou v [SOURCES.md](SOURCES.md).
