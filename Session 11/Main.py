import json



file = "books.json"

try:
    with open(file,"r") as f:
        books = json.load(f)
        print(books)

except:
    books = []

def save_toJson():
    with open("books.json", "w") as data:
        json.dump(books, data)

def add_book():
    title = input("insert book title : ") 
    author = input("insert book author : ") 
    year = input("insert book year : ") 
    genre = input("insert book genre : ") 
    borrowed = input("is book borrowed : ") 
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "borrowed": borrowed
    }

    books.append(book)
    list_book()
    save_toJson()
    
def list_book():
    for index, book in enumerate(books):
        print()
        print("No: ", index+1)
        print("------------")
        print("title: ", book['title'])
        print("author: ", book['author'])
        print("year: ", book['year'])
        print("genre: ", book['genre'])
        print("borrowed: ", book['borrowed'])
        print("------------")

def edit_book():
    list_book()
    no_book = int(input("Choose no book you want to edit: " ))
    new_book = books[no_book-1]
    print("------------")
    print("title: ", new_book['title'])
    print("author: ", new_book['author'])
    print("year: ", new_book['year'])
    print("genre: ", new_book['genre'])
    print("------------")
    
    update_book = input("Choose which one do you want to update")
    
    if update_book == "1":
        new_book["title"] = input("Input new title")
    elif update_book == "1":
        new_book["author"] = input("Input new author")
    elif update_book == "1":
        new_book["year"] = input("Input new year")
    elif update_book == "1":
        new_book["genre"] = input("Input new genre")
    else:
        print("No option")
    
    save_toJson()
    
    
def delete_book():
    list_book()
    no_book = input("choose book you want to delete")
    books.pop(int(no_book) -1)
    
    save_toJson()
while True:
        print("\n--- Please Choose menu ---")
        print("1. Add Book")
        print("2. List Book")
        print("3. Edit book")
        print("4. Delete book")
        print("5. Exit")
        
        menu = input("Choose Menu: ")
        if menu == "1":
            add_book()
        elif menu == "2":
            list_book()
        elif menu == "3":
            edit_book()
        elif menu == "4":
            delete_book()
        elif menu == "5":
            break
        else:
            print("invalid menu")
        
        save_toJson()
        