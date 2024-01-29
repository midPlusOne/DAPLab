#List operation
li1 = [1,2,3,4,5]
print("Original List: ",li1)
li1.append(6)
print("Appended: ",li1)
li2 = li1.copy()
print("Copied to li2: ",li2)
print("Count of 4 in li1: ",li1.count(4))
print("Index of 3 in li1: ",li1.index(3))
li1.insert(7,7)
print("Inserting 7 in 7th position: ",li1)
li1.remove(7)
print("Removing 7 from li1: ",li1)
li1.reverse()
print("Reversing li1: ",li1)
li1.clear()
print("Clearing li1: ",li1)
print("Length of li2: ",len(li2))
print("Max in li2: ",max(li2))
print("Min in li2: ",min(li2))

tp = (1,2,3)
li1 = list(tp)
print("tuple: ",tp)
print("tp converted to list: ",li1)