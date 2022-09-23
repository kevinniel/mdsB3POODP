# 358 lignes
import random


class Bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Dice():

    nb_face = 6
    value = None

    def roll(self):
        self.value = random.randint(1, self.nb_face)

class Dices():

    dices = []

    def __init__(self):
        for i in range(0, 5):
            self.dices.append(Dice())
        # ?????
        self.roll_all()
        

    def __repr__(self):
        return str( self.dices[0].value) + " ❘ " + str(self.dices[1].value) + " ❘ " + str(self.dices[2].value) + " ❘ " + str(self.dices[3].value) + " ❘ " + str(self.dices[4].value)

    def roll_all(self):
        for i in range(0, 5):
            self.dices[i].roll()

    def roll_indexes(self, indexes):
        accepted_value = ["n","1","2","3","4","5"]
        for i in indexes:
            if i in accepted_value:
                if (i == "n"):
                    return False

                self.dices[int(i)-1].roll()

        return False

class Score():

    win = False
    combinations = {
        "one" : None,
        "two" : None,
        "three" : None,
        "four" : None,
        "five" : None,
        "six" : None,
        "bonus_part_one" : None,
        "brelan" : None,
        "carre" : None,
        "full" : None,
        "little_suite" : None,
        "highest_suite" : None,
        "yams" : None,
        "chance" : None
    }  

    # TODO
    def is_all_same( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        # TODO
        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers == 5):
                return i

        return False

    # TODO
    def count_number(self, dices, number):
        counter = 0
        dices_value = self.dices_values_to_array(dices)

        for n in dices_value:
            if n == number:
                counter += 1
        
        return counter * number

    # TODO
    def is_brelan( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        # TODO
        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                return i              

        return False

    # TODO
    def is_carre( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        # TODO
        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 4):
                return i              

        return False

    # TODO
    def is_full( self, dices ):
        is_brelan = False
        is_pair = False

        dices_value = self.dices_values_to_array(dices)

        # TODO
        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                is_brelan = True 
            elif (equal_numbers >= 2):
                is_pair = True

        if (is_brelan and is_pair):
            return True      

        return False

    # TODO
    def is_highest_suite( self, dices ):
        
        dices_value = self.__sort_array_dices(dices)
        print(dices_value)
        # TODO
        if([1, 2, 3, 4, 5] in dices_value or [2, 3, 4, 5, 6] in dices_value):
            return True

        return False

    # TODO
    def is_little_suite( self, dices ):

        dices_value = self.__sort_array_dices(dices)

        # TODO
        if([1, 2, 3, 4] in dices_value or [2, 3, 4, 5] in dices_value or [3, 4, 5, 6] in dices_value):
            return True

        return False

    def is_game_ended(self):

        self.win = True

        for key in self.combinations:
            if ( self.combinations[key] == None ):
                self.win = False  

    def dices_values_to_array(self, dices):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)
        return dices_value
    
    def __sort_array_dices(self, dices):
        dices_values = self.dices_values_to_array(dices)
        return dices_values.sort()

class Display():

    def display(self, value):
        print(value)

    def start_game(self):
        print(Bcolors.HEADER + "Le jeu commence !\n" + Bcolors.ENDC)

    def update_dices(self, x):
        print(Bcolors.UNDERLINE + Bcolors.BOLD + "\n(" + str(x) + "/3) Quel dées voulez-vous modifiez ? (Ex : '123' ou '135' ou 'no' si vous ne voulez pas terminer vos 3 tours)\n" + Bcolors.ENDC)

    def show_possibilities(self, possibilities):
        print('\nPossibilitées : ' + str(possibilities) + '\n')

    def show_combinations(self, combinations):
        for line in combinations:
            print (Bcolors.WARNING + '--------------------' + Bcolors.ENDC)
            if (combinations[line] == None):
                print(Bcolors.WARNING + '|' + line + '|   ' + Bcolors.ENDC)
            else:
                print(Bcolors.WARNING + '|' + line + '| ' + str(combinations[line]) + Bcolors.ENDC)

    def sacrifice_case(self):
        print(Bcolors.UNDERLINE + Bcolors.BOLD + "\nChoisissez une case à sacrifier...\n" + Bcolors.ENDC)

    def sacrifice_empty_case(self):
        print(Bcolors.UNDERLINE + Bcolors.BOLD + "\nChoisissez une case vide à sacrifier...\n" + Bcolors.ENDC)

    def choose_combination(self):
        print(Bcolors.UNDERLINE + Bcolors.BOLD + "\nChoisissez la combinaison que vous souhaitez...\n" + Bcolors.ENDC)

    def option_not_available(self):
        print("Erreur : vous avez déjà choisi cette option, veuillez réessayer !")
    
    def option_not_allowed(self):
        print("Erreur : vous ne pouvez pas choisir cette option, veuillez réessayer !")

    def next_round(self):
        print(Bcolors.FAIL + "\nProchaine manche !\n" + Bcolors.ENDC)

    def win(self):
        print(Bcolors.WARNING + "Bravo, vous avez réussi !" + Bcolors.ENDC)

