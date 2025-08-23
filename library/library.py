library = [{"BookId": 1, "Title": "Learn Python Programming", "Author": "John Doe", "Year": 2020},
           {"BookId": 2, "Title": "Advanced Python", "Author": "Jane Smith", "Year": 2021},
           {"BookId": 3, "Title": "Data Science with Python", "Author": "Emily Davis", "Year": 2019}]

def search_book(query):
    results = []
    for book in library:
        if str(book["BookId"]) == str(query) or book["Title"].lower() == query.lower():
            results.append(book)
    return results  