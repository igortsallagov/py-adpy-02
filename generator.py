import hashlib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'war_piece.txt'
file_path = os.path.join(current_dir, file_name)


def md5_generator(path):
    for row in open(path, 'r'):
        result = hashlib.md5(row.encode())
        yield result.hexdigest()
