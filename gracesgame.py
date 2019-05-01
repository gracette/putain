print("Welcome, adventurer! What is your name?")
name = input()
print("It's good to meet you, " + name + ".")
print("You are currently in a small cottage. On a small kitchen table, there is a leather-bound journal lying face open.")
print("Next to the table is a dresser with three drawers.")

# Next we will use an array to store whatever the adventurer acquires.
# An array is like a box of stuff which can contain variables, numbers, text strings, etc...
# Many people in the Python community refer to arrays as "lists".
inventory = [] # Creates an array called "inventory" which is empty

# Add something to the array like this:
# inventory.append(something)
# And remove something like this:
# inventory.remove(something)
def show_first_option_menu():
    print("What would you like to do?")
    print("1. Read the journal")
    print("2. Examine the dresser")
    print("3. Look around")

    choice0 = int(input())

    if choice0 == 1:
        print("The journal is in a language you cannot read. However, there is a drawing of a dragon next to the first entry.")
        # TODO: finish writing option 1
    elif choice0 == 2:
        print("The two lower drawers are accessible, but the top drawer is locked and requires a key.")
        print("The lowest drawer contains a single shirt and a pair of pants.")
    elif choice0 == 3:
        print("foo")
        # do some fun stuff
    else:
        # probably print somekind of error message
        show_first_option_menu()

show_first_option_menu()
