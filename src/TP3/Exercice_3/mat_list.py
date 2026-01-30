def list_new_mat(nl, nc):
    # return [[0 for j in range(nc)] for i in range(n1)]
    matrice=[]
    for i in range(nl):
        ligne=[]
        for j i in range(nc):
            ligne.append(0)
        matrice.append(ligne)

    return matrice

def list_set_mat(matrice,ligne,colonne,valeur):
    matrice[ligne][colonne]=valeur

def list_get_mat(matrice,ligne,colonne);
    return matrice[ligne][colonne]
