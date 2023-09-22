def stylish(data, symb='    ', count=1, depth=0):
    result = []
    if not isinstance(data, (list, tuple, set, dict)):
        if str(data) == 'False':
            return 'false'
        elif str(data) == 'True':
            return 'true'
        elif str(data) == 'None':
            return 'null'
        else:
            return str(data)
    cur_sym = symb * depth * count
    if isinstance(data, (dict)):
        result.append('{')
        for key in data.keys():
            if key[0] == ' ':
                result.append(cur_sym + key + ': '
                              + stylish(data[key], symb, count, depth + 1)
                              )
            else:
                result.append((symb * (depth + count)) + 
                              key + ': ' + 
                              stylish(data[key], symb, count, depth + 1))
    result.append(symb * (depth) * count + '}')
    return '\n'.join(result)
