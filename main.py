menu = {
    "hot dog": 2.50,
    "hamburger": 3.00,
    "fries": 1.50,
    "soda": 1.00,   
    "popcorn": 2.00,
    "chips": 1.25
    }

menu_combos = {
    "burger combo": {
        "items": ["hamburger", "fries", "soda"],
        "price": 4.50,
        "savings": 1.00
    },
    "hot dog combo": {
        "items": ["hot dog", "fries", "soda"],
        "price": 3.75,
        "savings": 0.75
    },
    "family combo": {
        "items": ["hamburger", "hot dog", "fries", "fries", "soda", "soda"],
        "price": 9.00,
        "savings": 2.00
    }
}
fries_type = {
    "curly": 0.50,
    "crinkle": 0.50,
    "shoestring": 0.50
    }

soda_flavor = {
    "cola": 0.25,
    "lemon-lime": 0.25,
    "orange": 0.25
    }

popcorn_flavor = {
    "butter":0.25, 
    "salt":0.25, 
    "cheese":0.25,

}
chips_flavor = {
    "classic": 0.00,
    "kettle-cooked": 0.25,
    "rippled": 0.30,
}

burger_ingredients = {
    "big mac": [
        "beef patty",
        "special sauce",
        "lettuce",
        "cheese",
        "pickles",
        "onions",
        "sesame bun"
    ],
    "quarter pounder with cheese": [
        "quarter pound beef patty",
        "ketchup",
        "mustard",
        "pickles",
        "onions",
        "cheese",
        "sesame bun"
    ],
    "quarter pounder with cheese deluxe": [
        "quarter pound beef patty",
        "lettuce",
        "tomato",
        "onions",
        "pickles",
        "cheese",
        "mayo",
        "sesame bun"
    ]
}

hot_dog_ingredients = {
    "classic": ["hot dog bun", "sausage", "mustard", "ketchup"],
    "chili dog": ["hot dog bun", "sausage", "chili", "onions"],
    "cheese dog": ["hot dog bun", "sausage", "cheese sauce", "mustard"],
    "corn dog": ["cornmeal batter", "sausage", "honey mustard"]
}



cart = []
total = 0


print("MENU:")
for item, price in menu.items():
    print(f" {item.capitalize():12} ${price:.2f}")
print("-"*20)

# tax

def add_tax(amount):
    if len(cart) >= 10:
        tax_rate = 0.10
    else:
        tax_rate = 0.05
    return amount * (tax_rate)


def size_up():
    print("\n1. Small  - $0.00")
    print("2. Medium - $0.50")
    print("3. Large  - $1.00")
    try:
        choice = int(input("enter size (1/2/3): "))
        if choice == 1:
            return "small", 0.00
        elif choice == 2:
            return "medium", 0.50
        elif choice == 3:
            return "large", 1.00 
        else:
            print("please enter 1, 2, or 3!")
            return "", 0.00
        

    except ValueError:        # ← user nhập chữ thay vì số
        print("please enter a number!")
        return "small", 0.00


def size_hamburger():
    print("\n1. Small - $1.00")
    print("2. Medium - $1.25")
    print("3. Large - $2.00")
    try:
        choice = int(input("enter size (1/2/3): "))
        if choice == 1:
            return "small", 1.00
        elif choice == 2:
            return "medium", 1.25
        elif choice == 3:
            return "large", 2.00
        else:
            print("please enter 1, 2, or 3!")
            return "small", 1.00
         
    except ValueError:
        print("please enter a number")
        return "small", 1.00






def add_combos(choice=None):
    if choice is None:
        print("\n we have 3 combos is sales for now is burger combo ")
        choice = input("enter the combo you want: ").lower().strip()

    if choice in menu_combos:
        combo_data = menu_combos[choice]
        for item in combo_data["items"]:
            cart.append(item)
        extra = combo_data['price']
        savings = combo_data["savings"]
        print(f"\n{choice.title()} added to cart!")
        print(f"you save ${savings:.2f} with this combo!")
        print(f"current total: ${total + extra:.2f}")
        return extra
    else:
        print("sorry we don't have that combo")
        return 0.00

