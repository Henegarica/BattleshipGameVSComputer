
from texttable import Texttable
import random

from Computer import Computer
from Field import Field

##COMPUTER PLAYER UPDATED - QUITE STRONG
##COMPUTER PLAYER UPDATED - QUITE STRONG
class UI:
    def __init__(self):
        self._field_player_bs=Field()
        self._field_computer_bs=Field()
        self._field_computer_bs.computer_place_bs()
        self.ComputerPlayer=Computer()

    def check_input_for_attack(self,input):
        if len(input)!=3:
            return 0
        if input[0]<'0' or input[0]>'9':
            return 0
        if int(input[0]) not in range(10):
            return 0
        if ord(input[2])-65 not in range(10):
            return 0
        return 1

    def create_battleship(self,num):
        print("Battleship length: " +str(num))
        try:
            inp=input("Enter coordinates for the start of the battleship:")
            if len(inp)>3:
                return 0
            x1=int(inp[0])
            y1=inp[2]
            inp=input("Enter coordinates for the end of the battleship:")
            if len(inp) > 3:
                return 0
            x2=int(inp[0])
            y2=inp[2]
            return self._field_player_bs.translate_position_to_move(x1, y1, x2,y2,num)
        except:
            return 0

    def add_moves_for_computer(self,list,x,y,list2):
        x=int(x)
        y=ord(y)-65
        list3=[]
        for el in list2:
            command=str(el[0])+" "+el[1]
            list3.append(command)

        if x-1>=0:
            com=str(x-1)+" "+chr(y+65)
            if com not in list3:
                list.append(com)
        if x+1<=9:
            com = str(x+1)+" "+chr(y+65)
            if com not in list3:
                list.append(com)
        if y-1>=0:
            com = str(x)+" "+chr(y+65-1)
            if com not in list3:
                list.append(com)
        if y+1<=9:
            com = str(x)+" "+chr(y+65+1)
            if com not in list3:
                list.append(com)



    def place_battleships(self):

        num=6
        while num>1 :

            x=self.create_battleship(num)

            if x==1:
                pass
            else:
                while x==0:
                    print("Invalid coordinates. Try again!")
                    x=self.create_battleship(num)
            print(str(self._field_player_bs))
            num=num-1


    def menu(self):
        print(str(self._field_player_bs))
        print(str(self._field_computer_bs))
        self.place_battleships()
        computer_hit=0
        computer_not_random_moves=[]
        finished_1=self._field_player_bs.check_finished()
        finished_2=self._field_computer_bs.check_finished()

        player_turn=True
        while not finished_1 and not finished_2:
            print(str(self._field_player_bs))
            list=self._field_player_bs.return_list_moves()
            print(list)

            if player_turn:
                invalid=1
                while invalid:
                    inp=input("Where to attack?")
                    if self.check_input_for_attack(inp)==1:
                        x=inp[0]
                        y=inp[2]
                        if self._field_computer_bs.check_not_attacked(x,y)==1:
                            invalid=0
                        else:
                            print("Square already attacked. Try another one!")
                    else:
                        print("Invalid coordinates.Try again!")
                hit=self._field_computer_bs.attack(x,y)
                self._field_player_bs.add_to_list_moves(x,y,hit)

            else:
                invalid = 1
                while invalid:
                    # if computer_hit==0:
                    #     move=self.ComputerPlayer.attack()
                    # elif computer_hit==1:
                    #     comp_hit_move=self._field_computer_bs.return_list_moves()
                    #     comp_hit_move=comp_hit_move[len(comp_hit_move)-1]
                    #     move=self.ComputerPlayer.not_random(comp_hit_move)
                    if len(computer_not_random_moves)==0:
                        move=self.ComputerPlayer.attack()
                        x = move[0]
                        y = move[1]
                    else:
                        move=computer_not_random_moves[len(computer_not_random_moves)-1]
                        computer_not_random_moves.pop(len(computer_not_random_moves)-1)
                        x = move[0]
                        y = move[2]
                    if self._field_player_bs.check_not_attacked(x,y)==1:
                        invalid=0
                        hit=self._field_player_bs.attack(x,y)
                        if hit==1:
                            # computer_hit=1
                            comp_list_made_moves=self._field_computer_bs.return_list_moves()
                            self.add_moves_for_computer(computer_not_random_moves,x,y,comp_list_made_moves)
                        else:
                            # computer_hit=0
                            pass
                        self._field_computer_bs.add_to_list_moves(x,y,hit)
                        print("Computer attacked at " + str(x) +" "+ str(y))

            player_turn= not player_turn
            finished_1 = self._field_player_bs.check_finished()
            finished_2 = self._field_computer_bs.check_finished()

        if player_turn:
            print("You LOST!")
        else:
            print("You WON!")


console = UI()
console.menu()