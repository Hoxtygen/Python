#List is a collection of objects, it's mutable. That is, an element in a particular position can be changed

authors = ['Jeffery Deaver', 'Robin Cook', 'Mark Epstein', 'Brian Tracy', 'Nicolas Cage']
print(authors[4])

list_list = [4, 89, 'hello', [4, 8, 'me'], [56, 'michael', [44, 68]]]
print(list_list[4][2])
list_list[2]  = 'Michael Gove'
print(list_list)