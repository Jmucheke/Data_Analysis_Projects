from social_network import SocialNetwork
from user import User
from verified_user import VerifiedUser

# Initialize the Chirpy Social Network
chirpy_network = SocialNetwork()

verified_user = VerifiedUser("jes", "jes", "123")

# Add both users to the network
chirpy_network.add_user(verified_user, 'yes')

def display_menu():
    print("\n Chirpy Social Media Platform")
    print("========================================")
    print("1. Create New Account")
    print("2. Post a Chirp")
    print("3. View All Chirps")
    print("4. Like a Chirp")
    print("5. Comment on a Chirp")
    print("6. View Profile")
    print("7. List All Users")
    print("8. Exit")


def create_account():
    username = input("Enter username: ")
    display_name = input("Enter display name: ")
    password = input("Enter password: ")
    verified = input("Do you want a verified account? (yes/no): ").strip().lower()
    if verified == "yes":
        user = VerifiedUser(username, display_name, password)
    else:
        user = User(username, display_name, password)
    chirpy_network.add_user(user, verified)
    
def create_post():
    username = input("Enter username: ")
    user = chirpy_network.search_user_by_username(username)
    if user:
        chirp = input("Enter your chirp: ")
        post = user.create_post(chirp)
        chirpy_network.add_post(post)
    else:
        print("User not found.")
        
def display_posts():
    chirpy_network.list_all_posts()

def like_post():
    username = input("Enter username: ")
    user = chirpy_network.search_user_by_username(username)
    if user:
        chirpy_network.list_all_posts()
        try:
            index = int(input("Select the post index to like (starting from 0):" + "\n"))
            if 0 <= index < len(chirpy_network._posts):
                user.like_post(chirpy_network._posts[index])
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")
    
def add_comment():
    username = input("Enter username: ")
    user = chirpy_network.search_user_by_username(username)
    if user:
        chirpy_network.list_all_posts()
        try:
            index = int(input("Select the post index to comment (starting from 0):" + "\n"))
            if 0 <= index < len(chirpy_network._posts):
                comment = input("Enter your comment: ")
                chirpy_network._posts[index].add_comment(comment, user)
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")
        
def view_profile():
    username = input("Enter username: ")
    user = chirpy_network.search_user_by_username(username)
    if user:
        user.show_profile()
    else:
        print("User not found.")
        
def list_all_users():
    if chirpy_network._users:
        print("-- Registered Users --")
        for user in chirpy_network._users:
            print(user)
    else:
        print("No users registered yet.")

while True:
    display_menu()
    choice = input("Choose an option (1-8): ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        # Your code here: post a chirp
        create_post()
    elif choice == "3":
        # Your code here: view all chirps
        display_posts()
    elif choice == "4":
        # Your code here: like a chirp
        like_post()
    elif choice == "5":
        # Your code here: comment on a chirp
        add_comment()
    elif choice == "6":
        # Your code here: view profile
        view_profile()
    elif choice == "7":
        # Your code here: list all users
        list_all_users()
    elif choice == "8":
        print("Exiting Chirpy. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        
# if __name__ == "__main__":
    