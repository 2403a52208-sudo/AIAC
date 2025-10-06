def read_file(filename):
    """Read and return the full contents of a text file.

    Returns the file contents as a string, or None if the file does not
    exist or another I/O error occurs.
    """
    try:
        with open(filename, "r") as f:
            data = f.read()  # Read entire file into memory
        return data
    except FileNotFoundError:
        # Handle the common case where the provided path doesn't exist
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        # Catch unexpected I/O errors (permissions, encoding, etc.)
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Simple CLI flow: prompt for a path, read, then display contents
    filename = input("Enter the filename to read: ")
    content = read_file(filename)
    if content is not None:
        print("File contents:")
        print(content)
    # Otherwise, errors were already printed by read_file
