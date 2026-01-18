class Book:
    title = ""
    author = ""

class Stack:
    _stack = []
    def push(self,item):
        self._stack.append(item)
    def pop(self):
        return self._stack.pop()

class Queue:
    _queue = []
    def enqueue(self,item):
        self._queue.append(item)
    def dequeue(self):
        return self._queue.pop(0)
    def isEmpty(self):
        return(len(self._queue) == 0)


long_book = Book()
long_book.title = "War and Peace"
long_book.author = "Tolstoy"

medium_book = Book()
medium_book.title = "Book of Armaments"
medium_book.author = "Maynard"

short_book = Book()
short_book.title = "Vegetables that I like"
short_book.author = "John Keyes"


book_stack = []
book_stack.append(medium_book)
book_stack.append(short_book)
book_stack.append(long_book)

book_queue = []
book_queue.append(medium_book)
book_queue.append(short_book)
book_queue.append(long_book)

next_book = book_queue.pop(0)
