import random

from texttable import Texttable

##COMPUTER PLAYER UPDATED - QUITE STRONG
##COMPUTER PLAYER UPDATED - QUITE STRONG
class Field:
    def __init__(self):
        """
        initializing the game matrix
        initializing the list of moves which have been made by the computer/player
        initializing the list of remaining squares of battleships, in order to use it for calculating who won
        """
        self._cols  = 10
        self._rows  = 10
        self._data= [[0]*self._cols for i in range(self._rows)]
        self._remaining_bs=0
        self._list_moves=[]


    def __str__(self):
        """

        :return: the Game Field, in form of a Table
        """
        t= Texttable()
        header_row=['/']
        for i in range(self._cols):
            header_row.append(chr(65+i))
        t.header(header_row)

        for i in range(0,self._rows):

            display_row=[i]
            for j in range(self._cols):
                val=self._data[i][j]
                if val==0:
                    display_row.append(' ')
                else:
                    display_row.append(val)
            t.add_row(display_row)

        return t.draw()

    def check_not_attacked(self,x,y):
        """

        :param x: the X coordinate
        :param y: the Y coordinate
        :return: return 0 if square has been already attacked, such that you don't attack a square multiple times
                 return 1 if square is valid and has not been attacked yet
        """
        row1 = int(x)
        col1 = ord(y) - 65
        if self._data[row1][col1]<0:
            return 0
        return 1

    def add_to_list_moves(self,x,y,hit):
        """

        :param x: the X coordinate
        :param y: the Y coordinate
        :param hit: hit=1 if  X and Y represent a battleship square, else hit != 1 represents a missed attack
        :return: append to the list of moves if the square represented by X and Y is HIT or MISS
        """
        if hit==1:
            self._list_moves.append((x,y,"h"))
        else:
            self._list_moves.append((x,y,"m"))

    def return_list_moves(self):
        """

        :return: return the list of moves made by a player
        """
        return self._list_moves[:]


    def check_empty_square_for_new_bs(self,row1,col1,row2,col2,num):
        """

        :param row1: the X coordinate where the BS begins
        :param col1: the Y coordinate where the BS begins
        :param row2: the X coordinate where the BS ends
        :param col2: the Y coordinate where the BS ends
        :param num: the length of the BS
        :return: 1 if squares are empty and BS can be placed there in the Field,
        0 if squares are already taken and BS can not be placed
        """
        if row1==row2:
            if col1 > col2:
                col1,col2=col2,col1
            for i in range(col1,col2+1):
                if self._data[row1][i]==0:
                    pass
                else:
                    return 0
            return 1

        if col1==col2:
            if row1>row2:
                row1,row2=row2,row1
            for j in range(row1,row2+1):
                if self._data[j][col1]==0:
                    pass
                else:
                    return 0
            return 1


    def translate_position_to_move(self,x1,y1,x2,y2,num):
        """

        :param x1: the X coordinate where the BS begins
        :param y1: the Y coordinate where the BS begins
        :param x2: the X coordinate where the BS ends
        :param y2: the Y coordinate where the BS ends
        :param num: the length of the BS
        :return: translate "0 A" to "0 0" coordinates and return 0 if coordinates are INVALID or already in use,
        1 if BS has been placed successfully
        """
        row1=int(x1)
        col1=ord(y1)-65
        row2=int(x2)
        col2=ord(y2)-65

        if row1 in range(10) and row2 in range(10):
            if col1 in range(10) and col2 in range(10):
                pass
            else:
                return 0
        else:
            return 0
        if self.check_empty_square_for_new_bs(row1,col1,row2,col2,num):
            return self.make_move(row1,col1,row2,col2,num)
        else:
            return 0

    def make_move(self,x1,y1,x2,y2,num):
        """

        :param x1: the X coordinate where the BS begins
        :param y1: the Y coordinate where the BS begins
        :param x2: the X coordinate where the BS ends
        :param y2: the Y coordinate where the BS ends
        :param num: the length of the BS
        :return: place the BS on the given coordinates
        """
        if x1==x2:
            if y1 > y2:
                y1,y2=y2,y1
            if y2-y1 != num-1:
                 return 0
            for i in range(y1,y2+1):
                if self._data[x1][i]==0:
                    self._data[x1][i]=num
            self._remaining_bs+=num
            return 1

        if y1==y2:
            if x1>x2:
                x1,x2=x2,x1
            if x2-x1 != num-1:
                return 0
            for j in range(x1,x2+1):
                if self._data[j][y1]==0:
                    self._data[j][y1]=num
            self._remaining_bs+=num
            return 1

        return 0

    def check_finished(self):
        """

        :return: return 1 if player/computer has no remaining BS ( game has been won by one of them)
                 return 0 if player and computer have remaining BS
        """
        if self._remaining_bs==0:
            return 1
        else:
            return 0


    def computer_place_bs(self):
        """
                choose a random position to place the battleship, if squares are already in use,
                enter the while loop and choose random positions until valid ones are found
        :return: place the battleships on the computer field
        """
        num=6
        list_n=[0,1,2,3,4,5,6,7,8,9]
        list_l=["A","B","C","D","E","F","G","H","I","J"]
        while num>1 :
            x1=random.choice(list_n)
            x2=random.choice(list_n)
            y1=random.choice(list_l)
            y2=random.choice(list_l)
            returned=self.translate_position_to_move(x1,y1,x2,y2,num)
            if returned==1:
                pass
            else:
                while returned==0:
                    x1 = random.choice(list_n)
                    x2 = random.choice(list_n)
                    y1 = random.choice(list_l)
                    y2 = random.choice(list_l)
                    returned=self.translate_position_to_move(x1,y1,x2,y2,num)
            num=num-1

    def attack(self,x,y):
        """

        :param x: X coordinate to attack
        :param y: Y coordinate to attack
        :return: 1 if square attacked is HIT, 2 if square attacked is MISS, 0 if square already attacked
        """
        row1 = int(x)
        col1 = ord(y) - 65
        if row1 in range(10) :
            if col1 in range(10):
                pass
            else:
                return 0
        else:
            return 0
        if self._data[row1][col1] > 0:
            self._data[row1][col1]=-1
            self._remaining_bs=self._remaining_bs-1
            return 1
        elif self._data[row1][col1]==0:
            self._data[row1][col1] = -99
            return 2
        else:
            return 0
