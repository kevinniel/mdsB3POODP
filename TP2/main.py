class Stool:

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


s = Stool("bleu", 30, 2)

print(s.color, s.feet_height, s.feet_nb)


class Chair:

    color = None
    feet_height = None
    feet_nb = None
    back_height = None

    def __init__(self, color, feet_height, feet_nb, back_height):
        self.color = color
        self.feet_height = feet_height
        self.feet_nb = feet_nb
        self.back_height = back_height

    def fold(self):
        print("je me plie")

    def unfold(self):
        print("je me déplie")