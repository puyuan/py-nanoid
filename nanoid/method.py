from math import ceil, log

from algorithm import algorithm_generate as algorithm


def method(algorithm, alphabet, size):
    alphabet_len = len(alphabet)

    mask = 2
    if alphabet_len > 1:
        mask = (2 << int(log(alphabet_len - 1) / log(2))) - 1
    step = int(ceil(1.6 * mask * size / alphabet_len))

    id = ''
    while True:
        random_bytes = algorithm(step)

        for i in range(step):
            random_byte = random_bytes[i] & mask
            if random_byte < alphabet_len:
                if alphabet[random_byte]:
                    id += alphabet[random_byte]

                    if len(id) == size:
                        return id