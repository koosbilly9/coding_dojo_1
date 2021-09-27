# recommended comand line arguments module

import argparse


parser = argparse.ArgumentParser("learn argparse")

# add_mutually_exclusive_group()
group = parser.add_argument_group()

# with action="store_true" it check only if flag is true or false
group.add_argument("--verbose", "-v",
                    help="increase output verbosity",
                    type=int,
                    default=0)

# quit - the opposite of verbose
group.add_argument("--quiet", "--q",
                   help=" opposite of verbose",
                   action="store_true")

# Position argument 1st args assign to variable "square"
parser.add_argument("square",
                    help="display square of given number",
                    type=int)

# optional parameter denoted by "--" , shortcut --p created for free
# type is int
parser.add_argument("--power", "-p",
                    help="raise to power",
                    default=2,
                    type=int)


#choices restrict input to valid choices
parser.add_argument("--format", "-f",
                    help="output format json or test",
                    choices=['j', 'J', 't', 'T'],
                    default="T" )

args = parser.parse_args()


if args.quiet:
    print(args.square ** args.power)
elif args.verbose >= 2:
    print(f"the power of {args.power} of {args.square} eqauls {args.square**args.power}")
elif args.verbose >= 1:
    print(f"{args.power}^{args.square} = {args.square**args.power}")
else:
    print(args.square ** args.power)



if args.format.upper() == "J":
    print("some json ")
elif args.format.upper() == "T":
    print("some text")