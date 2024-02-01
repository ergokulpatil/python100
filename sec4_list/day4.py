# a=3
# b="hello"
# print(type(a))
# print(type(b))
#write progrma to select random name from list
import random
states=['Mh','Goa','KA','mp']
#print(states[0])
l=len(states)
choice= random.randint(0,l-1)
print(states[choice])
