'''
Created on 17-Sep-2019

@author: Dell
'''
print('hello')
print("I'm going out")


''' Escape Sequence'''
print('hello \nworld')
print('hello \tworld')

''' len function'''
print(len('hello'))

''' String Slicing & indexing'''
mystring="Hello World"
print(mystring[0])
print(mystring[8])
print(mystring[9])
print(mystring[-2])

mystring='qwertyuiop'
print(mystring)
print(mystring[2:]) #all the way to end
print(mystring[:3]) #all the way from front upto but on include
print(mystring[2:6]) #from the middle
print(mystring[::]) #Start : Stop : Step-size
print(mystring[::2]) #2 is the step-size here
print(mystring[::-1]) #reversing the string

'''immutable'''
name="Sam"
firstname=name[1:]
print(firstname)
print('P' + firstname)

'''String Methods'''

x='Hello World'
print(x.upper())
print(x.lower())
print(x.split())
x='Hello World'
print(x.split('e'))

''' .format() method'''
print('this is a new {}'.format('Programming language'))
print('the {1} {2} in the {0}'.format('east','sun','rises'))
print('the {s} {r} in the {e}'.format(e='east',s='sun',r='rises'))

''' float formatting'''
result=100/777
print(result)
print('result was {r}'.format(r=result))
print('result was {r:1.3f}'.format(r=result))

'''string literal method'''

name='Nikhil'
age=22
print('hello my name is {}'.format(name))
print(f'hello my name is {name}')
print(f'{name} is {age} years old')