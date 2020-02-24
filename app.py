from app.stream.file_stream import FileStream
import sys

if __name__ == "__main__":
    f = FileStream()
    f.read_from_source(source=sys.stdin)