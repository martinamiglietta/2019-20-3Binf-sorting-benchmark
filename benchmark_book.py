from book import Book
from selection_sort_book import selection_sort

book1 = Book("Canzoniere", "petrarca", )
book2 = Book("Divina Commedia", "Dante")
book3 = Book("Decameron", "Boccaccio")
book_list = [book1,book2,book3]

selection_sort(book_list)