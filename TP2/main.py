class Seated:

    color = None
    feet_height = None
    feet_nb = None

    def __init__(self, color, feet_height, feet_nb):
        self.color = color
        self.feet_height = feet_height
        self.feet_nb = feet_nb

    def fold(self):
        print("je me plie")

    def unfold(self):
        print("je me déplie")


class Stool(Seated):

    def __init__(self, color, feet_height, feet_nb):
        super().__init__(color, feet_height, feet_nb)


class Chair(Seated):

    back_height = None

    def __init__(self, color, feet_height, feet_nb, back_height):
        super().__init__(color, feet_height, feet_nb)
        self.back_height = back_height


class SeatedFactory:
    
    def run(self, *args):

        if(len(args) == 3):
            return Stool(args[0], args[1], args[2])
        
        if(len(args) == 4):
            return Chair(args[0], args[1], args[2], args[3])

        return None


f = SeatedFactory()
f = f.run("aaa", 1)
print( type(f) )
# f ===> type Stool

# s = Stool("aaaa", 1, 1)
# # s.unfold()

# c = Chair("aaaa", 1, 1, 4)
# c.fold()
# c.unfold()
