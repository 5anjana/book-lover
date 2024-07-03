import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        book = 'Pride and Prejudice'
        rating = 5
        booklover1.add_book(book, rating)
        self.assertTrue(book in booklover1.book_list.book_name.values.tolist(), 'Book is not added.')

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        book = 'Pride and Prejudice'
        rating = 5
        booklover1.add_book(book, rating)
        booklover1.add_book(book, rating)
        self.assertEqual(1, booklover1.book_list.book_name.value_counts().get(book, 0), 'Same book is added multiple times.')
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        book = 'Pride and Prejudice'
        rating = 5
        booklover1.add_book(book, rating)
        self.assertTrue(booklover1.has_read(book), 'Read book is not is read list.')
        
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        booklover1.add_book('Pride and Prejudice', 5)
        book = 'Lord of the Flies'
        self.assertFalse(booklover1.has_read(book), 'Unread book is in read list.')
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        booklover1.add_book('Pride and Prejudice', 5)
        booklover1.add_book('Norwegian Wood', 1)
        booklover1.add_book('Jane Eyre', 3)
        booklover1.add_book('Slaughterhouse-Five', 4)
        self.assertEqual(booklover1.num_books_read(), len(booklover1.book_list), 'Number of books read is wrong.')
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover1 = BookLover('Sanjana', 'eqp6pg@virginia.edu', 'Fiction')
        booklover1.add_book('Pride and Prejudice', 5)
        booklover1.add_book('Norwegian Wood', 1)
        booklover1.add_book('Jane Eyre', 3)
        booklover1.add_book('Slaughterhouse-Five', 4)
        fav_books = booklover1.fav_books()
        self.assertTrue((fav_books.book_rating > 3).all(), 'Not all favourite books have a rating more than 3.')
        
if __name__ == '__main__':
    unittest.main(verbosity=3)


