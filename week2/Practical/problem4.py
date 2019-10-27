import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--age", help="Get an age from user", type=int)

args = parser.parse_args()

if args.age:
    print("Happy Birthday, you are already " + str(args.age) + " years old!")
else:
    print("No optional argument was given!")