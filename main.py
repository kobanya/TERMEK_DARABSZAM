'''
NB-2023.03.20

Készíts egy Python programot 2-termek_for.py néven, amely 15 termék darabszámát generálja véletlenszámgenerátorral 0 és 100 között.
Használj “f” kiiíratási módot! For ciklust használj!
Segítség:
- for ciklus – annak az i változóját kell felhasználni a termékek sorszámához
- randrange 0 - 100

Mintapélda
1. termék: 45 db
2. Termék: 8 db
3. Termék:  0 db
…
15. Termék: 100 db
'''

from random import randrange

for i in range(1, 16):
    darabszam = randrange(101)
    print(f"{i}. termék: {darabszam} db")
