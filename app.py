############################### script to test all the functions ##########################
from tools.col import  myzip
from tools.numbers.simp import add_numbers,subtrac_numbers
from tools.numbers.comp import ispal,sum_of_digits
from enums import Main_menu,Simple,Comp

count=0


def test():
    #test all functions
    print('add numbers - ok') if add_numbers(100,100)==200 else  print('add_numbers function not working')
    print('subtrac number ok') if subtrac_numbers(100,50)==50 else print('subtrac_numbers function not working')
    print('ispal function ok') if ispal(323)==True else print('ispal function not working')
    print('sumofdigits function ok') if sum_of_digits(111)==3 else print('sumofdigits function not working')
    print('myzip function ok') if myzip(('c','c'),('b','b'))==(('c','b'),(('c','b'))) else print('myzip function not working')


def main():
    #main menu for all functions
    selection=-1
    while selection != int(0):
        for i in Main_menu:
            print(f'{i.value} - {i.name}')
        selection=int(input('please enter the number of the function you would like to use'))
        if selection==Main_menu.SIMP_FUNCTIONS.value:simp_menu()
        if selection==Main_menu.COMP_FUNCTIONS.value:comp_menu()
        if selection==Main_menu.MYZIP.value:print(myzip((tuple(input('please enter a collection').split())),tuple((input('please enter a second collecion').split()))))
        if selection==Main_menu.TEST_FUNCTIONS.value:test()
        if selection==Main_menu.EXIT.value: selection=0


def simp_menu():
    #menu for simp functions
    global count
    selection=-1
    while selection != int(0):
        for i in Simple:
            print(f'{i.value} - {i.name}')
        selection=int(input('please enter the number of the function you would like to use'))
        if selection==Simple.ADD_2_NUMBERS.value:
            print(add_numbers(int(input('first num to add')),int(input('second num to add'))))
            count += 1
        if selection==Simple.SUBTRACT_NUMBER.value:
            print(subtrac_numbers(int(input('enter first num')),int(input('enter second number'))))
            count += 1
        if selection==Main_menu.EXIT.value: selection=0


def comp_menu():
    #menu for comp functions
        if count <  1: #checks if simp functions were used
            print("Sorry,you must use simple function at least once before using comp functions")
            main()
        else:
            selection=-1
            while selection != int(0):
                for i in Comp:
                    print(f'{i.value} - {i.name}')
                selection=int(input('please enter the number of the function you would like to use'))
                if selection== Comp.PALINDROME_NUM.value:print(ispal(input('enter a num')))
                if selection== Comp.SUM_DIGITS_NUM.value:print(sum_of_digits(input('enter a num')))
                



if __name__ == '__main__':
    main()