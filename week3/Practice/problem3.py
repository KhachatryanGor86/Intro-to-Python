import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val")

list2 = ['a', 'b', 'c', 'a', 'c']

args = parser.parse_args()
q = list2.count(args.val)

print(list2)
print("Number of " + args.val + "-s = " + str(q))