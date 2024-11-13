from library import Library
from books import Book
from members import Member

def main():
    book1 = Book("How to cook the best Turkmen Pilaw","Avdy Agajykov")
    book2 = Book("How to make the best South Korean Kimchi", "Jeonghu Heo")
    book3 = Book("How to prepare the best Hummus ", "Hassan Mroue")
    
    member1 = Member("John", "Agajykov", 1)
    member2 = Member("Hassan", "Mroue", 2)
    member3 = Member("Jeonghu", "Heo", 3)
	
    # library = Library()
    # #library.add_member(member1)
    # library.add_book(member1)
	
	
	# member1.show_borrowed_book()
    # library.add_member(member2)
    # library.add_member(member3)
    # library.display_members()
    # library.add_book(book1)
    # library.add_book(book2)
    # library.add_book(book3)
    # library.display_books()
	
    # library.get_number_of_books()
    # library.get_number_of_members()
    # library.remove_member(member1)
    # library.display_members()
    # library.remove_books(book1)
    # library.display_books()

    
    # library.add_book(book1)
    # library.display_books()
    member1.borrow_book(book1)
    # member1.show_borrowed_book()
	
	




	
	
	


if __name__ == "__main__":
    main()