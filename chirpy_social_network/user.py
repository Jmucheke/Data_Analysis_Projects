from post import Post  
import random

class User:
    total_users = 0  

    def __init__(self, username, display_name, password):
        self._username = username
        self._display_name = display_name  # Private attribute
        self._password = password          # Private attribute
        self._posts = [ ]                   # Private attribute for user posts
        User.total_users += 1

    # Read-only property for username (since it shouldn't change after creation)
    @property
    def username(self):
        return self._username

    # Getter for display_name
    @property
    def display_name(self):
        return self._display_name

    # Setter for display_name
    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")
        self._display_name = value

    def show_profile(self):
        print("User:", self._display_name, "(@" + self._username + ")")

    def create_post(self, content):
        post = Post(content, self)
        self._posts.append(post)
        return post

    def like_post(self, post):
        post.like_post(self)

    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        guest_username = "guest" + str(random_number)
        guest_display_name = "Guest"
        return cls(guest_username, guest_display_name, "guestpass")

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password
    
    # Provide a user-friendly string representation
    def __str__(self):
        return "<User: %s (%s)>" % (self._display_name, self._username)