import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--age', type=int)
args = parser.parse_args()
if args.age:
  print(args.name, 'is', args.age, 'years old.')
else:
  print('Hello,', args.name + '!')