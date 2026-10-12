#21
#12.10.
#kulickajde ze strany na stranu plus tabulka

import math
import time

pocet = int(input("Kolik má být počet? "))

for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)

for i in range(pocet):
    print(" " * (pocet - i) + "O")
    time.sleep(0.1)

print("Tabulka")
for i in range(10):
    print(i, math.sqrt(i))
