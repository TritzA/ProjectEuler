import time

from Utilitaire import Gene

# Résumé : La classe Test sert aussi de modèle.
if __name__ == '__main__':
    temps_debut = time.time()

    # CODE ICI

    temps_fin = time.time()
    Gene.rep(-1, temps_fin - temps_debut)
    # Réponse : -1 , en : -1 s.
