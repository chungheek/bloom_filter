# bloom_filter.py
# References:
# https://www.kdnuggets.com/2016/08/gentle-introduction-bloom-filter.html
# https://llimllib.github.io/bloomfilter-tutorial/

from bitarray import bitarray
import mmh3

bit_arr_size = 623518  # can change to test different arguments
hash_func_count = 1  # can change to test different arguments
dictionary = 'dictionary.txt'  # can change to test different arguments
input_f = 'sample_input.txt'  # can change to test different arguments


class BloomFilter(set):

    """
    BloomFilter takes in a size and hash_func_count arguments which
    creates a bitarray with given size and will hash hash_func_count
    times for a given string
    """

    def __init__(self, size, hash_func_count):
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_func_count = hash_func_count

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.bit_array)

    ''' Adds a word to the bloom filter '''

    def add(self, word):
        for i in range(self.hash_func_count):
            index = mmh3.hash(word, i) % self.size
            self.bit_array[index] = 1

        return self

    ''' Will return true or false if word is in bloom filter '''

    def __contains__(self, word):
        out = True
        for i in range(self.hash_func_count):
            index = mmh3.hash(word, i) % self.size
            if self.bit_array[index] == 0:
                out = False

        return out


def main():
    bloom = BloomFilter(bit_arr_size, hash_func_count)
    dict_file = open(dictionary, 'r', encoding="utf8", errors='ignore')
    dict_lines = [dict_line.strip() for dict_line in dict_file]

    num = 0
    # Add dictionary to bloom filter
    for line in dict_lines:
        num += 1
        bloom.add(line)

    dict_file.close()

    # Gather input from a file
    input_file = open(input_f, 'r', encoding="utf8",
                      errors='ignore')
    input_lines = [input_line.strip() for input_line in input_file]

    # See if input is in bloom filter
    for input_words in input_lines:
        if input_words in bloom:
            print('Maybe')
        else:
            print('No')


if __name__ == '__main__':
    main()
