"""Handle the arguments provided to GatorGrader"""

import argparse


def parse(args):
    """Parses the arguments provided on the command-line"""
    # create the parser with the default help formatter
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # do not display the welcome message
    gg_parser.add_argument(
        "--nowelcome", help="Do not display the welcome message", action="store_true"
    )

    # specify a file and a directory
    gg_parser.add_argument("--file", type=str)
    gg_parser.add_argument("--directory", type=str)

    gg_parser.add_argument("--singlecomments", nargs="+", type=int)

    gg_parser.add_argument("--multicomments", nargs="+", type=int)

    gg_parser.add_argument("--paragraphs", nargs="+", type=int)
    gg_parser.add_argument(
        "--wordcount", "--sentences", nargs="+", type=int, dest="wordcount"
    )

    gg_parser.add_argument("--fragments", nargs="+", type=str)
    gg_parser.add_argument("--fragmentcounts", nargs="+", type=int)

    gg_parser.add_argument("--languages", nargs="+", type=str)

    gg_parser.add_argument("--commands", nargs="+", type=str)
    gg_parser.add_argument("--outputlines", nargs="+", type=int)

    gg_parser.add_argument("--commits", type=int)

    gg_arguments_finished = gg_parser.parse_args(args)
    return gg_arguments_finished


def verify(args):
    """Checks if the arguments are correct"""
    verified_arguments = False
    # both a file and a directory were specified
    if args.directory is not None and args.file is not None:
        verified_arguments = True
    return verified_arguments
