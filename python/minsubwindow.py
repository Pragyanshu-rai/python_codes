def key_check(string, keys):

    for key in keys:

        if key not in string:

            return False

    return True


def get_window(string, keys):

    if key_check(string, keys) == False:

        return ""

    start = 0
    end = len(string)-1

    while True:

        if key_check(string[start:], keys) == False:

            if start != 0:
                start -= 1
            break

        start += 1

    # print(string[start:])

    while True:

        if key_check(string[start:end+1], keys) == False:
            
            end += 1
            break

        end -= 1

    return string[start:end+1]


x, x, = input().split(" ")
string = input()
keys = input()

print(get_window(string, keys))
