adj = ["red", "big", "tasty"]
fruits = ["apple", "banana","cherry"]
for i in adj:
    for j in fruits:
        if(i == "red" and j == "banana") :
            continue
        if(i == "big" and j == "cherry"):
            continue
        print(i, j, ";", end=" ")
        