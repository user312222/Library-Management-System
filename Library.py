class Library:
    
    
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def Search (self, title, author):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for word in books:
            attributes = word.split(",")
            if attributes[0] == title and attributes[1] == author:
                return True
        return False


        

    def List_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for word in books:
            attributes = word.split(",")
            print("Title: " + attributes[0] + " Author: " + attributes[1] + " Release Date: " + attributes[2] + " NumberOfPage: " + attributes[3])
    
    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter book autor: ")

        if Library.Search(self, book_title,author):
            print("Ups, book already exist...")
            

        else : 
            release_date = input("Enter release date: ")
            num_pages = input("Enter number og pages: ")
            self.file.write(book_title + "," + author + "," + release_date + "," + num_pages +",\n")
            self.file.flush()

       

    

    



    def remove_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter book autor: ")
        self.file.seek(0)
        books = []
        obj = None
        found = False
        for word in self.file:
            attributes = word.split(",")
                
            if attributes[0] == title and attributes[1] == author: 
                obj = word
                found = True
                break
            else:
                books.append(word)
            
        if found: 
            print("Deleted " + obj)

        else :
            print("Ups there is no book in this name")
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(books)
    
   

def main():
    lib = Library()
   
    while True:
        print("***MENU*** \n" +
             "1) List Books \n" + 
             "2) Add book\n"
             "3) Remove Book \n" +
             "0) Exit\n")
        try: 
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number: ")
            continue

        if choice == 1:
            lib.List_books()

        elif choice == 2:
            lib.add_book()

        elif choice == 3:
            lib.remove_book()
        
        elif choice == 0:
            exit("Exiting... \nHave a nice day")
        else :
            print("Please choose between 0-3")


    
if __name__ == "__main__":
    main()    


    
                

    
