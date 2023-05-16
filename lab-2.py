#Py-datatypes-lab-2




#Question1#

#Make a list with 3 elements
List1=[0,1,2]
#print(List1)
#add an element to the end of list
List1.append(3)
#print(List1)
#remove an element from the list
List1.remove(0)
##print(List1)
#reverse the list
List1.reverse()
#print(List1)
#sort the list
List1.sort()
#print(List1)
#add an element at the start of the list
List1.insert(0,-1)
#print(List1)
#print the index of the last element
print(len(List1)-1)
#print(List1)








#Question 2:

#Consider the following list:
people = ["Ahmed", "Nasser", "Mohammed"]

#print the list in the following format: Ahmed, Nasser, Mohammed
print(', '.join(people)) 









#Question 3:

#Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
List3=[ {'name':"Maymoonah1" , 'phone':"0155555"} , {'name':"Maymoonah2" , 'phone':"0255555"}  
       ,{'name':"Maymoonah3" , 'phone':"0355555"}  ]
#print(List3)

#now add 1 more dictionary to the list
List3.append({'name':'Maymoonah4' , 'phone':'0455555'} )
#print(List3)


#now delete the name from the first dictionary
del List3[0]
#print(List3)


#update the phone number of the last person
List3[-1]="{'name':'Maymoonah4' , 'phone':'0955555'}"
#print(List3)

#check if a first dictionary has a key called "name"
print("name" in List3[0])
