from user import User
from verified_user import VerifiedUser

class SocialNetwork:
    def __init__(self):
        self._users = [ ]  # Private list to store User objects
        self._posts = [ ]  # Private list to store Post objects

    def add_user(self, user, verified):
        account_type = verified

        # Extract user information
        username = user.username
        display_name = user.display_name
        password = user._password

        # Check if user already exists
        if self.search_user_by_username(username):
            print("\nUser with username '{}' already exists!\n".format(username))
            return

        # Create the appropriate user object
        if account_type == "True":
            new_user = VerifiedUser(username, display_name, password)
        else:
            new_user = User(username, display_name, password)

        # Add the new user to the network
        self._users.append(new_user)
        print(display_name, "has been added to Chirpy.")

    def add_post(self, post):
        self._posts.append(post)
        print("A new post has been added to Chirpy.")

    def search_user_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None

    def search_user_for_post(self, username, password):
        user = self.search_user_by_username(username)
        if user:
            if user.check_password(password):
                return user
            else:
                print("Enter correct password.")
        else:
            print("User not found.")
        return None

    def remove_user(self, username):
        user_to_remove = self.search_user_by_username(username)
        if user_to_remove:
            self._users.remove(user_to_remove)
            print("\n", user_to_remove.display_name, "has been removed from the Chirpy.")
        else:
            print("\nUser with username", username, "not found!")

    def list_all_posts(self):
        if not self._posts:
            print("\nNo posts to display.")
        else:
            for index, post in enumerate(self._posts):  # Add index using enumerate
                print(index, ". ", post.author.display_name, " posted: '", post.content, "'", sep="")

                # Show likes if any
                if post._likes:
                    liked_by = ", ".join(user.display_name for user in post._likes)
                    print("   Liked by:", liked_by)

                # Show comments if any
                if post._comments:
                    for comment in post._comments:
                        print("     - ", comment._commenter.display_name, ": '", comment._text, "'", sep="")