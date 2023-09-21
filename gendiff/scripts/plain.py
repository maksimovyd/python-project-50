def plain(res_dict, dict_one, dict_two, path=[], res_str=''):
    res_str = ''
    for key, value in res_dict.items():
        path.append(key[4:])
        if key[:1] == ' ':
            if isinstance(value, dict):
                if key[4:] in dict_one and key[4:] in dict_two:
                    if (isinstance(dict_one[key[4:]], dict) and
                            isinstance(dict_two[key[4:]], dict)):
                        res_str += (
                            plain(
                                res_dict[key], dict_one[key[4:]],
                                dict_two[key[4:]], path, res_str=res_str))
                        if len(path) > 0:
                            path.pop()
                        continue
        substring = ''
        if key[4:] in dict_one and key[4:] not in dict_two:
            substring = f'Property \'{".".join(path)}\' was removed\n'
        elif (key[4:] in dict_one and key[4:] in dict_two and
              dict_one[key[4:]] != dict_two[key[4:]]):
            substring = (
                f'Property \'{".".join(path)}\' was updated. '
                f'From {refund_val(dict_one[key[4:]])} '
                f'to {refund_val(dict_two[key[4:]])}\n')
        elif key[4:] not in dict_one and key[4:] in dict_two:
            substring = (
                f'Property \'{".".join(path)}\' was '
                f'added with value: {refund_val(value)}\n')
        if substring not in res_str:
            res_str += substring
        if len(path) > 0:
            path.pop()
    return res_str


def refund_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif str(value) == 'False':
        return 'false'
    elif str(value) == 'True':
        return 'true'
    elif str(value) == 'None':
        return 'null'
    else:
        return f'\'{value}\''
