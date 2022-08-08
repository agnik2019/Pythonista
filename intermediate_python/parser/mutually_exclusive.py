import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--add', action='store_true')
group.add_argument('--subtract', action='store_true')
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()
if args.add:
  sum = args.x + args.y
  print('Sum:', sum)
elif args.subtract:
  difference = args.x - args.y
  print('Difference:', difference)

'''
if a parameter has action store_true but is missing in the command line, the default value will be False, 
otherwise, the value will be True. Similarly, if a parameter has action store_false but is missing in the command line, 
the default value will be True, otherwise, the value will be False.

'''