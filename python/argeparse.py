
#Volume of a Cylinder using argeparse

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a Cyliner')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of Cylinder')
# -- prefix in front of the arguments turn them into optional, instead of positional.

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()
# Adding mutually exclusive group means only one of these options can be parsed.
# Eg : python3 argeparse.py -H -r 2 -v


# vol = (math.pi)*rad*height
# print(vol)

def cylinder_volume(radius, height):
    vol = (math.pi)*(radius ** 2)*(height)
    return vol

if __name__ == '__main__':
    volume = cylinder_volume(args.radius,args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"Volume of a Cylinder with radius {args.radius} and height {args.height} is {volume}")
    else:
       print(f"Volume of the Cylinder = {volume}")

