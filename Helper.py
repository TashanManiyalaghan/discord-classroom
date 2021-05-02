def parse_inputs(string)

    params = []
    param = ''
    sentence = False

    for index in range(len(string)):

        if string[index] == '\"' or string[index] == '\'':
            if sentence:
                params.append(param)
                param = ''
            sentence = not sentence

        else:
            if sentence or (not sentence and string[index] != ' '):
                param = param + string[index]

        if not sentence and len(param) > 0 and string[index] == ' ':
            params.append(param)
            param = ''

    return params