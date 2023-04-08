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
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = 10**9 + 7
    x = 263
    occurrences = []
    n, m = len(text), len(pattern)
    h = pow(x, m-1, p)
    pattern_hash = sum(ord(pattern[i])*pow(x, i, p) for i in range(m)) % p
    text_hash = sum(ord(text[i])*pow(x, i, p) for i in range(m)) % p

    for i in range(n-m+1):
        if pattern_hash == text_hash and pattern == text[i:i+m]:
            occurrences.append(i)
        if i < n-m:
            text_hash = (text_hash - ord(text[i])*h) % p
            text_hash = (text_hash*x + ord(text[i+m])) % p
            text_hash = (text_hash + p) % p

    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
