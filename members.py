
from books import Book
class Member:
	_id = None
	_name = None
	_lastName = None
	_borrowed_books = []

	def __init__(self, name, lastName, id):
		self._name = name
		self._lastName = lastName
		self._id = id
		
	def borrow_book(self, book):
		self._borrowed_books.append(book)

	def show_borrowed_book(self):
		if not self._borrowed_books:
			print(f"{self._name} have not borrowed any books")
		else:
			for borrowed_book in self._borrowed_books:
				print(f"{self._name} borrowed the {borrowed_book}")

	def __str__(self) -> str:
		return f"Member: {self._name} {self._lastName}, ID: {self._id}"