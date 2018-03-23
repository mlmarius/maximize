from __future__ import print_function
import itertools

#####################################
# Problema 1
# ==================================
# balancedSum
#####################################


def balancedSum(sales):
    total = sum(sales)
    crt = 0
    for i in range(0, len(sales)):
        if crt == total - crt - sales[i]:
            return i
        crt += sales[i]


print(balancedSum([1, 2, 3, 3]))

# ====================================================================

#####################################
# Problema 2
# ==================================
# maximizeRatings
#####################################



def maximizeRatings(ratings):

    # generez toate posibilele combinatii de selectii pentru lungimea lui ratings
    # ex: "0100100" ....
    # momentan le pastrez ca stringuri ca sa fie mai usor la pasul urmator
    combos = ["".join(seq) for seq in itertools.product("01", repeat=len(ratings))]

    # filtram optiunile si rejectam toate situatiile in care avem doua numere
    # rejectate in mod secvential
    # deasemenea, tot aici convertim din stringuri in liste de integer-uri astfel
    # incat sa ajungem la [0,1,0,1,1...]
    combos = [map(int, list(c)) for c in combos if '00' not in c]

    # am ramas doar cu optiunile valide conform criteriului
    # acum combin array-ul de intrare cu toate optiunile valide ramase
    # urmeaza sa folosesc fiecare optiune ca o masca pentru array-ul de intrare
    options = [zip(combo, ratings) for combo in combos]

    # pentru claritate
    # separam sumarea termenilor intr-o
    # functie separata
    def computeOutcome(option):
        # Calculam suma numerelor selectate
        items = [i[0]*i[1] for i in option]
        return sum(items)

    # calculam sumele generate de toate optiunile valide
    outcomes = [computeOutcome(option) for option in options]

    # voilla:
    return max(outcomes)


i1 = [-1, -2, -3, -4, -5]
i2 = [9, -1, -3, 4, 5]

print(maximizeRatings(i1))
print(maximizeRatings(i2))
