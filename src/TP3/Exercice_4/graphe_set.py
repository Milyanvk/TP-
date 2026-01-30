def set_ens_sommets(set_arcs):
    sommet=set()
    for arc in set_arcs:
        sommets=sommets

def set_ens_successeurs(set_arcs,n):
    successeurs=[]
    for arc in set_arcs:
        if arc[0]==n:
            successeurs.append(arc[1])
    return successeurs

def set_ens_predecesseurs(set_arcs,n):
    predecesseurs=[]
    for arc in set_arcs:
        if arc[1]==n:
            predecesseurs.append(arc[0])
    return predecesseurs

def set_ens_puits(set_arcs)