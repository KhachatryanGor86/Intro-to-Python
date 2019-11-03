import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val", type = int)

set2 = {0,1,2,3,4,5,6,7,8,9}

args = parser.parse_args()

print(set2)
if args.val in set2:
    set2.remove(args.val)
print(set2)