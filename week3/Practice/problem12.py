import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val", type = int)

set3 = {0,1,2,3,4,5,6,7,8,9}
min = min(set3)
max = max(set3)
args = parser.parse_args()

if args.val >= min and args.val <= max:
    print(True)
else:
    print(False)