from library import Library
from books import Book
from members import Member

def main():
    print("\n=========================================== Library App ===========================================\n")
    print("Student: Avdyrahman Agajykov\nProgram: Dual Study (Software Engineering)\nClass: Programming\n")
    book1 = Book("How to cook the best Turkmen Pilaw","Avdy Agajykov")
    book2 = Book("How to make the best South Korean Kimchi", "Jeonghu Heo")
    book3 = Book("How to prepare the best Hummus ", "Hassan Mroue")
    
    member1 = Member("John", "Agajykov")
    member2 = Member("Hassan", "Mroue")
    member3 = Member("Jeonghu", "Heo")
	
    library = Library()
    library.add_member(member1)
    library.add_member(member2)
    library.add_member(member3)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
   
    print("\n=========================================== Status  ===========================================\n")
    print(f"Number of Active Members: {library.get_number_of_members()}")
    print(f"Number of Active Books: {library.get_number_of_books()}")
    
    print("\n=========================================== Display Books ===========================================\n")
    library.display_books()
    print("\n=========================================== Display Members ===========================================\n")
    library.display_members()
    
  	#Tracking Operations:
    member1.borrow_book(book1)
    member2.borrow_book(book2)
    member3.borrow_book(book3)
	
    print("\n=========================================== Borrowed Books ===========================================\n")
    member1.show_borrowed_book()
    member2.show_borrowed_book()
    member3.show_borrowed_book()
    

   #Remove operations:
    print("\n=========================================== Remove Member  ===========================================\n")
    library.remove_member(member1)
    library.display_members()
    print(f"\nRemoved Member: {member1.get_user_info()} ")
    library.get_number_of_members()
    

    print("\n=========================================== Remove Books ===========================================\n")
    library.remove_books(book1)
    library.display_books()
    print(f"\nRemoved Book: {book1.get_book_info()} ")
    library.get_number_of_books()
    
    print("\n=========================================== Update User Info ===========================================\n")
    member2.update_user_name_and_lastName("Davi", "Becker")
    library.display_members()

    print("\n=========================================== Library App ===========================================")
    
#In case file will be called from outside
if __name__ == "__main__":
    main()