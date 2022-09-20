import random

class Dice:

    nb_face = 6
    
    # gestion du cas None
    __value = None

    def roll(self):
        self.__value = random.randint(1, self.nb_face)
        # self.set_value( random.randint(1, self.nb_face) )

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


class Dices:

    __dice1 = None
    __dice2 = None
    is_double = None
    sum = None

    def __init__(self):
        self.__dice1 = Dice()
        self.__dice2 = Dice()

    def roll(self):
        self.__dice1.roll()
        self.__dice2.roll()
        # vérifier si double
        self.__check_double()
        # vérifier la somme
        self.__check_sum()

    def __check_double(self):
        if( self.__dice1.get_value() == self.__dice2.get_value() ):
            self.is_double = True
        else:
            self.is_double = False
        
        print( self.is_double )

    def __check_sum(self):
        self.sum = self.__dice1.get_value() + self.__dice2.get_value()
        
        print( self.sum )

d = Dices()
d.roll()
# d.__dice1.__value = 6
# d.__dice2.__value = 6
# print( d.__dice1.__value, d.__dice2.__value )
# print( d.is_double )