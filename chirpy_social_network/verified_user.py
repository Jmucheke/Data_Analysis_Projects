from user import User
from post import Post

class VerifiedUser(User):
    def __init__(self, username, display_name, password):
        # Initialize using User's constructor
        super().__init__(username, display_name, password)
        # Privately mark the user as verified
        self._verification_badge = True
        # Update the private display name attribute to include a verified badge
        self._display_name = "✅ " + display_name

    def get_verification_status(self):
        return "Verified ✅" if self._verification_badge else "Regular"

    # Override create_post() to include verified flair in post content
    def create_post(self, content):
        verified_content = "✅ " + content
        post = Post(verified_content, self)
        self.posts.append(post)
        return post