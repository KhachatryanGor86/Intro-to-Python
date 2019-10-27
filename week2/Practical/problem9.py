import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
parser.add_argument("start_index", type=int)
parser.add_argument("end_index", type=int)

args = parser.parse_args()
print("The given text: " + args.text)
print("Start index: " + str(args.start_index))
print("End index: " + str(args.end_index))
print("Output index: " + args.text[int(args.start_index): int(args.end_index)])
