import os
import re
import json
from exterms import parse_name


def merge_dict(idx1, idx2):
    """to merge 2 dictionarys"""
    for k, v in idx2.items():
        if k in idx1.keys():
            idx1[k] += v
        else:
            idx1[k] = v
    return idx1


def dir_walk(current_dir):
    try:
        dirname = current_dir.name
    except AttributeError:
        dirname = current_dir
        index = {'count': 0}
    else:
        index = {'count': 0, dirname: 10}
    print(dirname, "parsing...... ", os.path.abspath(current_dir))
    with os.scandir(current_dir) as it:
        for entry in it:
            if (not entry.name.startswith('.') and entry.is_dir()):
                index = merge_dict(index, dir_walk(entry))  # merge subdir's to
            elif entry.is_file() and entry.name.endswith('pdf'):
                words = parse_name(entry.name)
                while words:
                    word = words.pop()
                    if index.get(word):
                        index[word] += 1
                    else:
                        index[word] = 1
                    index['count'] += 1

    index_file = os.path.join(os.path.abspath(current_dir), '.index')
    json.dump(index, open(index_file, 'w'))
    return index


dir_walk('C:\\Users\\jimmy\\books')
# dir_walk('.')
