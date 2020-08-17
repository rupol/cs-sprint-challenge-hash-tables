# input: list of filepaths and list of filename queries
# output: all the filepaths that match the given queries

def finder(files, queries):
    # keys: filename
    # values: array of file paths
    result = []
    for filepath in files:
        # strip path down to filename (the last element if split on /)
        split_path = filepath.split("/")
        filename = split_path[-1]
        if filename in queries:
            result.append(filepath)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/bar',
        '/usr/bin/baz',
        '/trash/baz',
        '/bin/qux',
        '/usr/bin/qux',
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
