import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def verticale(mat):
    return -1


# retourne soit le produit en partant d<un point
# ou le plus grand produit des veticales

def horizontale(mat):
    return -1


def diagonale_un(mat):
    return -1


def diagonale_deux(mat):
    return -1


def afficher_matrice():
    chaine = "73167176531330624919225119674426574742355349194934" \
             "96983520312774506326239578318016984801869478851843" \
             "85861560789112949495459501737958331952853208805511" \
             "12540698747158523863050715693290963295227443043557" \
             "66896648950445244523161731856403098711121722383113" \
             "62229893423380308135336276614282806444486645238749" \
             "30358907296290491560440772390713810515859307960866" \
             "70172427121883998797908792274921901699720888093776" \
             "65727333001053367881220235421809751254540594752243" \
             "52584907711670556013604839586446706324415722155397" \
             "53697817977846174064955149290862569321978468622482" \
             "83972241375657056057490261407972968652414535100474" \
             "82166370484403199890008895243450658541227588666881" \
             "16427171479924442928230863465674813919123162824586" \
             "17866458359124566529476545682848912883142607690042" \
             "24219022671055626321111109370544217506941658960408" \
             "07198403850962455444362981230987879927244284909188" \
             "84580156166097919133875499200524063689912560717606" \
             "05886116467109405077541002256983155200055935729725" \
             "71636269561882670428252483600823257530420752963450"

    a_copier = ""
    i = 0
    j = 0
    a_copier += "=np.array(["
    while i < 20:
        a_copier += "["
        while j < 50:
            print(j)
            if j != 49:
                a_copier += str(chaine[i * 20 + j]) + ","
            else:
                a_copier += str(chaine[i * 20 + j])
            j += 1
        a_copier += "],"
        j = 0
        i += 1
    a_copier += "])"
    # mat = np.array([[1, 2], [1, 2]], [[1, 2], [1, 2]]) # exemple
    print(a_copier)


