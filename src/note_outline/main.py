import argparse
import os

from src.note_outline.cli import create_cli, validate_cli
from src.note_outline.file_io import read_file, write_file
from src.note_outline.note_manipulation import compile_output_file, count_links, get_file_names


def main():
    # try:
    args = create_cli()
    # except SystemExit:
    #     pass

    try:
        validate_cli(args)
        try:
            dir = os.path.dirname(args.file)

            if dir[:1] == "/":
                dir += "/"
            else:
                dir += "./"

            filename = os.path.basename(args.file)
        except UnboundLocalError:
            pass

        print("Reading " + filename)
        try:
            file_text = read_file(dir + filename)
        except FileNotFoundError as e:
            print(e)

        print("Parsing text from " + filename)
        linked_file_names = get_file_names(dir, filename, file_text)
        print("Found " + str(count_links(linked_file_names)) + " internal links")

        print("Compiling text")
        output_file = compile_output_file(dir, file_text, linked_file_names)

        if args.output is not None:
            print("Writing " + args.output)
            try:
                write_file((dir + args.output), output_file)
            except FileNotFoundError as e:
                print(e)
        elif args.inplace is not None:
            print("Writing " + filename)
            try:
                write_file((dir + filename), output_file)
            except FileNotFoundError as e:
                print(e)
        else:
            print("Writing to standard output\n")
            for line in output_file:
                print(line, end="")
            print("\n")

        print("Done")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
