books = [
    (1, "1984", "George Orwell", 1949),
    (2, "Animal Farm", "George Orwell", 1945),
    (3, "The Great Gatsby", "F. Scott Fitzgerald", 1925),
    (4, "Pride and Prejudice", "Jane Austen", 1813),
    (5, "Lord of the Flies", "William Golding", 1954)
]

def find_by_id(book_id):
    for book in books:
        if book[0] == book_id:
            return book

def find_by_title(title):
    for book in books:
        if book[1].lower() == title.lower():
            return book

def books_before(year):
    return [book for book in books if book[3] < year]

def author_count():
    count = {}
    for book in books:
        author = book[2]
        count[author] = count.get(author, 0) + 1
    return count