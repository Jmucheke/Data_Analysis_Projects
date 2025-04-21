class Comment:
    def __init__(self, text, commenter):
        self._text = text          # The text content of the comment
        self._commenter = commenter  # The User who made the comment

    def __str__(self):
        return self._commenter.display_name + " commented: '" + self._text + "'"