from src.FileX import FileX

if __name__ == "__main__":
    # Read and parse the file
    entries = FileX.read_file("FileX.txt")

    # Print the parsed entries
    for entry in entries:
        print(entry)