def add_hot_dog(choice=None):
    if choice is None:
        print("\n we have classic, chili dog, cheese dog, corndog")
        choice = input("enter the hotdog you want(q to remove): ").lower().strip()

    if choice in hot_dog_ingredients:
        ingreditents = hot_dog_ingredients[choice].copy()
        print(f"\nIngredients for {choice.title()}: {ingreditents}") 
        remove = input("enter ingredient to remove (or press Enter to skip): ").strip()
        if remove in ingreditents:
            ingreditents.remove(remove) 
            print(f"updated ingredients: {ingreditents}")  
        elif remove != "":
            print("ingredient not found!")

        size, size_cost = size_up()
        hot_dog_name = f"{size.title()} {choice.title()} hot dog"
        cart.append(hot_dog_name)
        extra = menu["hot dog"]
        print(f"{hot_dog_name} added to cart. current total: ${total + extra:.2f}")
        return extra
    elif choice == "q":
        print("cancelled.")
        return 0.00
    else:
        print("sorry we don't have that type of hotdog")
        return 0.00
    


def add_hamburger(choice=None):
    if choice is None:
        print("\n we have big mac, quarter pounder with cheese, quarter pounder with cheese deluxe ")
        choice = input("Enter the burger you want (big mac, quarter pounder with cheese, quarter pounder with cheese deluxe) (q to remove): ").lower().strip()
    
    if choice in burger_ingredients:
        ingredients = burger_ingredients[choice].copy()
        print(f"\nIngredients for {choice.title()}: {ingredients}")
        # trước đó nên thê, remove ở kipf choice =="q"
        remove = input("Enter ingredient to remove (or press Enter to skip): ").strip()
        if remove in ingredients:
            ingredients.remove(remove)
            print(f"updated ingredients: {ingredients}")
        elif remove != "":
            print("ingredient not found!")
        
        size, size_cost = size_hamburger()
        hamburger_name = f"{size.title()} {choice.title()} hamburger"
        cart.append(hamburger_name)
        extra = menu["hamburger"]
        print(f"{hamburger_name} added to cart. current total: ${total + extra:.2f}")
        return extra
    elif choice == "q":
        print("cancelled.")
        return 0.00
    else:
        print("sorry we don't have that type of hambyrger.")
        return 0.00

        

    

def add_chips():
    
    print("\nWe have 3 type of chips classic, kettle-cooked, rippled. please choose one")
    choice = input("enter the type of chips you want: ").lower().strip()

    if choice in chips_flavor:
        chips_name = f"{choice} chips"
        size, size_cost = size_up()
        chips_name = f"{size} {chips_name}"
        cart.append(chips_name)
        extra = chips_flavor[choice] + size_cost
        print(f"{chips_name} added to cart current total: ${total:.2f}")
        return extra 
    else:
        print("sorry we don't have thay type of chips, please choose from classic, kettle-cooked, rippled")
        return 0.00




def add_fries(choice=None):
    if choice is None:
        print("\nwe have 3 types of fries: curly, crinkle, and shoestring. please choose one")
        choice = input("enter the type of fries you want: ").lower().strip()
    
    if choice in fries_type:
        fries_name = f"{choice} fries"
        size, size_cost = size_up()  
        fries_name = f"{size} {fries_name}" 
        extra = fries_type[choice] + size_cost
        cart.append(fries_name)
        print(f"{fries_name} added to cart. current total: ${total:.2f}")
        return extra
    else:
        print("sorry we don't have that type of fries, please choose from curly, crinkle, and shoestring")
        return 0.00


def add_soda(choice=None):
    if choice is None:
        print("we have 3 flavors of soda: cola, lemon-lime, and orange. please choose one")
        choice = input("enter the flavor of soda you want: ").lower().strip()
    
    if choice in soda_flavor:
        soda_name = f"{choice} soda"
        size, size_cost = size_up()
        soda_name = f"{size} {soda_name}"
        cart.append(soda_name)
        extra = soda_flavor[choice] + size_cost
        print(f"{soda_name} added to cart, current total: ${total:.2f}")
        return extra
    else:
        print("sorry we don't have that flavor of soda, please choose from cola, lemon-lime, and orange")
        return 0.00



