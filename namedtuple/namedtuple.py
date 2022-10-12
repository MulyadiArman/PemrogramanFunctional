from collections import namedtuple

# ini adalah salah satu contoh penggunaan dari namedtuple 

Person = namedtuple("person", "name age height")
jane = Person("Jane", 25,1.75)
jane.age

print(jane)