import random
import string

# Function for generating usernames
def generate_random_username(adjectives, nouns):
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    c = ""
    a = str(input("\nDo you want to add Numbers/Special Symbols:(Y/N)-"))
    if a == 'Y' or a == 'y':
        print("\n1.Numbers\n2.Special Symbols\n3.Both Numbers and Special Symbols")
        b = int(input("Enter your choice:"))
        if b == 1:
            try:
                c = int(input("Enter the number:"))
            except ValueError:
                print("Wrong Input\n")
                return ""  # Return if input is invalid
        elif b == 2:
            specialsymbols = set('@#$%!&?/=+*^')
            c = (input("Enter the Special Symbols:"))
            if all(char in specialsymbols for char in c):
                pass
            else:
                print("Wrong Input\n")
                return ""  # Return if input is invalid
        elif b == 3:
            c = str(input("Enter what you want to add:"))
        else:
            print("Invalid Choice!\nNo username generated.")
            return ""  # Return if input is invalid
    else:
        i = random.randint(10, 999)
        j = ['@', '#', '$', '%', '!', '&', '?', '/', '=', '+', '*', '^', '~']
        c = str(i) + random.choice(j) + random.choice(j)

    username = '{}{}{}'.format(word1, word2, c)
    return username

# Function to save the generated usernames (append to the text file)
def save_username_to_file(username, filename='D:/Libraries/ritwik/Documents/Mokshit/Python Internship Projects/Project-1/Usernames.txt'):
    with open(filename, 'a') as infile:
        infile.write(username + "\n")

# Function to display the generated usernames along with their lengths
def display_usernames(filename='D:/Libraries/ritwik/Documents/Mokshit/Python Internship Projects/Project-1/Usernames.txt'):
    try:
        with open(filename, 'r') as infile:
            read = infile.read().strip(' \n').split('\n')
            print("Generated Usernames:")
            for username in read:
                length = len(username)  # Calculate the length of the username
                print(f"Username: {username}, Length: {length}")
    except FileNotFoundError:
        print("No usernames found.")

def main():
    try:
        num = int(input("How many random words you want to generate:"))
    except ValueError:
                print("Invalid Input\n")
                exit()
    # Read word lists
    with open('D:/Libraries/ritwik/Documents/Mokshit/Python Internship Projects/Project-1/Nouns.txt', 'r') as infile:
        nouns = infile.read().strip(' \n').split('\n')
    with open('D:/Libraries/ritwik/Documents/Mokshit/Python Internship Projects/Project-1/Adjectives.txt', 'r') as infile:
        adjectives = infile.read().strip(' \n').split('\n')

    # Loop for generating n number of usernames
    for i in range(num):
        username = generate_random_username(adjectives, nouns)
        save_username_to_file(username)

    # Display all generated usernames
    display_usernames()

if __name__ == "__main__":
    main()