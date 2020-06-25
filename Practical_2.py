#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[4]:


def av_val(int1, int2, int3):
    return ((int1 + int2 +int3))/3


# ## Problem 2

# In[13]:


def even_values(list_of_integers):
    return len([x for x in list_of_integers if x%2 == 1])


# ## Problem 3

# In[49]:


def func_3(name, *args):
        if len(args) > 0:
            print(name + ", your average grade is " + str(sum(args)/len(args)))
        else: 
            print("No grades available for " + name)


# ## Problem 4

# In[85]:


class circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def getdesc(self):
        print("A", self.color, "circle with radius", self.radius)
a = circle(6, "blue")
circle.getdesc(a)


# ## Problem 5

# In[86]:


class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary
    def getfullname(self):
        return self.name, self.last_name
    def annualsalary(self):
        annual_salary = self.__monthly_salary*12
        if annual_salary > 100:
            print("High")
        else:
            print("Low")
a = Employee("Anna", "Smith", 10)
a.getfullname()


# ## Problem 6

# In[112]:


class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
    def compare_car(self, car_2):
        if int(self.max_speed) > int(car_2.max_speed):
            return "car1 is better than car2"
        elif int(self.max_speed) == int(car_2.max_speed):
            return "The two cars have the same max speed"
        else:
            return "car2 is better than car1"

        
car1 = Car("S-class", "white", 290)
car2 = Car("E-class", "black", 280)
car1.compare_car(car2)


# ## Problem 7

# In[117]:


class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("I can move")
class Dog(Animal):
    def move(self):
        print("I can run really fast")

cc = Dog("dog") 
cc.move()

