# a=10
# b=20
# if a > b:
#     print(a)
# elif a+b:
#     print(a*b)
# else:
#     print(b)
#
# a=(16,17,18)
# for i in a:
#    print(i)
# Example file for working with classes
# class myClass():
#     def method1(self):
#         print("Guru99")
#
#     def method2(self, someString):
#         print("Software Testing:" + someString)
# c=myClass()
# c.method1()
# c.method2("venu good at testing")


# def myfunc(n):
#   return lambda a : a ** n
#
# mydoubler = myfunc(3)
#
# print(mydoubler(6))

#multiplication table
number=int(input("enter the number to print table:"))
print("multiplication of number:",number)
count =1

while count<=20:
    # number=number*1
    print(number,'x',count,"=",number*count)
    count +=1