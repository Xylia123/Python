# -*- coding: utf-8 -*-
#bekérünk egy számot
#elosztjuk 1.6-tal, hogy megkapjuk hány mérföld
#kiírjuk, hogy pl. "16km az 10 mérföld"

# -*- coding: utf-8 -*-
x = int(raw_input("Enter the value for x: "))
print x

y = x/1.6
print str (x) + " km " + str(y) + " merfold"

while True:
    km = int(raw_input ("kérek egy távolságot km-ben: "))
    merfold = km/1.6
    print str(km) + " km az " + str(merfold) + " merfold "
    # kérdezzük meg, hogy "Szeretnél még átváltani?"
    tovabb = raw_input("Szeretnél még átváltani? (igen/nem) ")

    # ha nem, akkor lépjünk ki
    if tovabb == "nem":
        break

