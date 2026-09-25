# Testovací brány

| ID | Ověření | Důkaz |
| --- | --- | --- |
| T00 | Struktura a formáty zdrojů | tools/check_source.py, přesný výstup |
| T00A | Read-only vyhledávač definic, pouze syntetická data | python -m unittest discover -s tests -v; nenahrazuje skutečná herní data ani build |
| T01 | Sestavení skutečným SDK/kompilátorem | verze prostředí, celý build log |
| T02 | Načtení módu a vlastní log | verze hry, povolené módy, log se značkou projektu |
| T03 | Spuštění nové testovací kampaně | log nové kampaně, bez chyby loaderu |
| T04 | Uložení/načtení testovací kampaně | log po načtení, žádná nová chyba |
| T05 | Spuštění mise bez UFO se správnou vazbou na kampaň | Podmíněný scénář v XSG-004A-MISSION-ENTRY.md; NOT_RUN do sestavení XSG-004B a doložení jeho spouštěče |
| T10 | M1: artefakt a návrat | postup z FIRST-EXPEDITION.md, stavy týmu |
| T11 | M1: ústup bez artefaktu | bez odměny, správní přeživší |
| T12 | M1: ztráta týmu / nosiče | žádná neoprávněná odměna |
| T13 | M1: opakované načtení a zpracování výsledku | odměna právě jednou |
| T14 | M1: řízení původní kampaně | průchod definovaným úvodním intervalem |
| T20 | Export prefabu v ověřeném Unity Editoru | Přesný podmíněný postup v XSG-011A-ASSET-EXPORT.md; Editor log, manifesty, SHA-256 balíčku; nyní NOT_RUN |
| T21 | Indexace a zobrazení vlastní geometrie v X2 | Postup v XSG-011A-ASSET-EXPORT.md; log a screenshot; nyní NOT_RUN, čeká na T20 a XSG-011B |

T00 nenahrazuje T01–T04. Pro počáteční loader zatím provádět jen T00–T04.
Testy M1 se stanou vykonatelnými až po implementaci jednotlivých částí.
Používat novou testovací kampaň a označené testovací pozice.

Výsledek testu musí být PASS, FAIL nebo NOT_RUN. U NOT_RUN uvést konkrétní důvod.
Při požadavku na uživatele uvést přesné kroky a požadovaný log; samotné „otestuj to“ nestačí.
