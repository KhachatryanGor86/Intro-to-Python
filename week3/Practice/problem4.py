import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val")

list4 = ['a', 'b', 'c', 'a', 'c']

args = parser.parse_args()
print(list4)

list4.remove(args.val)
print(list4)