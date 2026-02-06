print("hello chitti babu")
print("em chestunav")
def function_name():
    print("hello ")
function_name()

def sanjay():
    ''' this is the function related to me '''
    print("hello, world !!")

sanjay()

def sum(a,b):
    c=a+b
    return c
d=sum(1,2)
print(d)
#postional arguments

def friend (friend, sathish):
    """Display information about a pet."""
    print(f"I have a {friend} named {sathish}.")

friend("sathish", "Rex")  # animal_type="dog", pet_name="Rex"

def details(name,course="python"):
    ''' this is for course verification'''
    print(f" im {name } im  interested in {course}")

details("sanjay","python")

details ("shivasai")

def item_details(price,name="bonda"):
    ''' price of the tiffin as per the market standards '''
    print(f" the cost of the {name} is {price} in the market")

item_details("40$")
item_details(10)
item_details(199)
item_details(200)
item_details(50,"idly")
#args arbitary positional arguments 
def make_pizza(*toppings):
    """Print the list of toppings requested."""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

def friends_list(*friends):
    ''' this includes my friends list '''
    print(" the following are memebers of my friends list ")
    for i in friends:
        print(f"- {i}" )
friends_list("sanjay","shivasai","shakthi","priscilla")

def fav_food(*menu):
    ''' my fav food items '''
    print(" the following are the my fav food items")
    for items in menu:
        print(items)

fav_food("bonda","biriyani","bhagara","pulihora","etc")


def build_profile(first, last, **user_info):
    """Building a dictionary containing user information."""
    profile = {
        'first_name': first,
        'last_name': last
    }
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user = build_profile('Albert', 'Einstein',
                     location='Princeton',
                     field='Physics',
                     born=1879)
print(user)



def get_dimensions():
    """Return width and height."""
    width = 500
    height = 300
    return width, height

dimensions = get_dimensions()  # dimensions is a tuple (500, 300)
width, height = get_dimensions()  # Unpacking the tuple

def get_dimensions():
    """Return width and height."""
    width = 500
    height = 300
    return width, height

dimensions = get_dimensions()  # dimensions is a tuple (500, 300)
width, height = get_dimensions()  # Unpacking the tuple
print(dimensions)
print(width,height)

def best_friends():
    a="salman khan"
    b="sharukh khan"
    c="amitabh bachhan"
    return a, b, c
list=best_friends()
print(list)
a,b,c=best_friends()
print(a,b,c)

# when multiple return values are present in the function then the return values are packed in a tuple 

#another example on multiple return valeus we are going to see

def heroines():
    top="samantha"
    second="kaja aggarwal"
    third="shraddhakapoor"
    fourth=" sreeleela"
    fifth="sreeleela"
    third="thammanah"
    sixth=" nayanthara"
    return top, second, third, fourth, fifth, sixth

tfi_heroines=heroines()
print(tfi_heroines)
top, second, third, fourth, fifth, sixth=heroines()
print(top, second, third, fourth, fifth, sixth)

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b
c=divide(2,2)
print(c)