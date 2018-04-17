#16.2 Word Frequency

from collections import defaultdict

def wordFreq(book , w):

      book_len = len(book)

      count = 0


      for word in book:
            if w == word:
                  count += 1

      if count > 1:

            print('Count of {} in book is {} '.format(w , count))
      else:
            print('Word not found')
                  


def wordFreqHash(book , w):

      book_len = len(book)

      book_dict = defaultdict(int)

      for word in book:

            book_dict[word] += 1

      print(book_dict)


book = ["the" , "word" , "a" , "these" , "the" , "words"] * 5
wordFreq(book , 'rat')
wordFreqHash(book , 'the')
