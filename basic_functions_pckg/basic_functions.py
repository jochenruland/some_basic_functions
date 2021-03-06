import math
import numpy as np

def calcuate_7_5():
    """ Calculates all such numbers which are divisible by 7 but are not a multiple of 5,
        between lowervalue and uppervalue (both included). The numbers obtained will be printed
        in a comma-separated sequence on a single line """
    lowervalue = int(input('lower value:'))
    uppervalue = int(input('upper value:'))
    value_list = []
    for i in range(lowervalue, uppervalue + 1):
        if (i %7 == 0) and (i %5 != 0):
            value_list.append(str(i))
            i += 1
        else:
            i += 1

    return print(', '.join(value_list))

def fact(x):
    ''' Function which can compute the factorial of a given numbers.
        The results will be printed in a comma-separated sequence on a single line
        Suppose the following input is supplied to the program: 8 Then, the output should be: 40320'''
    fact_no = x
    result = 1

    while fact_no > 0:
        result = result * fact_no
        fact_no -= 1

    return result

def create_dict(n):
    ''' With a given integer number n, the function generates a dictionary that contains (i, i*i)
        such that is an integral number between 1 and n (both included).
        And then the program should print the dictionary. Suppose the following input is supplied
        to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
    tmp_dict = dict()

    for i in range(1, n+1):
        tmp_dict[i]=i*i
        i+=1

    return tmp_dict

def create_list_tuple(s):
    ''' The function accepts a sequence of comma-separated numbers from console
        and generates a list and a tuple which contains every number.
        Suppose the following input is supplied to the program: 34,67,55,33,12,98
        Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
        With tuple() method can convert list to tuple '''
    tmp_list = s.split(',')
    t=tuple(tmp_list)
    return tmp_list, t

class Additionalstringmethods:
    ''' Define a class which has at least two methods
        Also please include simple test function to test the class methods.'''
    def __init__(self, i_str=''):
        self.input_str = i_str

    def getString(self):
        ''' getString: to get a string from console input'''
        self.input_str = input('write whatever you like:')


    def printString(self):
        ''' printString: to print the string in upper case '''
        new_string = self.input_str.upper()
        print(new_string)


# calcuate_7_5()
#x=int(input('Integer to calculate factorial:'))
#print(fact(x))
#n = int(input('Integer to create dict:'))
#print(create_dict(n))
#s = input('Enter comma separated numbers:')
#print(create_list_tuple(s))

#string_obj = Additionalstringmethods('test')
#string_obj.getString()
#string_obj.printString()



#def test_Additionalstringmethods():
#    t_object = Additionalstringmethods('bullshit')
#    assert(t_object.printString()==print('BULLSHITt'))

#test_Additionalstringmethods()

def squareroot_2_50_s_30(s):
    ''' A program that calculates and prints the value according to the given formula:
        Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30.
        D is the variable whose values should be input to your program in a comma-separated sequence.
        Example Let us assume the following comma separated input sequence is given to the program: 100,150,180
        The output of the program should be: 18,22,24
        Hints: If the output received is in decimal form, it should be rounded off to its nearest value
        (for example, if the output received is 26.0, it should be printed as 26)
        In case of input data being supplied to the question, it should be assumed to be a console input. '''

    input_list = s
    output_list = []

    for i in input_list:
        calc = round(math.sqrt(2 * 50 * float(i)/30))
        output_list.append(str(calc))

    return print(','.join(output_list))

#s = [x for x in input('comma separated integer').split(',')]
#squareroot_2_50_s_30(s)

def create_2_dim_array(dims):
    ''' A program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
        The element value in the i-th row and j-th column of the array should be i*j.
        Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5
        Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form '''

    rowNum=int(dims[0])
    colNum=int(dims[1])

    list_transform = [[0 for col in range(colNum)] for row in range(rowNum)]

    for i in range(rowNum):
        for j in range(colNum):
            list_transform[i][j]=i*j
            j+=1
        i+=1

    return print(list_transform)

# a_dims = [int(x) for x in (input('Enter 2 dimensions separated by comma: ').split(','))] # Transforms string into integer directly after input
# create_2_dim_array(a_dims)

def sort_word_list(s):
    ''' A program that accepts a comma separated sequence of words as input
        and prints the words in a comma-separated sequence after sorting them alphabetically.
        Suppose the following input is supplied to the program: without,hello,bag,world
        Then, the output should be: bag,hello,without,world '''
    sorted_list = sorted(s)
    return print(','.join(sorted_list))

# input_list = [x.upper() for x in input('Enter comma separated words: ').split(',')]
# sort_word_list(input_list)

def capitalized_char():
    ''' A program that accepts sequence of lines as input and prints the lines
        after making all characters in the sentence capitalized.
        Suppose the following input is supplied to the program: Hello world Practice makes perfect
        Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT '''
    input_list = []
    while True:
        s = input()
        if s:
            input_list.append(s.upper())
        else:
            break
    #return [print(sentence) for sentence in input_list]
    return print(' '.join(input_list))

#capitalized_char()

def remove_duplicates():
    ''' A program that accepts a sequence of whitespace separated words as input and prints the words
        after removing all duplicate words and sorting them alphanumerically. Suppose the following
        input is supplied to the program: hello world and practice makes perfect and hello world again
        Then, the output should be: again and hello makes perfect practice world
        We use set container to remove duplicated data automatically and then use sorted() to sort the data.'''
    input_list = []

    while True:
        s = input('write whatever you want in mulitple lines: ')
        if s:
            input_list.append(s.split(' '))
        else:
            break

    output_list = []
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            output_list.append(input_list[i][j])
            j+=1
        i+=1

    output_list = sorted(set(output_list))

    return print(' '.join(output_list))

#remove_duplicates()

def four_digit_div_5():
    ''' A program which accepts a sequence of comma separated 4 digit binary numbers
        as its input and then check whether they are divisible by 5 or not.
        The numbers that are divisible by 5 are to be printed in a comma separated sequence.
        Example: 0100,0011,1010,1001 Then the output should be: 1010
        Notes: Assume the data is input by console. '''
    input_list = []
    for x in input('comma separated 4 digtit binary numbers: ').split(','):
        input_list = int(x, 2)

    output_list = []
    for value in input_list:
        if not value%5:
            output_list.append(str(value))

    return print(','.join(output_list))

#four_digit_div_5()

def find_no_digits_even(lowervalue, uppervalue):
    ''' A program, which will find all such numbers between 1000 and 3000 (both included)
        such that each digit of the number is an even number.
        The numbers obtained should be printed in a comma-separated sequence on a single line '''
    output_list = []
    for i in range(lowervalue, uppervalue+1):
        s = str(i)
        for j in range(len(s)):
            if int(s[j])%2==0:
                j+=1
            else:
                break
        if j == len(s):
            output_list.append(s)

    return print(','.join(output_list))

#find_no_digits_even(4000,5000)

def calculate_no_letters_digits(s):
    ''' A program that accepts a sentence and calculate the number of letters and digits.
        Suppose the following input is supplied to the program: hello world! 123
        Then, the output should be: LETTERS 10 DIGITS 3 '''
    dict = {'LETTERS': 0, 'DIGITS' : 0}

    for c in s:
        if c.isalpha():
            dict['LETTERS'] += 1
        elif c.isdigit():
            dict['DIGITS'] += 1
        else:
            pass

    return print(dict)

input_str = input('Write a sentence with letters and digits: ')
calculate_no_letters_digits(input_str)
