# # list_numbers = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12,13,14,15,16,17,18]
# #
# # list1 = list_numbers.index(0:1)
# # print(list1)
# #
#
#
#
#
# indices = [1, 4, 9, 16]
# templist = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
# sublist = []
#
# for i in indices:
#     sublist.append(templist[0][i])
#     print(i)





# indices = [0, 1, 4, 9,16,25, 36,49, 64]
# templist = [list(range(0,65))]
# sublist = []
#
# for i in indices:
#     sublist.append(templist[0][i])
#     print(i)




# a = int(input())
# b = int(input())
#
#
# print(a//b)
# print(a/b)




#
# a = int(input())
# for num in range(0,a+1):
#     print(num, end='')



# print("enter a number:")
# a = int(input())
#
# print("enter another number:")
# b=int(input())
#
# print("Press 1 for addition:")
# print("2 for substraction:")
#
# add =int(input())
# if add==1:
#     print((a + b)
#
# if sub==2:
#     print(a - b)



#
# My_list = [2 ,4 ,5,7,2,4,6,8,9,]
#
# sorted_list =(My_list)
# print(sorted_list)
#
#
#
# year = int(input("enter year: "))
# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         print(year,"is a leap year")
#     elif year % 400 == 0:
#         print("it's a leap year")
#     else:
#         print(year,"is not a LEAP year")
#
#
# is_leap(year)
#


year = int(input("Enter a year: "))
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year,"is a leap year")
    elif year % 400 == 0:
        print("it's a leap year")
    else:
        print(year,"is not a LEAP year")

is_leap(year)
