#Write a program to determine the type of input using match statement.
data= eval (input("enter data:"))
match data :
    case bool():
        print("boolean")
    case int():
        print("int")
    case float():
         print ("float")
    case str():
        print("str")
    case list():
        print("list")
    case dict():
        print("dict")
    case set():
        print("set")
    case tuple():
        print("tuple")
    case none:
        print("none")
    
    