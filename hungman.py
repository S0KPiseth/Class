import random
category = random.choice(["Food", "Vegetables", "Fruit"])
fruits = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew",
    "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry",
    "Strawberry", "Tangerine", "Ugli Fruit", "Valencia Orange", "Watermelon", "Xigua",
    "Yellow Passion Fruit", "Zucchini", "Apricot", "Blueberry", "Cantaloupe", "Dragon Fruit",
    "Guava", "Jackfruit"
]

vegetables = [
    "Artichoke", "Asparagus", "Broccoli", "Cabbage", "Carrot", "Cauliflower", "Celery", "Corn",
    "Cucumber", "Eggplant", "Fennel", "Garlic", "Green Bean", "Kale", "Leek", "Lettuce",
    "Mushroom", "Onion", "Pea", "Pepper", "Potato", "Pumpkin", "Radish", "Spinach",
    "Squash", "Sweet Potato", "Tomato", "Turnip", "Zucchini", "Beet"
]

foods = [
    "Pizza", "Burger", "Pasta", "Sushi", "Salad", "Sandwich", "Steak", "Tacos",
    "Burrito", "Noodles", "Fried Rice", "Soup", "Omelette", "Pancakes", "Waffles", "Curry",
    "Kebab", "Dumplings", "Paella", "Lasagna", "Quiche", "Risotto", "Stew", "Chili",
    "Falafel", "Bagel", "Ravioli", "Gnocchi", "Bruschetta", "Gazpacho"
]


def game(list):
    print("Type (exit) to quite the game, (hint) to reveal a first letter\nand (guess) to guess the whole word.")
    mistakes = 0
    hint = 0

    print(f"The word is in the {category} category: ")
    word = str(random.choice(list))
    display = [" _ " for i in range(len(word))]
    
    
    print("".join(display))
    print(word)
    while mistakes <3:
        user = input("Enter the letter to guess: ")
        if user =="exit":
            print("You Quite the game!")
            break
        elif user == "hint" and hint<1:
            display[0]= word[0]
            hint = 1
        elif user == "guess":
            if input("Enter the word: ").lower() == word.lower():
                print("You win!")
                break
            else:
                print("You lose!")
                break

        for i,char in enumerate(word):
            if user.lower() == char.lower():
                display[i]=" "+char+" "
            
        if user.lower() not in word.lower():
            mistakes+=1
        print("".join(display))
        if " _ " not in display:
            print("You win!")
            break
    if mistakes == 3:
        print("You lose!")

if category == "Food":
    game(foods)
    
elif category == "Vegetables":
    game(vegetables)
else:
    game(fruits)
