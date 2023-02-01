# Es veu el import del datatime, la funcio i el calcul del la edat y l'any
def anyNaixement(edat):
    import datetime
    any = datetime.datetime.now().year
    calculAny = any - edat
    return calculAny


