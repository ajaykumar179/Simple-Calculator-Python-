a = int(input("enter the 1st value: "))
b = int(input("enter the 2nd value: "))

c = str(input("enter 1 for \"addition\"\nenter 2 for \"substraction\" \nenter 3 for \"multiplication\" \nenter 4 for \"division\"\n"))

match c:
    case "1":
        print(a+b)
    case "2":
        print(a-b)
    case "3":
        print(a*b)
    case "4":
        print(a/b)


