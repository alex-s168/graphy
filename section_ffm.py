import sys


def parse(lines: list[str]) -> dict[str, str]:
    file_sections = {}
    temp = ""
    curr_section = ""

    for line in lines:
        line = line.split('#')[0].strip()

        if line.startswith('['):
            if ']' not in line:
                print("Invalid section_ffm!")
                sys.exit(1)

            file_sections[curr_section] = temp[:]
            temp = ""
            curr_section = line[1:-1]

        else:
            temp += line + '\n'

    file_sections[curr_section] = temp

    return file_sections
