import argparse
import os

def create_cli():
    parser = argparse.ArgumentParser(
        description="A tool to compile an outline from notes in your zettelkasten."
    )
    parser.add_argument(
        "file",
        type=os.path.abspath,
        help="an outline file"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="an output file"
    )
    parser.add_argument(
        "-i",
        "--inplace",
        default=None,
        action="store_true",
        help="save outline file in place (overriding original file)"
    )
    parser.add_argument(
        "-d",
        "--delete",
        default=None,
        action="store_true",
        help="delete outline comments from file"
    )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.0.1')
    args = None
    try:
        args = parser.parse_args()
    except SystemExit:
        pass

    return args


def validate_cli(args):
    count = 0

    for arg in [args.output, args.inplace]:
        if arg:
            count += 1

    if count > 1:
        raise Exception("Please enter only one optional argument.")
