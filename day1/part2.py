import fileinput
import itertools

if __name__ == '__main__':
    input_list = fileinput.input()
    freq_map = {0: 1}
    freq = 0
    seen = None
    for line in itertools.cycle(input_list):
        freq = freq + int(line)
        try:
            seen = freq_map[freq]
            break
        except:
            freq_map[freq] = freq
            continue
    print(seen)
