class Publication:
    def __init__(self, name: str):
        self.name = name

    def print_information(self):
        print(self)

class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def __str__(self) -> str:
        return f"{self.name} (author {self.author}, {self.page_count} pages)"

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def __str__(self) -> str:
        return f"{self.name} (chief editor {self.chief_editor})"

print(Book("Compartment No. 6", "Rosa Liksom", 192))
print(Magazine("Donald Duck", "Aki Hyyppä"))
