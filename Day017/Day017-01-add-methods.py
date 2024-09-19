# Adding Methods to the class

class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def greet(self):
        print("Hello, my name is", self.name)

    def follow(self, user): # Method to follow another user (user is an object)
        user.followers += 1 # Increment followers of the user
        self.following += 1 # Increment following of the user

# Example
user1 = User("001", "John")
user2 = User("002", "Jane")

user1.greet()

# Follow user2
user1.follow(user2)
print('User1 followers:', user1.followers)
print('User1 following:', user1.following)
print('User2 followers:', user2.followers)
print('User2 following:', user2.following)
