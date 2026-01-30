from.position import position

def sous_liste(petite_liste,grande_liste):
    
    depart=0
    for element in petite_liste:
        pos=position(element,grande_liste,depart)
        if pos==-1:
            return False
        depart= pos+1
    
    return True
    
    
    
    
    if len(petite_liste)==0:
        return True

    index_petite=0
    index_grande=0
