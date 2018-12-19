import fileinput

if __name__ == '__main__':
    freq = 0
    for line in fileinput.input():
        freq = freq + int(line)
    print(freq)
