from random import randint

class swiggy():
    def __init__(self):
        self.cart = {}
        self.curRes = ""
        self.history = {}
        self.totalItems  = 0
        self.NameOfResturent = {'naruto japanese spacial': {"fish": 125,
                                               "noodles": 130,
                                               "rice": 150},

                    'dbz hotel':                {"soup": 135,
                                                "rice": 155,
                                                "roti sabji": 160},

                   'naruto internation':       {"sushi": 170,
                                                "roti": 180,
                                                "samosa": 190}}
        print()
        print("#"*50 ,"HELLO, WELCOME TO SWIGGY", "#"*50)
        print("It would be great to know your name ")
        name = input()
        print("Hey", name,"You do looK hungry Let's Get you something to eat ASAP")
        self.mainMenu()

    def mainMenu(self):
        print("")   
        print("="*50 ,"MAIN  MENU", "="*50)
        print()
        print("SELECT ANY ONE OF THESE AVAILABLE OPTIONS")
        print()
        print("(1) ORDER FOOD \n"
              "(2) EXIT \n"
              "(3) ORDER HISTORY")
        while True:
            NumberForMainManu = int(input("Enter You selection :"))
            if NumberForMainManu == 1:
                self.renderHotelMenu(NumberForMainManu)
            elif NumberForMainManu == 2:
                print("Thank For using our services, Hope to see you again")
                exit()
            elif NumberForMainManu == 3:
                self.History()
            else: 
                print("Invalid input try again")

    def payment(self,amount):
        print()
        print(">"* 50, "WELCOME TO THE PAYMENT GATEWAY", "<"*50)
        print()
        print("AMOUNT TO BE PAID FOR YOUR SWIGGY ORDER RS", amount, "/-")
        print()
        print("AVAILABLE PAYMENT OPTIONS \n"
        "(C) CREDIT CARD \n"
        "(D) DEBIT CARD \n"
        "(N) NET BANKING \n"
        "(U) UPI \n"
        "(W) WALLETS \n"
        "(A) CASH ON DELIVERY")

        print("="*50)
        while True:
            inp = input().upper()
            if inp == "C" or inp == "D" or inp == "N" or inp == "U" or inp == "W":
                print("="*50)
                print()
                print("PAYMENT SUCCESSFULL")
                print("HURRAY, ORDER CONFIRMED")
                print()
                print("\n                 (H) ORDER HISTORY    (M) MAIN MENU    (E) EXIT")
                print("="*50)
                self.clearCart()
                while True:
                    inp1 = input("SELECT YOUR OPERATION: ").upper()
                    if inp1 == "M":
                        self.mainMenu()
                        break
                    elif inp1 == 'E':
                        exit()
                    elif inp1 == 'H':
                        self.History()
                        break
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")
                print("="*86)
                self.main_menu()
            elif inp == 'A':
                if amount > 499:
                    print("CASH ON DELIVERY IS NOT AVAILABLE FOR ORDERS ABOVE 499")
                    print("TRY AGAIN WITH DIFFERENT OPTIONS")
                else:
                    print("="*50)
                    print()
                    print("PLEASE PAY THE AMOUNT TO THE DELIVERY PARTNER")
                    print("HURRAY, ORDER CONFIRMED")
                    print()
                    print("\n                 (H) ORDER HISTORY    (M) MAIN MENU    (E) EXIT")
                    print("="*50)
                    self.clearCart()
                    while True:
                        inp1 = input("SELECT YOUR OPERATION").upper()
                        if inp1 == "M":
                            self.mainMenu()
                            break
                        elif inp1 == 'E':
                            exit()
                        elif inp1 == 'H':
                            self.History()
                        else:
                            print("INVALID INPUT PLEASE TRY AGAIN")
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")

    def showCart(self):
        print()
        print(">"*35, "CART", "<"*35)
        print()
        print("Resturant  Selected: " , ":".ljust(25),self.curRes)
        print()
        total = 0
        print( "Items".ljust(40), "Calculation".ljust(30))
        print()
        print("-"*50)
        print()
        for i in self.cart:
            curtotal = self.cart[i]["Quantity"] * self.cart[i]["Price"]
            total += curtotal
            print(i.ljust(40), self.cart[i]["Quantity"],
                "*", self.cart[i]["Price"], "=", curtotal)
        print()
        print('total >>>>>>', total, "/-")
        print("="*20," Main-M" , "Pay= P" ,"="*20)
        while True:
            userInp = input("Enter Your Choice: ")
            userInp = userInp.lower()
            if userInp == "m":
                self.mainMenu()
            if userInp == "p":
                order_no = randint(0,10000)
                self.history[order_no] = [self.curRes, total]
                self.payment(total)

    def clearCart(self):
        self.cart = {}
        self.curRes = ""
        self.totalItems  = 0

    def renderHotelMenu(self,NumberForMainManu):
        print("*"*50)
        if NumberForMainManu == 1:
            print("Some of the best available restaurant are this :")
            for key, value in enumerate(self.NameOfResturent):
                print(key+1,")",     value)  ##rs place problem

            print("="*20, "Main-M" ,"="*20)  ####### not working 

        hotelMenu = int(input("Enter your Choice :"))
        # # value = NameOfResturent['naruto']
        r = 0
        for key, value in self.NameOfResturent.items():
            r += 1
            if hotelMenu == r:
                itemMap = {}
                cur = 1
                for key1, value1 in value.items():
                    itemMap[str(cur)] = key1
                    print(cur,")",key1.ljust(30), value1, "/-")
                    cur += 1

                while True:
                    selection = input("Enter Your Order :") #2
                   
                    if(selection.isnumeric()):#yes
                       
                        if self.curRes == "":
                            self.curRes = key
                        else:
                            if self.curRes != key:
                                print("Your cart is cleared  as you seleceted item from diffrent restaurant")
                                self.clearCart()
                        quantity = int(input("How many do you want : "))
                        print("*************c-cart, m-menu************")
                        if(self.totalItems + quantity > 3):
                            print("Resurant cannot process more than three Item for one order")
                        else:
                            if itemMap[selection] in self.cart:
                                self.cart[itemMap[selection]]["Quantity"] += quantity
                            else:
                                self.cart[itemMap[selection]] = {
                                    "Price": self.NameOfResturent[key][itemMap[selection]], "Quantity": quantity}
                            self.totalItems += quantity
                    else:
                        try:
                            selection = selection.lower()
                            if(selection == "c"):
                                self.showCart()
                                break
                            elif(selection == "m"):
                                self.mainMenu()
                                break
                            else:
                                raise Exception("error")
                        except:
                            print("Invalid Input Try Again")

    def History(self):
            print()
            print(">"*33, " ORDER HISTORY","<"*33)
            if len(self.history) == 0:
                print("NO ORDERS YET")
                print()
                print("(M) MAIN MENU \n"
                "(E) EXIT")
                print("="*86)
            else:
                for i in self.history:
                    print("ORDER NUMBER = ", i)
                    print("RESTURANT -",self.history[i][0])
                    print("ORDER TOTAL =",self.history[i][1])
                    print("-"*30)
                    print("(M) MAIN MENU \n"
                    "(E) EXIT")
                    print("="*86)
            while True:
                r = input("SELECT A OPERATION: ").upper()
                if r == 'M':
                    self.mainMenu()
                elif r == 'E':
                    exit()
                else:
                    print("INVALID INPUT TRY AGAIN")
if __name__ == "__main__":
    swiggy()