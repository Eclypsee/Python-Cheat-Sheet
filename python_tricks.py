##############################################################################
# # example unit test code. put this into a new file.
# import unittest
# class ExampleTest(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(3, 3) # expected, actual
#     def test_2(self):
#         self.assertAlmostEqual(3.00000001, 3.00000002) # expected, actual
# if __name__ == '__main__':
#     unittest.main()


##############################################################################
# remember == checks if 2 variables are equal
# while the "is" operator checks if they are in the same memory


##############################################################################
# example function with docstring
def example(k:int, j:int)->int:
    """example docstring"""
    print("example:", k+j, "apples")


##############################################################################
print("##################################### class definition ################################")
class Point:
    def __init__(self, x:int, y:int)->None:
        self.x = x
        self.y = y

    def __str__(self)->str: # allows you to print the object. also __repr__ does same thing. repr means representation
        return f'({self.x}, {self.y})' # f string allows you to put anything in here

    def __eq__(self, otherthing:object):# when you call ==
        if not isinstance(otherthing, Point):
            return False
        return self.x == otherthing.x and self.y == otherthing.y

print(Point(4, 6)) 
p = Point(4, 6)
k = Point(4, 6)
print(p)
print(p==k)


##############################################################################
# main guard. if the python file is imported, do not run the below
if __name__ == '__main__':


    ##############################################################################
    print("##################################### precedence ######################################")
    # logical operations / order / precedence
    # 1. PEMDAS
    # 2. relational operators <>,  ==,  is
    # 3. logical stuff NOT first, AND second, OR last
    print("operational order: ", not True and False or True>1+1)


    ##############################################################################
    print("##################################### function call ###################################")
    # calling the example function
    example(3, 5)


    ##############################################################################
    # pass statement
    for i in range(10):
        pass
    if (True):
        pass


    ##############################################################################
    print("##################################### boolean #########################################")
    # booleans
    # true is 1 and false is 0
    # true is also a non empty string and false is an empty string
    if True<5:
        print('since True is 1, 1 is less than 5')
    if "" or " ":
        print("empty string or string means false or true, which is true")


    ##############################################################################
    print("##################################### for loop ########################################")
    # for loop
    for i in range(10, 30, 2):
        print("loop:", i)


    ##############################################################################
    # while loop
    while 'asdf' == 'hello':
        continue  # this loops back to the beginning, skipping the print statement
        print('hello')


    ##############################################################################
    print("##################################### strings #########################################")
    # strings
    example = "abcdefg"
    # this splicing [1:6] means you start at index 1 and end at index 6
    print(example[1:6])
    # 3rd index to the last term
    print(example[3:-1])


    ##############################################################################
    print("##################################### arrays and loops and lists ######################")
    # Arrays and Lists, looping through them
    # [{expression} for {iterator} in {sequence} {(this is optional) if iterator:  do something}]
    # this bottom one meanas your square x, for every x in the array. returns 1, 4, 9, 16
    print("the result: ", [x ** 2 for x in [1, 2, 3, 4]])
    # returns 9, 16 because the rest of the numbers in the array are less than 2
    print("the result: ", [x ** 2 for x in [1, 2, 3, 4] if x>2])


    ##############################################################################
    maps = "################################# map filter and fold #################################"
    # map [1, 2, 3]---->do something to the values(output same len)----->[1.0, 2.0, 3.0]
    # filter [1, b, 2, d, 3, a, 4]---->do something to filter values out---->[1, 2, 3, 4]
    # fold [1, 2, 3, 4]--->add all values--->1+2+3+4---->10
    # lists passed into functions are the same list. its not a copy
    # swap in place means swap values without creating a new list. swap out of place means create a copy list


    ##############################################################################
    print("##################################### sorting algorithms ###############################")
    l1 = [5, 4, 3, 7, 2, 1, 5, 7]

    #selection sort
    ls = l1[:]
    for i in range(len(ls)):
        min_i = i
        for j in range (i, len(ls)):
            if ls[j]<ls[min_i]:
                min_i = j
        ls[min_i], ls[i] = ls[i], ls[min_i]
    print('selection sorted')

    # insertion sort
    ls = l1[:]
    for i in range(len(ls)):
        for j in range(i, 0, -1):
            if ls[j]<ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
    print('insertion sorted')

    ##############################################################################
    print("##################################### file reading #####################################")
    # reads a file hello.txt and makes removes extraneous spaces
    # then this writes the output to output.txt. it creates the file if it does not exist, and appends to it
    with open('hello.txt') as f:
        with open('output.txt', 'a') as t:
            for line in f:
                line = line.strip()# removes leading and trailing whitespace characters
                if not line == '':
                    previous_element = ''
                    for element in line:
                        if not previous_element == ' ' or not element == ' ':
                            t.write(f'{element}')
                            print(element, end="")
                        previous_element = element
                    t.write(f'\n')
                    print()
            t.write(f'\n')