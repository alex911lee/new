import os
import json
from exterms import parse_name


def move_file(current_dir):
    print("searching...... ", current_dir, os.path.abspath(current_dir))
    index = {}
    index_file = os.path.join(os.path.abspath(current_dir), '.index')

    try:
        index = json.load(open(index_file, 'r'))
    except FileNotFoundError:
        index['count'] = 0

    with os.scandir(current_dir) as it:
        for entry in it:
            if (not entry.name.startswith('.') and entry.is_dir()):
                move_file(entry)
            if (entry.is_file() and entry.name.endswith('pdf')):
                book_words = parse_name(entry.name)
                while book_words:
                    word = book_words.pop()
                    if index.get(word):
                        index[word] = index[word] + 1
                    else:
                        index[word] = 1
                    index['count'] = index['count'] + 1
    json.dump(index, open(index_file, 'w'))
    return None


move_file('C:\\Users\\jimmy\\books')
# dir_walk('.')
