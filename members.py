
from books import Book
class Member:
	def __init__(self, name, lastName):
		self._name = name
		self._lastName = lastName
		self._borrowed_books = []
		
	def get_user_info(self):
		return f"{str(self._name)} {str(self._lastName)}"
	
	def borrow_book(self, book):
		self._borrowed_books.append(book)

	def show_borrowed_book(self):
		if not self._borrowed_books:
			print(f"{self._name} have not borrowed any books")
		else:
			for borrowed_book in self._borrowed_books:
				print(f"{self._name} borrowed the {borrowed_book}")

	def update_user_name_and_lastName(self,name,last_name):
		self._name = name
		self._lastName = last_name

	def get_name(self):
		return self._name
	def get_last_name(self):
		return self._lastName
	

	def get_borrowed_books(self):
		return self._borrowed_books	

	#Overiding in case object will be called directly
	def __str__(self) -> str:
		return f"Member: {self._name} {self._lastName}"

	 	