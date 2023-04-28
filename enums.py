from enum import Enum

class Main_menu(Enum):
    SIMP_FUNCTIONS=1
    COMP_FUNCTIONS=2
    MYZIP=3
    TEST_FUNCTIONS=4
    EXIT=0


class Simple(Enum):
    ADD_2_NUMBERS=1
    SUBTRACT_NUMBER=2
    MAIN_MENU=0
    
class Comp(Enum):
    PALINDROME_NUM=1
    SUM_DIGITS_NUM=2
    MAIN_MENU=0