import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", type= str, help="Thsi will print 'Welcome, Name!")

args = parser.parse_args()

print("Welcome, " + args.name + "!")