
from distutils.command.build_scripts import first_line_re


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#extend - allows you to append another list to the end of list
#friends.extend(lucky_numbers)

#append - appends entitity to end of list
friends.append("Larry")

#insert - takes two parameters (pos, ent) and insents it into list at designated position
friends.insert(3, "Michelle")

#clear - clears all elements of list
#friends.clear()

#remove - removes entitiy from list
friends.remove("Kevin")

#pop - "pops" last element off of the list
#friends.pop()

#index - searches list for entity; prints position if found 
#print(friends.index("Karen"))

#count - counts the number of times entitiy appears in list
#print(friends.count("ent"))

#reverse - reverses order of entities in list
#friends.reverse()

#copy - makes a copy of the list
#friends.copy()
friends.sort()

print(friends)
