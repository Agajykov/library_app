from books import Book
from members import Member


class Library: 
	def __init__(self):
		self.books = [] 
		self.members = []

	def add_book(self, book):
		self.books.append(book)
	
	def display_books(self):
		if not self.books:
			print("No books in the library:")
		else:
			for book in self.books:
				print(book)

	def remove_books(self,book):
		if book in self.books:
			self.books.remove(book)			

	def add_member(self, member):
		self.members.append(member)
		
	def display_members(self):
		if not self.members:
			print("No members in the library:")
		else:
			for members in self.members:
				print(members)
	
	def remove_member(self,member):
		if member in self.members:
			self.members.remove(member)

	#Good to have functions

	def get_number_of_books(self):
		return len(self.books)

	def get_number_of_members(self):
		return len(self.members)
	


