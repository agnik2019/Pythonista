import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--values', type=int, nargs='+')
args = parser.parse_args()
sum = sum(args.values)
print('Sum:', sum)