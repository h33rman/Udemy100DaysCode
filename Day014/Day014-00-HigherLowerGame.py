# Higher/ Lower game
import random
import os

# List of Dictionary

game_data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 179,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
]
# Format the data
def format_data(account):
    """
    Format the account data into printable format
    """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"

# Generate 2 random data
def generate_data():
    """
    Generate a random account from the game data
    """
    return random.choice(game_data)

# Check if the user is correct
def check_answer(guess, a_followers, b_followers):
    """
    Check if the user is correct
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
is_game_over = False
account_b = generate_data()

while not is_game_over:
    account_a  = account_b
    account_b = generate_data()

    while account_b == account_a:
        account_b = generate_data()


    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct
    # Get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]



    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess 
    if is_correct:
        os.system('clear')
        print(f"You're right! Current score: {score}")
        score += 1
    elif score == 2**5: # Max score = 32 or 2**5
        os.system('clear')
        print(f"Congratulations! You've won the game. Final score: {score}")
        is_game_over = True
    else:
        os.system('clear')
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
        
