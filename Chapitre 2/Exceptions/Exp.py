
def verification(param):
    if param not in (5, 11, 9):
        raise ValueError("'Param' ne peut etre que 5, 11 ou 9")
    print 'tout va bien'

verification(5)