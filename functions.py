# functions defined to use in main.py

def personalityType():
    print("\n")
    print("Personality")
    print("1: Direct - strong willed, firm and result oriented")
    print("2: Influencer - Outgoing, enthusiastic and optimistic")
    print("3: Steady - Even-tempered, patient and tactful")
    print("4: Check-lister - Reserved, analytical and precise")

    choice = int(input("Choose a Personality Type 1-4: "))
    if choice == 1:
        choice = "You chose Direct"
    elif choice == 2:
        choice = "You chose Influencer"
    elif choice == 3:
        choice = "You chose Steady"
    elif choice == 4:
        choice = "You chose Check-lister"
    else:
        print("Invalid Input")
    return choice

def TypeOfOccasion():
    print("\n")
    print("Type of Occasions")
    print("1: Birthday")
    print("2: Holiday")
    print("3: Special Occasion")
    inp= int (input ("Enter a number:"))
    if inp == 1:
        inp = "You chose Birthday"
    elif inp == 2:
        inp = "You chose Holiday"
    elif inp == 3:
        inp = "You chose Special Occasion"
    else:
        print ("Invalid input")
    return inp


def hobbyChoice(h):
    if h == 1:
        h = "You chose : Sports/Exercise, Traveling and Volunteering"
    elif h == 2:
        h = "You chose : Traveling, Video-games and Going Out(Nightlife)"
    elif h == 3:
        h = "You chose : Reading, Art and Music"
    elif h == 4:
        h = "You chose : Cooking, Music and Writing"
    else:
        print("Invalid Input")
    return h


def recommendation(x,y):
    import random
    if x == "Male" and y == 1:
        male1=['Golf Set','Tickets to favorite team game','Travel Voucher', 'New Luggage Set,' ,
      'Hiking Boots','Arcteryx Rain Coat']
        recommendation = random.choice(male1)

    elif x == "Male" and y == 2:
        male2=['Xbox','PS5','Uber/Lyft Gift-card']
        recommendation = random.choice(male2)

    elif x == "Male" and y == 3:
        male3=['48 Laws of Power book', 'Movie poster', 'AMC movie tickets', 'Concert tickets',
      'Day Planner','New Apple Airpods']
        recommendation = random.choice(male3)

    elif x == "Male" and y == 4:
        male4=['Favorite Restaurant Gift-card', 'Cookbook', 'Journal','Stephen King memoir', 'Monthly Book Subscription']
        recommendation = random.choice(male4)

    elif x == "Female" and y == 1:
        female1=['Apparel from Favorite Sports Team', 'Tickets to Sport Event', 'Travel Voucher',
        'New Luggage Set', 'Travel Accessories']
        recommendation = random.choice(female1)

    elif x == "Female" and y == 2:
        female2=['Gaming Computer', 'Gaming Chair','Gaming Console', 'Uber/Lyft Gift-card',
        'Restaurant Gift-card', 'Cocktail Voucher']
        recommendation = random.choice(female2)

    elif x == "Female" and y == 3:
        female3=['Reading Glasses', 'Cute Coffee Mug', 'Reading Lamp', 'Monthly Book Subscription',
        'Reading Journal', 'Drawing Board', 'Masterclass.com Membership','Paintbrushes']
        recommendation = random.choice(female3)

    elif x == "Female" and y == 4:
        female4=[ 'Music subscription', 'Record Player','Headphones', 'Concert Tickets', 'Air Fryer',
         'Knife Set', 'Recipe Book', 'Writers Clock', 'Tote Bag', 'Pen and Pencil Set']
        recommendation = random.choice(female4)

    else:
        print("No Recommendation")

    return recommendation
