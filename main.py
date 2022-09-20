class Maison:

    # public
    superficie = 200
    hauteur = 5
    entre_nb = 3

    # protégé
    _protected = "protected"

    # privé
    __private = "private"

    def __init__(self):
        print( self.climatiser() )

    def climatiser(self):
        return "clim"

    def piscine(self):
        return "piscine"


# maison = Maison()

# print( maison.superficie )
# print( maison.hauteur )
# print( maison.entre_nb )
# print( maison.climatiser() )
# print( maison.piscine() )

# maison.superficie = 240

# print( maison.superficie )

# print( maison._protected )

# print( maison.__private )


class Immeuble(Maison):

    immeuble = "immeuble"



i = Immeuble()

print( i.immeuble )
print( i.piscine() )

print( i.hauteur )
print( i._protected )
print( i.__private )