def add_popcorn():
    print("we have 3 types of popcorn: butter, salt, and cheese, please choose one")
    choice = input("enter the flavor of popcorn you want: ").lower().strip()
    
    if choice in popcorn_flavor:
        popcorn_name = f"{choice} popcorn"
        size, size_cost = size_up()
        popcorn_name = f"{size} {popcorn_name}"
        cart.append(popcorn_name)
        extra = popcorn_flavor[choice] + size_cost
        print(f"{popcorn_name} added to cart, current total: ${total:.2f}")
        return extra
    else:
        print("sorry we don't have that flavor of popcorn, please choose from butter, salt and cheese. ")
        return 0.00

print("-- Please enter the items you would like to purchase --\n")
print("COMBOS:")
for combo, data in menu_combos.items():
    print(f"{combo.title():20} ${data['price']:.2f}. (save ${data['savings']:.2f})")





while True:
    food = input("enter the food you want to order (q to quit, f to show menu): ").lower().strip()
    
    if food == "q":
        break
    elif food == "f":
        print("MENU:")
        for item, price in menu.items():
            print(f" {item.capitalize():12} ${price:.2f}")
        print("-"*20)
        print("COMBOS:")
        for combo, data in menu_combos.items():
            print(f"{combo.title():20} ${data['price']:.2f}. (save ${data['savings']:.2f})")
        continue
    elif food == "":          # ← bắt input rỗng
        print("please enter a food item!")
        continue
    elif food in menu:
        try:
            quantity = int(input(f"How many {food} do you want? "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            if food == "soda":
                print("we have 3 flavors of soda: cola, lemon-lime, and orange. please choose one")
                flavor = input("enter the flavor of soda you want: ").lower().strip()
                if flavor not in soda_flavor:
                    print("sorry we don't have that flavor of soda, please choose from cola, lemon-lime, and orange")
                    continue
                for _ in range(quantity):
                    total += menu[food] + add_soda(flavor)
            elif food == "fries":
                print("\nwe have 3 types of fries: curly, crinkle, and shoestring. please choose one")
                fry_type = input("enter the type of fries you want: ").lower().strip()
                if fry_type not in fries_type:
                    print("sorry we don't have that type of fries, please choose from curly, crinkle, and shoestring")
                    continue
                for _ in range(quantity):
                    total += menu[food] + add_fries(fry_type)
            else:
                for _ in range(quantity):
                    total += menu[food]
                    cart.append(food)
                    if food == "popcorn":
                        total += add_popcorn()
                    elif food == "chips":
                        total += add_chips()
                    elif food == "hamburger":
                        total += add_hamburger()
                    elif food == "hot dog":
                        total += add_hot_dog()
            print(f"{quantity} {food.capitalize()} added to cart. Current total: ${total:.2f}")
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
    elif food in burger_ingredients:
        try:
            quantity = int(input(f"How many {food} do you want? "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            for _ in range(quantity):
                total += menu["hamburger"]
                cart.append(food)
                total += add_hamburger(food)
            print(f"{quantity} {food.title()} added to cart. Current total: ${total:.2f}")
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
    elif food in menu_combos:
        total += add_combos(food)


    else:
        print("sorry we don't have that item, please choose from the menu")


# nói chung phần này ổn có thể kiểm tra trong tương lai
print("\n" + "-"*20)
print("your order summary:")
print("-"*20)

if cart:
    for item in cart:
        print(f"- {item.capitalize()}")
        
    print("-"*20)
    print(f"Total: ${total:.2f}")
    tax_total = add_tax(total)
    total += tax_total
    print(f"tax for {len(cart)} items: ${tax_total:.2f}")
    print(f"Total with tax: ${total:.2f}")


else:
    print("you did not order anything.")

print("\nThank you for your order! Enjoy the movie!")
print("-"*20)
#info all the items in the cart and the total price

