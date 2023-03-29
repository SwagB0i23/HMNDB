print('                WELCOME TO THE HMNDB PROTOTYPE!')

print('\n\nHMNDB STANDS FOR:\nH - ow\nM - any\nN - umbers\nD - ivisible\nB - y')

print('\n\n\n          Basically, what the program does is: it takes a range of values [a to b] that you input and a number [x] (which you also input)\nand it checks how many numbers (and which numbers, specifically) are divisble by said number [x].')

print('\n\n\n          PLEASE ENJOY! REPORT ANY BUGS YOU SEE AND PLEASE BE PATIENT! THANKS')

print('\n\n\nSIDE NOTE: This is a working prototype; thus, there will be missing features to be added in the future.')

print('\n\n\n          PROGRAMMED BY: CJ GALVEZ')

#BACKBONE FUNCTIONS

def hmndb_calc(numlist):

    """THIS FUNCTION IS THE BACKBONE OF THE CALCULATOR"""
    """IT TAKES A NNUMLIST INPUTTED BY THE USER THROUGH user_input_range ran through minmaxinput and setrange"""
    """IT THEN ITERATES THROUGH THE RANGE AND DIVIDES ALL NUMS BY numdivby WHICH IS SET BY inputnumdivby function."""

    returnlist = []
    for num in numlist:
        if num%numdivby == 0:
            returnlist.append(num)
        else:
            pass
    return returnlist



def prfinal():

    """THIS FUNCTION JUST DISPLAYS ALL THE RESULTS IN A PRESET PRINT."""

    print('\033[1m' + '\033[92m' + f'\n\n\n      Numbers divisible by {numdivby} are: {divnums}'+'\033[0m')
    print('\033[1m' + '\033[92m' + f'      Total count: {len(divnums)}'+'\033[0m')

#INPUTTING FUNCTIONS

def minmaxinput():

    """THIS FUNCTION TAKES USER INPUT AND WITH THE HELP OF setrange function, SETS THE MIN AND MAX RANGE OF TESTED NUMS"""

    minimum_input = input('\n\nPlease enter the minimum value of range to test: ')
    minimum = minimum_input.split()

    maximum_input = input('\nPlease enter the maximum value of range to test: ')
    maximum = maximum_input.split()

    minmax = list(zip(minimum,maximum))

    return minmax



def setrange(minmax_values):

    """THIS FUNCTION CONVERTS TUP INPUT FROM minmaxinput and unpacks it to be set into user_input_range and used in hmndb_calc function."""

    for a,b in minmax_values:
        min_val = int(a)

        max_val = int(b) + 1

    return list(range(min_val,max_val))



def inputnumdivby():

    """THIS FUNCTION WILL TAKE USER INPUT TO CONVERT INTO numdivby ARG USED IN hmndb_calc."""

    numdiv = input('\nPlease input num to test divisibilty: ')

    return int(numdiv)


def prevclose():
    prevclose_input = input('\n\nPress enter to close.')
    return(prevclose_input)

#THE PROGRAM WILL RUN IN THE FOLLOWING SEQ:
#FIRST WILL BE THE INPUT
minmax_values = minmaxinput()
user_input_range = setrange(minmax_values)
numdivby = inputnumdivby()

#AFTERWARDS WILL BE THE CALCULATION BY BACKBONE
divnums = hmndb_calc(user_input_range)

#FINALLY WILL BE THE DISPLAYS
prfinal()

#THIS IS TO PREVENT INSTA CLOSING OF TERMINAL
prevclose()
