'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
  "  *  ",
  " *** ",
  "*****"
'''
n_floors = 15

def tower_builder(n_floors):
    count = 1
    star = 1
    print("[")
    while count <= n_floors:
        pyramid = "'" + "*" * star + "'"
        count += 1
        star += 2
        print(pyramid.center(n_floors *3," "))
    print("]")

tower_builder(n_floors)