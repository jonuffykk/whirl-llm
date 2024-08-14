class Document:
    def __init__(self, id, title, content, author=None, created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at

    def __str__(self):
        return f"Document(id={self.id}, title='{self.title}', author='{self.author}')"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            content=data.get('content'),
            author=data.get('author'),
            created_at=data.get('created_at')
        )