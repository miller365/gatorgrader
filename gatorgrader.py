""" GatorGrader checks the files of programmers and writers """

import argparse
import sys

import gatorgrader_files


def parse_gatorgrader_arguments(args):
    """ Parses the arguments provided on the command-line """
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    gg_parser.add_argument('--checkfiles', nargs='+', type=str)
    gg_parser.add_argument('--directories', nargs='+', type=str)

    gg_arguments = gg_parser.parse_args(args)
    return gg_arguments


def verify_gatorgrader_arguments(args):
    """ Checks if the arguments are correct """
    verified_arguments = True
    if args.checkfiles is not None and args.directories is None:
        verified_arguments = False
    elif args.directories is not None and args.checkfiles is None:
        verified_arguments = False
    elif len(args.directories) != len(args.checkfiles):
        verified_arguments = False
    return verified_arguments
    print(len(args.directories))


def display_welcome_message():
    """ Display a welcome message """
    print()
    print("GatorGrader: Automatically Check Files of Programmers and Writers")
    print("https://github.com/gkapfham/gatorgrader")
    print()



if __name__ == '__main__':
    display_welcome_message()
    # parse and verify the arguments
    gg_arguments = parse_gatorgrader_arguments(sys.argv[1:])
    did_verify_arguments = verify_gatorgrader_arguments(gg_arguments)
    if did_verify_arguments is False:
        print("Incorrect command-line arguments.")
        sys.exit(2)
    else:
        print("Valid command-line arguments")
        print("Running the specified checks!")
        print()
