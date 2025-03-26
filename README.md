def fruit(colour,size,shape,sweet):
    if colour == "green" and size == "l":
        return("watermellon")
    elif colour == "green" and size == "m":
        return("apple")
    elif colour == "green" and size =="s":
        return("grape")
    elif colour == "yellow" and shape == "n":
        return("banana")
    elif colour == "yellow" and shape == "y" and size == "l":
        return("grapefruit")
    elif colour == "yellow" and shape == "y" and size == "s":
        return("lemon")
    elif colour == "red" and size == "m":
        return("apple")
    elif colour == "red" and size == "s" and sweet == ("y"):
        return("cherry")
    elif colour == "red" and size == "s" and sweet == ("n"):
        return("grape")
    else:
        return("unknown")

    



colour = input("what colour is the fruit?: ")
size = input("is the fruit small(s), medium(m) or large(l): ")
shape = input("is the fruit round (y)yes (n)no?: ")
sweet = input("is the fruit sweet? (y)yes (n)no : ")
whatFruit = fruit(colour,size,shape,sweet)
print("your fruit is : ",whatFruit)
