mylist = [1, 2, 3]
print(__name__)
a = 100
import __main__
print(__main__.a)
__main__.a = 200
print(a)
print(__file__)