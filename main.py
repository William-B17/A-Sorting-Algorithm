import json

with open('cars.json') as f:
   mcars = json.load(f)

cars = []

def fc1(color):
    if(color==0):
        print("No color selected")
    else:
        for i in mcars:
            if(mcars[i]["color"] == color):
                if i in cars:
                    print()
                else:
                    cars.append(i)

def fc2(miles):
    uando = miles[:1]
    mile = miles[1:]
    if(uando=="u"):
        for i in mcars:
            if(mcars[i]["miles"] <= int(mile)):
                if i in cars:
                    print()
                else:
                    cars.append(i)
    elif(uando=="o"):
        for i in mcars:
            if(mcars[i]["miles"] >= int(mile)):
                if i in cars:
                    print()
                else:
                    cars.append(i)
    else:
        print("No mile count selected")

def fc3(fuel):
    if(fuel == 0):
        print("No fuel selected")
    elif(fuel == "e" or "benzin"):
        for i in mcars:
            if(mcars[i]["fuel"] == fuel):
                if i in cars:
                    print()
                else:
                    cars.append(i)


#def sort():


    #print("""
    #Write your search criterias.

    #type 0 for everything under the category""")
    #c1 = input("1(color: \"red\",\"white\",\"black\"): ")
    #fc1(c1)
    #c2 = input("2(miles: \"o200\" = everything over 200,\"u200\" = everything under 200): ")
    #fc2(c2)
    #c3 = input("3(fuel: \"e\", \"benzin\"): ")
    #fc3(c3)
    #c4 = input("4(price \"500-8000\" everything over 500 and under 8000): ")
    #fc4(c4)

#sort()