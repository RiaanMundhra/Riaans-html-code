class Book():
    def __init__(self, name, writer, pages):
        self.name = name
        self.writer = writer
        self.pages = pages
    def __len__(self):
        return int(self.pages)
    
boooook = Book("HarrybahiPottter", "Just Kidding Bowling", "100000")
print(len(boooook))