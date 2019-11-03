import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", type = str)
parser.add_argument("value", type = str)

args = parser.parse_args()

dict1 = {'k1':'Gor', 'k2':'Hayk', 'k3':'Armen'}
print(dict1)
dict1[args.key] = args.value
print(dict1)