
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#extend - allows you to append another list to the end of list
#friends.extend(lucky_numbers)

#append - appends entitity to end of list
friends.append("Larry")

#insert - takes two parameters (pos, ent) and insents it into list at designated position
friends.insert(3, "Michelle")

#remove - removes entitiy from list
friends.remove("Kevin")
print(friends)