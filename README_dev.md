## WAŻNE INFO

Nastąpiła zmiana w wywołaniu reguły głównej (w `driver.py`: `engine.prove_goal('rules.beer($beer)'))` dodałem dwa parametry `$link` i `$explanation`.

Na pierwszy rzut oka powoduje to dwie zmiany w pisaniu reguł

1. w każdej regule do uzyskanych piw trzeba będzie dociągnąć ich linki tak: `beer_facts.link($beer, $link)`
2. w każdej regule trzeba dociągnąć jej `explanation`, np.:
   Napisałem regułę pytającą o porę roku. Dla każdej pory roku jest inne wytłumaczenie:
   ![image](https://github.com/nowakmikolaj/beer-me-up/assets/102852926/abdc2a6d-c26b-4dad-b811-c39723b4d24d)

Proponuję składnię `explanation(unikalna_nazwa_reguły, czynnik_determinujący_rezultat, tekst_wyjaśniający)`.
W moim przypadku `czynnik_determinujący` to pora roku. Wywołanie w regule:
![image](https://github.com/nowakmikolaj/beer-me-up/assets/102852926/337e2f9c-b35e-4d57-86ed-b3086bfcc135)

`explanation` dla każdego piwa jest konkatenowane i wypisywane na konsolę po wyborze TOP 5 najlepszych piw. Konkatenowanie jest warunkowe, ponieważ jedno piwo może być wyplute kilka razy z tym samym explanation (bo z tej samej reguły), wtedy nie konkatenujemy. W przeciwnym przypadku konkatenujemy. Logika konkatenacji jest w pliku `models/beer_info.py`.
