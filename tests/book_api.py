import copy 

books = {
    "1": {
        "Name": "AI/ML",
        "Author": "Sanjay"
    }, 
    "2": {
        "Name": "MLOps",
        "Author": "Uddith"
    }
}

def get_books(*args):
    return {
        "books": books
    }

def post_book(value, *args):
    new_id = str(len(books) + 1)
    new_book = {
        "Name": value.get("Name"),
        "Author": value.get("Author")
    }
    books[new_id] = (new_book)
    print(new_book)
    return {
        "message": "New book added",
        "book": new_book
    }

def update_book(value, url_params):
    id = url_params.get("id")
    previous_books = copy.deepcopy(books)
    previous_book = previous_books[id]  
    books[id]["Name"] = value.get("Name")
    books[id]["Author"] = value.get("Author")
    new_book = books[id] 

    return {
        "message": "Updated a record",
        "previous_book": previous_book,
        "new_book": new_book
    }

def delete_book(url_params):
    id = url_params.get("id") 
    if id in books.keys():
        deleted_book = books.pop(id) 
        return {
            "message": "Deleted a record",
            "deleted_book": deleted_book
        } 
    else:
        return {
            "message": "No record found!"
        }