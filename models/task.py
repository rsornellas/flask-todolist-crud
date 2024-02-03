class Task:
    def __init__(self, id, title, description, done=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return f"{self.title} - {self.description}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
        }