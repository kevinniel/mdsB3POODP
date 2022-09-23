from pprint import pprint
import random

class Yams:

    game = None

    def __init__(self):
        self.game = Game()

class bcolors:
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


class Score:

    win = False

    combination = {
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

    def is_all_same( self, dices ):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers == 5):
                return i

        return False

    def count_number(self, dices, number):
        counter = 0

        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        for n in dices_value:
            if n == number:
                counter = counter + 1
        score = counter * number
        return score

    def is_brelan( self, dices ):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                return i              

        return False

    def is_carre( self, dices ):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 4):
                return i              

        return False

    def is_full( self, dices ):
        equal_three = False
        equal_two = False

        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                equal_three = True 
            elif (equal_numbers >= 2):
                equal_two = True  

        if (equal_three == True and equal_two == True):
            return True      

        return False

    def is_highest_suite( self, dices ):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        dices_value.sort()

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers > 1):
                dices_value.remove(i) 

        values_number =  len(dices_value)
        if (values_number == 5):

            if(dices_value[0]+1 == dices_value[1] and dices_value[1]+1 == dices_value[2] and dices_value[2]+1 == dices_value[3] and dices_value[3]+1 == dices_value[4]):

                return True

        return False

    def is_little_suite( self, dices ):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)

        dices_value.sort()

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers > 1):
                dices_value.remove(i) 

        values_number =  len(dices_value)
        if (values_number == 4):

            if(dices_value[0]+1 == dices_value[1] and dices_value[1]+1 == dices_value[2] and dices_value[2]+1 == dices_value[3]):

                return True

        return False

    def check_win(self):

        self.win = True

        for key in self.combination:
            if ( self.combination[key] == None ):
                self.win = False  


class Game():
    dices = Dices()
    print( bcolors.HEADER + "Le jeu commence !\n" + bcolors.ENDC )
    print( dices )

    score = Score()
    score.check_win()
    win = score.win

    first_try = True

    while(win == False):
        score.check_win()
        win = score.win

        error = False

        x=1
        if(first_try == True):
            x = 2
            
        while(error == False):

            score.check_win()
            win = score.win
            
            ask = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\n(" + str(x) + "/3) Quel dées voulez-vous modifiez ? (Ex : '123' ou '135' ou 'no' si vous ne voulez pas terminer vos 3 tours)\n" + bcolors.ENDC))

            error = dices.roll_indexes(ask)
            print( dices )

            x += 1
            if(x > 3):
                score.check_win()
                win = score.win
                
                possibility = []

                if (score.combination["chance"] == None):
                    possibility.append('chance')

                is_all_same = score.is_all_same( dices.dices )
                if (is_all_same > 0 and is_all_same < 7):
                    if (score.combination["yams"] == None):
                        possibility.append('yams')

                if (score.combination["one"] == None):
                    possibility.append('one')
                if (score.combination["two"] == None):
                    possibility.append('two')
                if (score.combination["three"] == None):
                    possibility.append('three')
                if (score.combination["four"] == None):
                    possibility.append('four')
                if (score.combination["five"] == None):
                    possibility.append('five')
                if (score.combination["six"] == None):
                    possibility.append('six')

                is_brelan = score.is_brelan( dices.dices )
                if (is_brelan != False):
                    if (score.combination["brelan"] == None):
                        possibility.append('brelan')

                is_carre = score.is_carre( dices.dices )
                if (is_carre != False):
                    if (score.combination["carre"] == None):
                        possibility.append('carre')

                is_full = score.is_full( dices.dices )
                if (is_full == True):
                    if (score.combination["full"] == None):
                        possibility.append('full')

                is_highest_suite = score.is_highest_suite( dices.dices )
                if (is_highest_suite == True):
                    if (score.combination["highest_suite"] == None):
                        possibility.append('highest_suite')
                    if (score.combination["little_suite"] == None):
                        possibility.append('little_suite')

                is_little_suite = score.is_little_suite( dices.dices )
                if (is_little_suite == True):
                    if (score.combination["little_suite"] == None):
                        possibility.append('little_suite')

                print ( '\nPossibilitées : ' + str(possibility) + '\n')

                for line in score.combination:
                    print ( bcolors.WARNING + '--------------------' + bcolors.ENDC)
                    if (score.combination[line] == None):
                        print ( bcolors.WARNING + '|' + line + '|   ' + bcolors.ENDC )
                    else:
                        print ( bcolors.WARNING + '|' + line + '| ' + str(score.combination[line]) + bcolors.ENDC )

                if not possibility:
                    ask_combination = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\nChoisissez une case à sacrifier...\n" + bcolors.ENDC))
                    while (score.combination[ask_combination] != None):
                        ask_combination = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\nChoisissez une case vide à sacrifier...\n" + bcolors.ENDC))
                    score.combination[ask_combination] = 0
                else:
                    ask_combination = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\nChoisissez la combinaison que vous souhaitez...\n" + bcolors.ENDC))

                    while (score.combination[ask_combination] != None):
                        print("Erreur : vous avez déjà choisi cette option, veuillez réessayer !")
                        ask_combination = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\nChoisissez la combinaison que vous souhaitez...\n" + bcolors.ENDC))

                    while ask_combination not in possibility:
                        print("Erreur : vous ne pouvez pas choisir cette option, veuillez réessayer !")
                        ask_combination = str(input( bcolors.UNDERLINE + bcolors.BOLD + "\nChoisissez la combinaison que vous souhaitez...\n" + bcolors.ENDC))
                
                dices_value = []
                for i in range(0, 5):
                    dices_value.append(dices.dices[i].value)
                dices_sum = sum(dices_value)

                if (score.combination[ask_combination] == None):
                    if (ask_combination == "one"):
                        count = score.count_number(dices.dices, 1)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "two"):
                        count = score.count_number(dices.dices, 2)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "three"):
                        count = score.count_number(dices.dices, 3)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "four"):
                        count = score.count_number(dices.dices, 4)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "five"):
                        count = score.count_number(dices.dices, 5)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "six"):
                        count = score.count_number(dices.dices, 6)
                        score.combination[ask_combination] = count
                    elif (ask_combination == "brelan"):
                        score.combination[ask_combination] = is_brelan
                    elif (ask_combination == "carre"):
                        score.combination[ask_combination] = is_carre
                    elif (ask_combination == "full"):
                        score.combination[ask_combination] = 25
                    elif (ask_combination == "little_suite"):
                        score.combination[ask_combination] = 30
                    elif (ask_combination == "highest_suite"):
                        score.combination[ask_combination] = 40
                    elif (ask_combination == "yams"):
                        score.combination[ask_combination] = 50
                    elif (ask_combination == "chance"):
                        score.combination[ask_combination] = dices_sum

                print ( bcolors.FAIL + "\nProchaine manche !\n" + bcolors.ENDC )
                dices.roll_all()
                print( dices )
                break

    if (win == True):
        print ( bcolors.WARNING + "Bravo, vous avez réussi !" + bcolors.ENDC )