# num = 1,2,3
#
# for num in range(2):
#     print(num)


# for num in range(0,10,2):
#    print(num)
# #range operator.....where 1st is the starting point,2nd end point and last one is the steps


####this showcase list function w.r.t. range generators
# my_list = list(range(0,22,2))
# print(my_list)


#
# index = 0
#
# for letter in 'abcde':
#     print("at index position {} the letter is {}".format(index,letter))
#     index += 1          #   #don't miss it (for iteration in elements of letters


###this prints the letters in words using for loop
# index = 0
#
# word = 'abcde'
#
# for letter in word:
#     print(letter[index])


######## #####enumerate func showcase
# word = 'abcde'
#
# for item in enumerate(word):
#     print(item)
######tuple forms


####breaking of tuples
# word = 'abcde'
#
# for index,letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')


# ####zip function
# my_list1 = [1,2,3]
# my_list2 = ['a','b','c']
# my_list3 = [200,200,300]
#
# for items in zip(my_list1,my_list2,my_list3):
#     print(items)


# ######suffle function i.e. a funtion in library 'random'
# from random import shuffle
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# shuffle(my_list)
# print(my_list)


# ####Random number from the computer....p.s. gave me 99 on my first favorrite number....
# from random import randint
#
# my_favorite_number = randint(0,1000)
# print(my_favorite_number)


# ####taking inputs from usuers using input funtion
#
# result = input("hay what's your favorite number:")
# print(result)
# print(type(result))             ####type is str because input funtion always takes inputs as string....Taddaaa!!!
#


# ####now to take inputs as intergers or floats
#
# result = int(input("hay!Enter an interger plese....because this is an integer type input:"))
# print(result)
# print(type(result))


#######NEW DAY NEW BEGINING

#
# st = 'Print only the words that start with s in this sentence'
#
# for word in st.split():
#     if word[0]=='s':
#         print(word)
# ####


# for x in range(11):
#     if x % 2 ==0:
#         print(x)


#
# for x in range(51):
#     if x % 3 ==0:
#         print(list[x])


#
# my_list = list(range(0,51,3))
# print(my_list)
# print(type(my_list))


# st = 'Print every word in this sentence that has an even number of letters'
# my_st = st.split()
# if word in my_st


# st = 'Print every word in this sentence that has an even number of letters'
#
# for word in st.split():
#     my_list = len(list(word))
#     if my_list % 2 == 0:
#         print(word)
#


##########FUUUUCCCKKKK look it's FizzBuzz

#
# for num in range(0,101):
#     if num%3 == 0 and num%5 == 0:
#         print("FizzBuzz")
#     elif num%3 == 0:
#         print("Fizz")
#     elif num%5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#
#


# st = 'Create a list of the first letters of every word in this string'
#
# print([word[0] for word in st.split()])


####FUNCTIONS



# def say_hello(name):
#     print(f"Hello {name}")
# say_hello("MVDZO")


#
# def addition(num1,num2):
#     result = num1 + num2
#     return result
# print(addition(5,7))

#
# def say_name(name = "default"):
#     print(f"hello {name}")
# say_name()









# # #
# def check_even_number(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#             pass
#     return False
# result = check_even_number([1,2,4])
# print(result)




# def check_even_number(num_list):
#     even_number =[]
#     for number in num_list:
#         if number % 2 == 0:
#             even_number.append(number)
#         else:
#             pass
#     return even_number
#
# result = check_even_number([5,3,2,1,4,6])
# print(result)



######PROGRAM THAT EVALUATES BEST EMPLYEE

# employee = [('maina',200),('mithu',400),('jantu',100),('su',800)]
#
# def check_employee(employee):
#     current_max = 0
#     employee_name = ''
#
#     for name,hours in employee:
#         if hours>current_max:
#             current_max = hours
#             employee_name = name
#         else:
#             pass
#     return (employee_name,current_max)
#
# result =check_employee(employee)
# print(result)


#
# stock = [('apple',100),('goog',400),('micsft',200)]
#
#
# def stock_func(stock):


######coding excercise
# name = input("what is your name:")
# def greet():
#     print(f'my name is {name}'.format(name))
#     return (name)
# greet()


# def myfunc(a):
#     if a == True:
#         return 'Hello'
#     elif a == False:
#         return 'Goodbye'
# my_true = print(myfunc(a=True))
# my_false = print(myfunc(a=False))

#
# def myfunc(*args):
#     my_list = []
#     for number in args:
#         if number % 2 ==0:
#             my_list.append(number)
#     return my_list
# result = print(myfunc(1,2,3,4,5))



# def myfunc():
#     print("Hello World!")
# result = myfunc()


#
# def myfunc(*args):
#     out = []
#     for num in args:
#         if num%2==0:
#             out.append(num)
#     return out
# result = print(myfunc(1,2,3,4,5))



#
# name = input("what is your name:")
# def greet():
#     print('my name is:'.format(name))
#     return (name)
# greet()




# def myfunc(a):
#     if a == True:
#         return 'Hello'
#     elif a == False:
#         return 'Goodbye'
# my_true = print(myfunc(a=True))
# my_false = print(myfunc(a=False))



# def myfunc(x,y,z):
#     if z == True:
#         return x
#     else:
#         return y
# result = print(myfunc(1,2,3))

#
# def is_greater(a, b):
#     if a > b:
#         return True
#     elif not(a > b):
#         return False
# result = print(is_greater(30,20))

#
# def myfunc(*args):
#     print(sum(args))
#
# result = myfunc(10,20,30,40)


#
# def myfunc(*args):
#     return sum(args)
# result = myfunc(10,20,30,40)
# print(result)


#
# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)
# result =print(myfunc('abcd'))



# from this/any list print the even nos
# list = [2, 6, 7, 46,23, 0, 56, 67, 76]
#
# list = [2, 6, 7, 46,23, 0, 56, 67, 76]
#
# def is_even(list):
#     list = [2, 6, 7, 46, 23, 0, 56, 67, 76]
#     for number in list:
#         if number % 2 != 0:
#             print(number,end=" ")
#         else:
#             pass
# is_even(list)



#
# def is_less(a,b):
#     if a%2 == 0 and b%2 == 0:
#         #both are even
#         if a > b:
#             result = b
#         else:
#             result = a
#     else:
#         #one or both numbers are odd
#         if a < b:
#             result = a
#         else:
#             result = b
#     return result
#
# num = is_less(3,7)
# print(num)


#######another way is to use min (and max for maximum) func
# #
# def is_less(a,b):
#     if a%2 == 0 and b%2 == 0:
#         if a < b:
#             return min(a,b)
#     else:
#         return min(a,b)
# num = is_less(-3,5)
# print(num)

#
# def is_less(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else:
#         return min(a,b)
#
# num = is_less(1,4)
# print(num)






