import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str, help= "will replace USA with Armenia")

args = parser.parse_args()
all_low = args.text.lower()
new_text = args.text.replace("usa", "Armenia")
new_text = new_text.replace("USA", "Armenia")
quantity = str(all_low.count("usa"))

print("The given string: " + args.text)
print("The USA/usa count is: " + quantity)
print("The new string: " + new_text)