# # n= int(input("enter number : "))

# # fact = 1
# # for i in range(1, n+1):
# #     fact*=i

# # print(" factorial : " , fact)
# # def cal_sum(a , b):
# #     sum = a + b
# #     print (sum)
# #     return sum
# # cal_sum(20, 10)

# # cal_sum(18,19)

# # def cal_sum():
# #     print("hello")
# #     return
# # cal_sum()

# # dsfggr
# # cities = ["a" , "b" , "c"]
# # heroes = ["d" , "e" , "f"]

# # def print_len(list):
# #     print(len(list))

# # def print_list(list):
# #     for item in list:
# #         print(item, end=" ")
 
# # print_list(heroes)
# # def cal_fact(n):
# #     fact = 1
# #     for i in range(1, n+1):
# #         fact *=i
# #     print(fact)

# # cal_fact(5)
# # def fact(n):
# #     if (n==1 or n==0):

# #         return 1                                   #recurssion

# #     return fact(n-1) * n


# # print(fact(4))




# # f = open("demo2.txt" , "r")
# # data = f.read()
# # print(data)
# # print(type(data))
# # f.close()


# # f = open("demo2.txt", "r")
# # data= f.read()
# # print(data)
# # line1 = f.readline()
# # print(line1)
# # line2 = f.readline()
# # print(line2)


# # f.close()

# # f = open("demo2.txt", "a+")
# # print(f.read())
# # f.write("1433")



# # f.close()


# # with open("demo2.txt", "w") as f:
# #     f.write("hello world")


# # import os

# # os.remove("demo2.txt")


# # with open("dem3.txt", "r") as f:
# #     data = f.read()
    
# # new= data.replace("hello" , "hi")
# # print(new)

# # with open("dem3.txt", "w") as f:
# #     f.write(new)
# # def check_for_word():
    
# #     word = "world"
# #     with open("dem3.txt", "r") as f:
# #         data = f.read()
# #         if(data.find(word) != -1):
# #             print("word found")
# #         else :
# #             print("not found")

# # def check_for_line():
# #     word = "hi"
# #     data  = True
# #     line_no = 1
# #     with open("dem3.txt", "r") as f:
# #         while data:
# #             data = f.readline()
# #             if(word in data):
# #                 print(line_no)
# #                 return
# #             line_no +=1

# #     return -1
# # print(check_for_line())

# # class student:
# #     name = "karan verma"

# # s1 = student()
# # print(s1.name)

# # class car:


# #     color = "red"
# #     model = "2020"
# #     make  = "honda"

# # car1 = car()
# # print(car1.color)
# # print(car1.model)
# # print(car1.make)


# # class student:
# #     college = "abc"
# #     name ="anonymous" 
# #     def __init__(self, name , marks):
# #         self.name = name
# #         self.marks = marks
# #         print("student created")

# # s1 = student( "kaju", 90)
# # print(s1.name, s1.marks)

# # s2 = student("rahul" , 80)
# # print(s2.name , s2.marks)

# # print(student.college)
# # print(student.name)

# # class student:
# #     def __init__(self, name , marks):
# #         self.name = name
# #         self.marks = marks

# #     @staticmethod
# #     def hello():
# #         print("hello there")
        
# #     def get_avg(self):
# #         sum = 0
# #         for val in self.marks:
# #             sum += val
# #         print("hi", self.name, "your avg is : ", sum/len(self.marks))


# # s1 = student("karan" , [90, 80, 70])
# # s1.get_avg()
# # s1.hello()  # This will print "hello there"


# # class car:
# #     def __init__(self, color , model , make):
# #         self.color = color
# #         self.model = model
# #         self.make = make

# #     def start(self):
# #         print("car started")

# #     def stop(self):
# #         print("car stopped")

# #     def accelarate(self):
# #         print("car accelarating")

# # car1 = car("red" , "2020" , "honda")
# # print(car1.color)
# # car1.start()
# # car1.accelarate()
# # car1.stop()


# # class car:
# #     def __init__(self):
# #         self.acc = False
# #         self.brk = False
# #         self.clutch = False

# #     def start (self):
# #         self.clutch = True
# #         self.acc = True
# #         print("car started")

# # car1 = car()
# # car1.start()


# # class account:
# #     def __init__(self, bal, acc):
# #         self.balance = bal
# #         self.acc_no = acc
    
# #     def debit(self, amt):
# #         self.balance -= amt
# #         print("debited : ", amt)
# #         print("current balance : ", self.get_balance())

# #     def credit(self, amt):
# #         self.balance += amt
# #         print("credited : ", amt)
# #         print("current balance : ", self.get_balance())

# #     def get_balance(self):
# #         return self.balance
    
# # acc1 = account(1000 , "12345")
# # acc1.debit(200)     
# # acc1.credit(500)
# # acc1.debit(100)
# # print("final balance : ", acc1.get_balance())


# # class student:
# #     def __init__(self, name):
# #         self.name = name
        
# # s1 = student("karan")
# # print(s1.name)  
# # del s1
# # print(s1.name)  # This will raise an error since s1 is deleted


# class car:
#     colr = "red"
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod                                         ##single inheritance
#     def stop():
#         print("car stopped")

# class toyota(car):
#     def __init__(self, brand):
#         self.brand = brand

# car1 = toyota("fortuner")
# car2 = toyota("prius")

# print(car1.colr)


# class car:

#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod                          
#     def stop():
#         print("car stopped")

# class toyota(car):
#     def __init__(self, brand):
#         self.brand = brand                             ##multilevel inheritance


# class fortuner(toyota):
#     def __init__(self, model):
#         self.model = model

# car1 = fortuner("2020")
# print(car1.model)
# car1.start()
# car1.stop()



# class A:
#     varA= "I am class A"

# class B:
#     varB = "I am class B"

# class C(A, B):                             ##multiple inheritance
#     varC = "I am class C"

# c1= C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

class car :
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    def stop(self):
        print("car stopped")    

class toyota(car):
    def __init__(self, name , type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop()

car1 = toyota("fortuner" , "suv")
print(car1.name)
print(car1.type)
car1.start()
car1.stop()

