class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self) -> str:
		return f"Book: {self.title} by {self.author}"
	
	def get_book_info(self):
		return f"{str(self.title)} {str(self.author)}"
	
	def update_book(self,title,author):
		self._name = title
		self._lastName = author