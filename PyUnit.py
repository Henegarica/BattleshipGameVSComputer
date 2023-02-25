import unittest
from Computer import  Computer
from Field import Field



class PyUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self._computer_field=Field()
        self._player_field=Field()
        self._comp_player=Computer()

    def test_computer(self):
        list_n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list_l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        move=self._comp_player.attack()
        move = self._comp_player.not_random(move)
        move = self._comp_player.not_random(move)
        move = self._comp_player.not_random(move)
        self.assertIn(move[0],list_n)
        self.assertIn(move[1],list_l)

    def test_field_not_attacked(self):
        self.assertEqual(self._player_field.check_not_attacked(0,"A"),1)

    def test_return_list_moves(self):
        self.assertEqual(self._player_field.return_list_moves(),[])

    def test_place_and_attack_BS(self):
        self.assertEqual(self._player_field.check_finished(),1)
        self.assertEqual(self._player_field.translate_position_to_move(0, "X", 0, "Z", 6),0)
        self.assertEqual(self._player_field.translate_position_to_move(0, "A", 0, "B", 6),0)
        self.assertEqual(self._player_field.translate_position_to_move(0,"A",0,"B",2),1)
        self.assertEqual(self._player_field.translate_position_to_move(0, "A", 0, "B", 2), 0)
        self.assertEqual(self._player_field.translate_position_to_move(0, "D", 0, "C", 2),1)
        self.assertEqual(self._player_field.translate_position_to_move(15, "A", 13, "B", 2),0)
        self.assertEqual(self._player_field.check_finished(), 0)
        self.assertEqual(self._player_field.translate_position_to_move(1, "A", 3, "A", 6),0)
        self.assertEqual(self._player_field.translate_position_to_move(1,"A",3,"A",3),1)
        self.assertEqual(self._player_field.translate_position_to_move(3, "E", 1, "E", 3),1)
        self.assertEqual(self._player_field.translate_position_to_move(3, "A", 1, "A", 3),0)
        self.assertEqual(self._player_field.make_move(0,"A",1,"B",2),0)
        x = self._player_field.__str__()

        self.assertEqual(self._player_field.attack(0,"A"),1)
        self.assertEqual(self._player_field.attack(0, "A"),0)
        self.assertEqual(self._player_field.attack(12, "A"), 0)
        self.assertEqual(self._player_field.attack(0, "X"), 0)
        self.assertEqual(self._player_field.attack(8, "H"), 2)
        self.assertEqual(self._player_field.check_not_attacked(8,"H"),0)
        self._player_field.add_to_list_moves(0,"A",1)
        self.assertEqual(len(self._player_field.return_list_moves()),1)
        self._player_field.add_to_list_moves(0, "A",0)
        self.assertEqual(len(self._player_field.return_list_moves()), 2)

    def test_computer_place(self):
        self._computer_field.computer_place_bs()
        self.assertEqual(self._computer_field.check_finished(),0)



    def test_field_str(self):
        x=self._player_field.__str__()


    def tearDown(self) -> None:
        pass