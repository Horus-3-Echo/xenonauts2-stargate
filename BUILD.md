# Sestavení a první test Xenonauts 2

Zde nebyla provedena kompilace ani spuštění hry. Cílová verze instalace je neznámá.
Aktuální upstream csproj používá netstandard2.1; starší text návodu uvádí .NET 4.8.
Pro tento kandidát volíme netstandard2.1 podle skutečné šablony. Potvrzení poskytne
až kompilace proti knihovnám konkrétní hry; viz DECISIONS.md a docs/SOURCES.md.

1. Zapiš verzi/build a větev hry, platformu a OS do environment.local.json.
2. Zkopíruj GamePaths.props.example na GamePaths.props a nastav skutečné cesty.
   GameManagedPath musí obsahovat čtyři referencované herní DLL. ExternalManagedPath
   musí obsahovat 0Harmony.dll odpovídající instalaci. Knihovny zůstávají lokálně.
3. S nainstalovaným .NET SDK spusť:
   `dotnet build src/StargateX2/StargateX2.csproj -c Debug`
   Ulož celý výstup; chyba závislosti znamená nejprve ověřit rozhraní cílové verze.
4. Teprve po úspěšném buildu připrav nový obsahový balíček `stargate_x2` v ověřené
   uživatelské složce módů. Jeho kořen obsahuje mod/manifest.json; výstup
   StargateX2.dll patří do assembly/common/. Build sám nic do hry nekopíruje.
5. Povol tento mód a spusť novou testovací kampaň. V logu vyhledej
   `[XSG] loaded version=0.1.0` a `[XSG] world-created section=Strategy`.
6. Ulož a načti testovací kampaň, znovu zkontroluj vytvoření strategického světa
   a chyby loaderu. Přilož log, verzi hry a seznam povolených módů.

T00 bez hry: `python tools/check_source.py`. Tato kontrola nepřekládá C#.
Zdrojový ZIP není připravený instalační ZIP, protože neobsahuje sestavenou DLL.
