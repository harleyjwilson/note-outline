import argparse

def create_cli():
    parser = argparse.ArgumentParser(
        description="A tool to compile an outline from notes in your zettelkasten."
    )
    parser.add_argument(
        # "file", 
        "-f", 
        "--file", 
        required=True,
        type=str,
        help="an outline file"
    )
    # parser.add_argument(
    #     # "archive",
    #     "-a",
    #     "--archive",
    #     required=True,
    #     type=str,
    #     help="path to your zettelkasten"
    # )
    parser.add_argument(
        # "output",
        "-o",
        "--output",
        required=True,
        type=str,
        help="output file"
    )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.0.1')
    args = parser.parse_args()
    
    return args  

