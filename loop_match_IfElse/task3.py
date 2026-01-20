#enter number of month name from user nd display days accordingly with in operator 
month=input("enter month name to print days")
match month:
    case  month if month in("jan","march","may","july","aug","oct","dec"):
        print("31 days")
    case month if month in("april","jun","sep","nov"):
        print("30 days")
    case "fab":
        print("28 days")
    case _:
        print("invalid")