class Game():

    def __init__(self):
        self.__init_attributes()
        self.__init_methods()

    def __init_attributes(self):
        self.dices = Dices()
        self.score = Score()
        self.display = Display()

    def __init_methods(self):
        self.launch_game()

    def launch_game(self):
        
        first_try = self.__init_game()

        while(self.score.win == False):
            self.start_round(first_try)

        if (self.score.win == True):
            self.display.win()

    def __init_game(self):
        self.display.start_game()
        self.display.display(self.dices)
        self.score.is_game_ended()
        return True

    def start_round(self, first_try):
        self.score.is_game_ended()
        error = False
        x=1
        if(first_try == True):
            x = 2
        while(error == False):
            self.score.is_game_ended()
            self.display.update_dices(x)
            ask = str( input() )
            error = self.dices.roll_indexes(ask)
            self.display.display(self.dices)
            x += 1
            if(x > 3):
                self.score.is_game_ended()
                possibilities = self.__get_possibilities()
                self.display.show_possibilities(possibilities)
                self.display.show_combinations(self.score.combinations)
                if not possibilities:
                    self.display.sacrifice_case()
                    ask_combination = str(input())
                    while (self.score.combinations[ask_combination] != None):
                        self.display.sacrifice_empty_case()
                        ask_combination = str( input() )
                    self.score.combinations[ask_combination] = 0
                else:
                    self.display.choose_combination()
                    ask_combination = str(input())
                    while (self.score.combinations[ask_combination] != None):
                        self.display.option_not_available()
                        self.display.choose_combination()
                        ask_combination = str( input() )
                    while ask_combination not in possibilities:
                        self.display.option_not_allowed()
                        self.display.choose_combination()
                        ask_combination = str( input() )
                if (self.score.combinations[ask_combination] == None):
                    self.__set_scores(ask_combination)
                self.display.next_round()
                self.dices.roll_all()
                self.display.display(self.dices)
                break

    def __get_possibilities(self):
        possibilities = []

        if (self.score.combinations["chance"] == None):
            possibilities.append('chance')

        is_all_same = self.score.is_all_same( self.dices.dices )
        if (is_all_same > 0 and is_all_same < 7):
            if (self.score.combinations["yams"] == None):
                possibilities.append('yams')

        if (self.score.combinations["one"] == None):
            possibilities.append('one')
        if (self.score.combinations["two"] == None):
            possibilities.append('two')
        if (self.score.combinations["three"] == None):
            possibilities.append('three')
        if (self.score.combinations["four"] == None):
            possibilities.append('four')
        if (self.score.combinations["five"] == None):
            possibilities.append('five')
        if (self.score.combinations["six"] == None):
            possibilities.append('six')

        is_brelan = self.score.is_brelan( self.dices.dices )
        if (is_brelan != False):
            if (self.score.combinations["brelan"] == None):
                possibilities.append('brelan')

        is_carre = self.score.is_carre( self.dices.dices )
        if (is_carre != False):
            if (self.score.combinations["carre"] == None):
                possibilities.append('carre')

        is_full = self.score.is_full( self.dices.dices )
        if (is_full == True):
            if (self.score.combinations["full"] == None):
                possibilities.append('full')

        is_highest_suite = self.score.is_highest_suite( self.dices.dices )
        if (is_highest_suite == True):
            if (self.score.combinations["highest_suite"] == None):
                possibilities.append('highest_suite')
            if (self.score.combinations["little_suite"] == None):
                possibilities.append('little_suite')

        is_little_suite = self.score.is_little_suite( self.dices.dices )
        if (is_little_suite == True):
            if (self.score.combinations["little_suite"] == None):
                possibilities.append('little_suite')
        
        return possibilities

    def __set_scores(self, ask_combination):
        if (ask_combination == "one"):
            count = self.score.count_number(self.dices.dices, 1)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "two"):
            count = self.score.count_number(self.dices.dices, 2)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "three"):
            count = self.score.count_number(self.dices.dices, 3)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "four"):
            count = self.score.count_number(self.dices.dices, 4)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "five"):
            count = self.score.count_number(self.dices.dices, 5)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "six"):
            count = self.score.count_number(self.dices.dices, 6)
            self.score.combinations[ask_combination] = count
        elif (ask_combination == "brelan"):
            self.score.combinations[ask_combination] = self.score.is_brelan(self.dices)
        elif (ask_combination == "carre"):
            self.score.combinations[ask_combination] = self.score.is_carre(self.dices)
        elif (ask_combination == "full"):
            self.score.combinations[ask_combination] = 25
        elif (ask_combination == "little_suite"):
            self.score.combinations[ask_combination] = 30
        elif (ask_combination == "highest_suite"):
            self.score.combinations[ask_combination] = 40
        elif (ask_combination == "yams"):
            self.score.combinations[ask_combination] = 50
        elif (ask_combination == "chance"):
            self.score.combinations[ask_combination] = sum(self.score.dices_values_to_array(self.dices.dices))

Game()