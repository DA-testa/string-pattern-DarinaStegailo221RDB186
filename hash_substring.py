# python3
# 221RDB186 Darina Stegailo 7.grupa

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p])
    occurrences = []

    for i in range(t - p + 1):
        if p_hash == t_hash and pattern == text[i:i+p]:
            occurrences.append(i)

        if i < t - p:
            t_hash = hash(text[i+1:i+p+1])

    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
