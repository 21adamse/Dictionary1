countries={
    "UK":"London",
    "France":"Paris",
    "China":"Bejing",
    "USA":"Washington DC",
    "Japan":"Tokyo"
}
choice=""
while choice !="F":
    print("Would you like to:")
    print("A-Insert")
    print("B-Display all countries")
    print("C-Display all capitals")
    print("D-Get capital")
    print("E-Delete")
    print("F-End code")
    choice=input()
    if choice=="A":
        country=input("What country would you like to add: ")
        capital=input("What is it's capital: ")
        countries[country]=capital
    elif choice=="B":
        print(countries.keys())
    elif choice=="C":
        print(countries.values())
    elif choice=="D":
        countrychoice=input("Which country capital do you want to get")
        print(countries[countrychoice])
    elif choice=="E":
        countrydelete=input("Which country do you want to delete")
        del countries[countrydelete]
    else:
        print("Invalid input")