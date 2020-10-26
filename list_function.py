lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Kim", "Mark", "Jim", "Oscar", "Pierre"]
# extend add both array to the list at the end
# friends.extend(lucky_numbers)
friends.sort()
print(friends)
# append add something to the list at the end
friends.append("Creed")
print(friends)
# insert add something to the list at the anywhere u want
friends.insert(1, "Kelly")
print(friends)
# remove delete something to the list
friends.remove("Jim")
print(friends)
# pop will pop off an item on the list
friends.pop()
print(friends)
print(friends.index("Oscar"))
print(friends.count("Kim"))
friends.extend(lucky_numbers)
print(friends)



