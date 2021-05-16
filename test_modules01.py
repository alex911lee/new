import pytest


def merge_dict(idx1, idx2):
    """to merge 2 dictionarys"""
    for k, v in idx2.items():
        if k in idx1.keys():
            idx1[k] += v
        else:
            idx1[k] = v
    return idx1


def test_case01():
    dic1 = {
        "count": 15, "way": 1, "hard": 1, "python": 9, "more": 1, "learn": 3,
        }
    dic2 = {
        "count": 22, "recurrent": 1, "requests": 1, "pandas": 7, "using": 3,
        "python": 5,
        }

    assert merge_dict(dic1, dic2) == {
        "count": 37, "way": 1, "hard": 1, "python": 14, "more": 1, "learn": 3,
        "recurrent": 1, "requests": 1, "pandas": 7, "using": 3,
        }
