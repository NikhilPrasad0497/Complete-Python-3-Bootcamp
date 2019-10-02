'''LISTS'''
my_list1=[1,2,3]
print(len(my_list1))
print(my_list1[0])
print(my_list1[1:])

my_list=['String',100,2,3]
print(len(my_list))
print(my_list[0])
print(my_list[1:])

print(my_list+my_list1)
print(my_list)
my_list[0]='STRING ALL CAPS'
print(my_list)
my_list1.append('six')
print(my_list1)
'''remove from last'''
print(my_list1.pop()) 
print(my_list1)
print(my_list1.pop(0))

'''sort method 
    Note this method cannot be assigned to a variable
'''
new_list=['u','a','i','e','o']
new_list1=[5,3,1,4,2]
new_list.sort()
print(new_list)

'''reverse()'''

new_list1.reverse()
print(new_list1)
