import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val", type = int)

set1 = {0,1,2,3,4,5}

args = parser.parse_args()

print(set1)
set1.add(int(args.val))
print(set1)