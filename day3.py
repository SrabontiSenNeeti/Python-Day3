#math function
import math
a= 50.6
print(math.ceil(a))
print(math.floor(a))
print(math.e)
print(math.pi)
print(math.tau)

#Area
r=3 #radius
pie = math.pi
print(pie*r*r) #area

#Factorial
a=5
print(math.factorial(a))


#Finding the absolute Value
a= -20
print(math.fabs(a))
print(abs(a))


#Finding the power of exp
a = 4
b = -3
c = 0.0
print(math.exp(a))
print(math.exp(b))
print(math.exp(c))

#finding the power of a number
a = 3
b = 4
print(pow(a,b))
print(pow(3,3))

#Finding the Logarithm
a = 2
b = 3
print(math.log(a,b))
print(math.log2(16))
print(math.log10(10000))


#Finding the square root
print(math.sqrt(0))
print(math.sqrt(4))
print(math.sqrt(9.5))


#Trigonomatric and Angular functions
a=math.pi/6
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))

print(math.sin(30))
print(math.cos(30))
print(math.tan(30))

#Converting values from degree to radians and vice versa
a = math.pi/6
b = 30
print(math.degrees(a))
print(math.radians(b))

#Finding gamma value
a = 6
print(math.gamma(a))



#Expression and Statement
"""
a = 4
b = a+4
c = a-1
operator er pore ja thake seti holo expression ex: a-1 ar puro ta holo statement ex: c = a-1
"""


#augmented assignment Operator

a = 2
b = a+1
a = a+1
a+=1
#eta k amra a+=1 eta likhte pari.
#this is called augmented assignment operator
print(b)
print(a)


#Long STring er khetre 3 ta quotation use kora jai
name = """
this is long
string
line
"""
print(name)

#new tab er jonno \t
name = """
\t this is long
string
line
"""
print(name)

#new line er jonno \n
name = """
this is \ncalled long
string
line
"""
print(name)


#Concatenation(+sign used in concatenation)
name = "Neeti"
surname = "Sen"
print(name+surname)
print(name +" "+ surname)


#type Conversion
a = 14
b = 14.02
c = 'ff'
noneValue = None
print(type(b))
print(type(b))
print(type(c))
print(type(noneValue))


#Formatted String
name = "Neeti"
age = "23"
print(f"Greetings, Welcome to GITHUB!!! {name}.You are in.Your {age}")
#or
print("Greetings,Welcome to Github!"+name+"."+"Your"+ age)
#or
print("Greetings,welcome to GITHub! {}.You are in.Your {}".format(name,age))
#or
print("Greetings,welcome to GITHub! {0}.You are in.Your {1}".format(name,age))
#or
print("Greetings,welcome to GITHub! {1}.You are in.Your {0}".format(name,age))

#String er majhe ' thakle
print("It's a Nice Name")


#String Index
name = "Srabonti Sen Neeti"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name)

#[start point thakbe ai bracket er majhe]
#[Start er por : dile hobe stop hobe]
#[start:stop]
name = "neeti"
print(name[0:3])  #print item before 3 no index
print(name[0:])
print(name[1:4])
print(name[:2])

#[start:stop:step]
name= "THis is your class time"
print(name[0:5:1])
print(name[0:15:2])
print(name[0:15:3])
print(name[0:15:4])
print(name[0:23:5])
print(name[::2])
print(name[::3])
print(name[::-1])
print(name[::-2])
print(name[::-3])

#step a (-) dile reverse hoy
name ='123456789'
print(name[::-1])




#dosomic er por amra j koy ghor rakhte chai
print(round(3.566666666,2))
print(round(3.566666666,3))
print(round(3.566666666,3))
print(round(3.566666666,5))









