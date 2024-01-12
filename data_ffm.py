import sys


def parse(lines: list[str]) -> list[dict[str, str]]:
    if len(lines) == 0:
        print("Invalid data_ffm!")
        sys.exit(1)

    header = lines[0].split(',')

    out_data = []

    for line in lines[1:]:
        data = line.split(',')

        if len(data) != len(header):
            print("Invalid data_ffm!")
            sys.exit(1)

        g = {}

        for i, h in enumerate(header):
            g[h] = data[i]

        out_data.append(g)

    return out_data
