class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self) -> str:
		return f"Book: {self.title} by {self.author}"