#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[ ]:


def my_max(*args):
    """my_max function takes undefined number of non-keyword
    arguments as inputs and returns the maximum value out of those"""
    if len(args) == 0:
        return "no numbers given"
    else:
        max_value = args[0]
        for arg in args:
            if arg > max_value:
                max_value = arg
            else:
                pass
    return max_value


# ## Problem 2

# In[ ]:


def unique_list_maker(list_object):
    """unique_list_maker function takes a list as an input 
    and returns another list which contains only the 
    unique elements of the original list"""
    unique_list = []
    for i in list_object:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


# ## Problem 3

# In[ ]:


def my_fib(n):
    """my_fib takes the input n in a form of positive integer and then calculates 
    and returns the n-th fibonnaci number. 
    However, this function has a limit: 0 <= n <= 100
    So, n should be an integer less than 101 and should not be negative"""
    if n == 1 | n == 2:
        return 1
    elif (n <= 0) | (n > 100):
        return "Fibonacci sequence does not have that element or your input is more than 100"
    else:
        fib_numbers_list = [1,1]
        counter = 0
        while counter <= 97:
            fib_numbers_list.append(fib_numbers_list[-1] + fib_numbers_list[-2])
            counter += 1
        return fib_numbers_list[n-1]
    
    
print(my_fib(0))
print(my_fib(14))
print(my_fib(-4))


# ## Problem 4
# 

# In[ ]:


class Person:
    def __init__(self, name, last_name, age, gender, student, __password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = __password
        
    def Greetings(self, second_person):
        print("Welcome dear", second_person.name)
        
    def Goodbye(self):
        print("Bye everyone!")
        
    def Favourite_num(self, num1):
        return "My favourite number is", num1
    
    def Read_file(self, filename):
        file = filename+".txt"
        open(file)
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def get_password(self):
        return self.__password
    
    
std_1 = Person("Ruben", "Mkrtchyan", 20, "male", True, "qwerty12345")
std_2 = Person("Hayk", "khachatryan", 33, "male", False, "abcdefg123")
std_1.Greetings(std_2)
std_1.Goodbye()
std_2.Favourite_num(8)
std_1.Read_file("text")
std_2.set_password("Hayk33")
std_2.get_password()


# ## Problem 5

# In[ ]:


class Calculation:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        print(self.x + self.y)
    
    def subtraction(self):
        print(self.x - self.y)
        
class MyCalculation(Calculation):
    
    def multiplication(self):
        print(self.x * self.y)
    
    def division(self):
        print(self.x / self.y)

        
a = MyCalculation(3,5)
a.addition()
a.subtraction()
a.multiplication()
a.division()
        