def lire_matrice():
    # afficher_matrice()
    import numpy
    mat = np.array([[7, 3, 1, 6, 7, 1, 7, 6, 5, 3, 1, 3, 3, 0, 6, 2, 4, 9, 1, 9, 2, 2, 5, 1, 1, 9, 6, 7, 4, 4, 2, 6, 5,
                     7, 4, 7, 4, 2, 3, 5, 5, 3, 4, 9, 1, 9, 4, 9, 3, 4],
                    [2, 2, 5, 1, 1, 9, 6, 7, 4, 4, 2, 6, 5, 7, 4, 7, 4, 2, 3, 5, 5, 3, 4, 9, 1, 9, 4, 9, 3, 4, 9, 6, 9,
                     8, 3, 5, 2, 0, 3, 1, 2, 7, 7, 4, 5, 0, 6, 3, 2, 6],
                    [5, 3, 4, 9, 1, 9, 4, 9, 3, 4, 9, 6, 9, 8, 3, 5, 2, 0, 3, 1, 2, 7, 7, 4, 5, 0, 6, 3, 2, 6, 2, 3, 9,
                     5, 7, 8, 3, 1, 8, 0, 1, 6, 9, 8, 4, 8, 0, 1, 8, 6],
                    [2, 7, 7, 4, 5, 0, 6, 3, 2, 6, 2, 3, 9, 5, 7, 8, 3, 1, 8, 0, 1, 6, 9, 8, 4, 8, 0, 1, 8, 6, 9, 4, 7,
                     8, 8, 5, 1, 8, 4, 3, 8, 5, 8, 6, 1, 5, 6, 0, 7, 8],
                    [1, 6, 9, 8, 4, 8, 0, 1, 8, 6, 9, 4, 7, 8, 8, 5, 1, 8, 4, 3, 8, 5, 8, 6, 1, 5, 6, 0, 7, 8, 9, 1, 1,
                     2, 9, 4, 9, 4, 9, 5, 4, 5, 9, 5, 0, 1, 7, 3, 7, 9],
                    [8, 5, 8, 6, 1, 5, 6, 0, 7, 8, 9, 1, 1, 2, 9, 4, 9, 4, 9, 5, 4, 5, 9, 5, 0, 1, 7, 3, 7, 9, 5, 8, 3,
                     3, 1, 9, 5, 2, 8, 5, 3, 2, 0, 8, 8, 0, 5, 5, 1, 1],
                    [4, 5, 9, 5, 0, 1, 7, 3, 7, 9, 5, 8, 3, 3, 1, 9, 5, 2, 8, 5, 3, 2, 0, 8, 8, 0, 5, 5, 1, 1, 1, 2, 5,
                     4, 0, 6, 9, 8, 7, 4, 7, 1, 5, 8, 5, 2, 3, 8, 6, 3],
                    [3, 2, 0, 8, 8, 0, 5, 5, 1, 1, 1, 2, 5, 4, 0, 6, 9, 8, 7, 4, 7, 1, 5, 8, 5, 2, 3, 8, 6, 3, 0, 5, 0,
                     7, 1, 5, 6, 9, 3, 2, 9, 0, 9, 6, 3, 2, 9, 5, 2, 2],
                    [7, 1, 5, 8, 5, 2, 3, 8, 6, 3, 0, 5, 0, 7, 1, 5, 6, 9, 3, 2, 9, 0, 9, 6, 3, 2, 9, 5, 2, 2, 7, 4, 4,
                     3, 0, 4, 3, 5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5],
                    [9, 0, 9, 6, 3, 2, 9, 5, 2, 2, 7, 4, 4, 3, 0, 4, 3, 5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5, 0, 4, 4,
                     5, 2, 4, 4, 5, 2, 3, 1, 6, 1, 7, 3, 1, 8, 5, 6, 4],
                    [6, 6, 8, 9, 6, 6, 4, 8, 9, 5, 0, 4, 4, 5, 2, 4, 4, 5, 2, 3, 1, 6, 1, 7, 3, 1, 8, 5, 6, 4, 0, 3, 0,
                     9, 8, 7, 1, 1, 1, 2, 1, 7, 2, 2, 3, 8, 3, 1, 1, 3],
                    [1, 6, 1, 7, 3, 1, 8, 5, 6, 4, 0, 3, 0, 9, 8, 7, 1, 1, 1, 2, 1, 7, 2, 2, 3, 8, 3, 1, 1, 3, 6, 2, 2,
                     2, 9, 8, 9, 3, 4, 2, 3, 3, 8, 0, 3, 0, 8, 1, 3, 5],
                    [1, 7, 2, 2, 3, 8, 3, 1, 1, 3, 6, 2, 2, 2, 9, 8, 9, 3, 4, 2, 3, 3, 8, 0, 3, 0, 8, 1, 3, 5, 3, 3, 6,
                     2, 7, 6, 6, 1, 4, 2, 8, 2, 8, 0, 6, 4, 4, 4, 4, 8],
                    [3, 3, 8, 0, 3, 0, 8, 1, 3, 5, 3, 3, 6, 2, 7, 6, 6, 1, 4, 2, 8, 2, 8, 0, 6, 4, 4, 4, 4, 8, 6, 6, 4,
                     5, 2, 3, 8, 7, 4, 9, 3, 0, 3, 5, 8, 9, 0, 7, 2, 9],
                    [8, 2, 8, 0, 6, 4, 4, 4, 4, 8, 6, 6, 4, 5, 2, 3, 8, 7, 4, 9, 3, 0, 3, 5, 8, 9, 0, 7, 2, 9, 6, 2, 9,
                     0, 4, 9, 1, 5, 6, 0, 4, 4, 0, 7, 7, 2, 3, 9, 0, 7],
                    [3, 0, 3, 5, 8, 9, 0, 7, 2, 9, 6, 2, 9, 0, 4, 9, 1, 5, 6, 0, 4, 4, 0, 7, 7, 2, 3, 9, 0, 7, 1, 3, 8,
                     1, 0, 5, 1, 5, 8, 5, 9, 3, 0, 7, 9, 6, 0, 8, 6, 6],
                    [4, 4, 0, 7, 7, 2, 3, 9, 0, 7, 1, 3, 8, 1, 0, 5, 1, 5, 8, 5, 9, 3, 0, 7, 9, 6, 0, 8, 6, 6, 7, 0, 1,
                     7, 2, 4, 2, 7, 1, 2, 1, 8, 8, 3, 9, 9, 8, 7, 9, 7],
                    [9, 3, 0, 7, 9, 6, 0, 8, 6, 6, 7, 0, 1, 7, 2, 4, 2, 7, 1, 2, 1, 8, 8, 3, 9, 9, 8, 7, 9, 7, 9, 0, 8,
                     7, 9, 2, 2, 7, 4, 9, 2, 1, 9, 0, 1, 6, 9, 9, 7, 2],
                    [1, 8, 8, 3, 9, 9, 8, 7, 9, 7, 9, 0, 8, 7, 9, 2, 2, 7, 4, 9, 2, 1, 9, 0, 1, 6, 9, 9, 7, 2, 0, 8, 8,
                     8, 0, 9, 3, 7, 7, 6, 6, 5, 7, 2, 7, 3, 3, 3, 0, 0],
                    [2, 1, 9, 0, 1, 6, 9, 9, 7, 2, 0, 8, 8, 8, 0, 9, 3, 7, 7, 6, 6, 5, 7, 2, 7, 3, 3, 3, 0, 0, 1, 0, 5,
                     3, 3, 6, 7, 8, 8, 1, 2, 2, 0, 2, 3, 5, 4, 2, 1, 8], ])
    return mat


# Résumé :
if __name__ == '__main__':
    temps_initial = time.time_ns()

    ### CODE ICI

    temps_fin = time.time()
    reponse = -1
    print("Reponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Reponse : -1 , en : -1 ms.
