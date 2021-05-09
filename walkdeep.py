import os
import json
from exterms import parse_name


def dir_walk(current_dir):
    print("searching...... ", current_dir, os.path.abspath(current_dir))
    index = {'count': 0}

    with os.scandir(current_dir) as it:
        for entry in it:
            if (not entry.name.startswith('.') and entry.is_dir()):
                dir_walk(entry)
            elif (entry.is_file() and not entry.name.startswith('.') and
                    not entry.name.endswith('ini')):
                words = parse_name(entry.name)
                while words:
                    word = words.pop()
                    if index.get(word):
                        index[word] = index[word] + 1
                    else:
                        index[word] = 1
                    index['count'] = index['count'] + 1

    index_file = os.path.join(os.path.abspath(current_dir), '.index')
    json.dump(index, open(index_file, 'w'))
    return None


dir_walk('C:\\Users\\jimmy\\books')
# dir_walk('.')
