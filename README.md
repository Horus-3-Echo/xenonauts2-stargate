# Stargate — Xenonauts 2

Zdrojový startér 0.1.0, připravený 2026-09-25. Není to sestavený ani hratelný mód.
Obsahuje první kód pro záznam načtení módu a životního cyklu hry, soubory
projektu, backlog a testovací postup. Herní výprava ještě není implementovaná.

Začni v BUILD.md. Dostupná kontrola bez hry: `python tools/check_source.py`.
Průběžný stav je v STATUS.md, jediný pracovní backlog v BACKLOG.md.
Cílem je čtyřčlenný tým → planeta → artefakt → návrat → trvalá odměna.

Nález XSG-004A: docs/XSG-004A-MISSION-ENTRY.md rozlišuje vytvoření mise bez
sestřelu UFO od neověřeného nasazení bez letounu. Obsahuje přesné doložené typy,
zbývající vstupy a postup read-only kontroly skutečného moddable_content.zip.
Testy tohoto diagnostického nástroje: `python -m unittest discover -s tests -v`.
Jde o syntetické testy Python nástroje, nikoli build C# nebo spuštění výpravy.

Projekt je oddělený od druhé varianty módu. Sdílí pouze zadání v1.
Pracovní autoritou je [Horus-3-Echo/xenonauts2-stargate](https://github.com/Horus-3-Echo/xenonauts2-stargate), větev `main`.
Zdrojový ZIP byl 2026-09-25 převeden do repozitáře včetně prvního plánovaného běhu.
Původní ZIP zůstává archivem migrace; další vývoj se ukládá pouze do GitHubu.
Repozitář obsahuje zdroje, žádné herní knihovny, SDK ani sestavené binární soubory.

Nejdříve doplň verzi hry, distribuční platformu, větev a dostupnost SDK do
environment.example.json (pracovní kopie environment.local.json).
Cesty ke hře se nesmí odvozovat z ukázky jiné instalace.
