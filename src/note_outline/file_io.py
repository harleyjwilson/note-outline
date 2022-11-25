def read_file(filename):
    note_text = None

    try:
        file = open(filename, "r")
        note_text = file.readlines()
    except FileNotFoundError as e:
        print("Error reading file: ", e)

    return note_text


def write_file(filename, text):
    try:
        file = open(filename, "w")
        file.writelines(text)
    except FileNotFoundError as e:
        print("Error writing file: ", e)
    except TypeError as e:
        print("Error writing file: ", e)
