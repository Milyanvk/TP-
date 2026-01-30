def cumuler(fonction,liste):
    if len(liste)<2:
        raise ValueError('La liste a seulement 2 éléments')

    accumulateur=liste[0]
    for element in liste[1:]:
        accumulateur=fonction(accumulateur,element)

    return accumulateur