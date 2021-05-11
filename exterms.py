import re


def exclude_word(word_list):
    prepositions = [
        'aboard', 'about', 'above', 'across', 'after', 'against', 'along',
        'amid', 'among', 'around', 'before', 'behind', 'below', 'beneath',
        'beside', 'between', 'beyond', 'but', 'concerning', 'considering',
        'despite', 'down', 'during', 'except', 'following', 'for', 'from',
        'inside', 'into', 'like', 'minus', 'near', 'next', 'off', 'onto',
        'opposite', 'out', 'outside', 'over', 'past', 'per', 'plus',
        'regarding', 'round', 'save', 'since', 'than', 'through', 'till',
        'toward', 'under', 'underneath', 'unlike', 'until', 'upon', 'versus',
        'via', 'with', 'within', 'without', 'the', 'and',
        ]
    publishers = [
        'apress', 'packt', 'oreilly', 'reilly', 'addison', 'wesley', 'john',
        'wiley', 'manning', 'mcgraw', 'hill', 'prentice', 'hall', 'pearson',
        'springer',
        ]
    months = [
        'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
        'oct', 'nov', 'dec',
    ]
    excludes = prepositions + publishers + months
    [word_list.remove(wd) for pb in excludes for wd in word_list if wd == pb]
    return word_list


def parse_name(file_name):
    string = file_name.lower()
    pattern = '[a-zA-Z]{3,20}'
    result = re.findall(pattern, string)
    wordlst = exclude_word(result)
    return wordlst
