import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int, required=True)
parser.add_argument('--y', type=int, required=True)
args = parser.parse_args()
product = args.x * args.y
print('Product:', product)