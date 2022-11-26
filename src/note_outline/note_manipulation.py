import re
import os

from src.note_outline.file_io import read_file


def get_links(filename, file_text):
    file_uid = ''.join(re.findall('[0-9]{12}', filename))
    pattern = '\[\[[0-9]{12}\]\]'
    links = {}
    for no, line in enumerate(file_text):
        matches = re.findall(pattern, line)
        if matches:
            for match in matches:
                temp = match.strip('[[]]')
                if match.strip('[[]]') == file_uid:
                    matches.remove(match)
            links.update({no: matches})

    return links


def count_links(links):
    count = 0

    for line, line_links in links.items():
        for link in line_links:
            count += 1

    return count


def get_file_names(dir, filename, file_text):
    links = get_links(filename, file_text)
    file_names = {}
    files_in_dir = set()

    for root, dirs, files in os.walk(dir, topdown=False):
        files_in_dir = files

    for line, line_links in links.items():
        temp = []
        for link in line_links:
            for f in files_in_dir:
                if re.search(link.strip("[[]]"), f) is not None:
                    temp.append(f)
        file_names.update({line: temp})
    return file_names


def compile_output_file(dir, file_text, file_names):
    output_file = []

    for no, line in enumerate(file_text):
        output_file.append(line)

        if no in file_names:
            for file in file_names[no]:
                output_file.append("<!--\n")
                output_file.append("    " + file + "\n")
                linked_file_text = read_file(dir + file)

                if linked_file_text[-1][-1:] != "\n":
                    linked_file_text.append("\n")

                for linked_lines in linked_file_text:
                    output_file.append("    " + linked_lines)
                output_file.append("-->\n")

    return output_file


def clean_outline_file(file_text):
    in_comment = False
    outfile_text = []
    for line in file_text:
        if line == "<!--\n":
            in_comment = True
        if not in_comment:
            outfile_text.append(line)
        elif line == "-->\n":
            in_comment = False
    return outfile_text
