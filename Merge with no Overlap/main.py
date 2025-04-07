class FileX:
    def __init__(self, range_start: int, range_end: int, data: str):
        self.range_start = range_start
        self.range_end = range_end
        self.data = data

    def __repr__(self):
        return f"{self.range_start}|{self.range_end}|{self.data}|"


def read_file(filename: str) -> list[FileX]:
    entries = []
    with (open(filename, 'r') as file):
        for line in file:
            parts = []
            # Remove any leading/trailing whitespace and split by '|'
            parts_aux = line.strip().split('|')
            # Filter out empty strings from split (in case of || or trailing |)
            for part in parts_aux:
                if part:
                    parts.append(part)

            if len(parts) == 3:
                entries.append(FileX(int(parts[0]), int(parts[1]), parts[2]))

    return entries


if __name__ == "__main__":
    # Read and parse the file
    entries = read_file("FileX.txt")

    # Print the parsed entries
    for entry in entries:
        print(entry)