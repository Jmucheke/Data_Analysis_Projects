from comment import Comment  

class Post:
    total_posts = 0

    def __init__(self, content, author):
        self._content = content   # Private attribute for content
        self._author = author     # Private attribute for author
        self._likes = []          # Private attribute for users who liked the post
        self._like_count = 0      # Private attribute for counting likes
        self._comments = [ ]       # Private attribute for storing comments
        Post.total_posts += 1

    # Getter for content
    @property
    def content(self):
        return self._content

    # Setter for content with validation
    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")
        self._content = new_content

    # Read-only property for author
    @property
    def author(self):
        return self._author

    def like_post(self, user):
        if user not in self._likes:
            self._likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    def get_like_count(self):
        return self._like_count

    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)
        self._comments.append(comment)
        print(comment._commenter.display_name, "added a comment on", self._author.display_name + "'s post.")
        return comment

    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280

    def __repr__(self):
        # Show a snippet if content is over 30 characters
        snippet = self._content if len(self._content) <= 30 else self._content[:27] + "..."
        return "<Post by " + self._author.username + ": '" + snippet + "', Likes: " + str(self._like_count) + ">"