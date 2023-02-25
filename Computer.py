import random

##COMPUTER PLAYER UPDATED - QUITE STRONG
##COMPUTER PLAYER UPDATED - QUITE STRONG
class Computer:
    """
    computer player
    """
    def __init__(self):
        pass

    def attack(self):
        """
        generate random positions to attack
        :return: a random position to attack the human's field
        """
        list_n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list_l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        x = random.choice(list_n)
        y = random.choice(list_l)
        return x,y

    def not_random(self,move):
        """

        :param move: holds the last HIT square and choses a neighbour of it to try to hit again a ship
        :return: a neighbour position of the last HIT position, because battleships are made of neighbour squares
        """
        x_hit=move[0]
        x_hit=int(x_hit)
        y_hit=move[1]
        y_hit=ord(y_hit)-65
        rand=random.randint(0,1)

        if rand==0:
            if y_hit<9:
                return x_hit,chr(y_hit+1+65)
            else:
                return x_hit,chr(y_hit-1+65)
        else:
            if x_hit < 9:
                return x_hit+1,chr(y_hit+65)
            else:
                return x_hit-1,chr(y_hit+65)