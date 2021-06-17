# bloom_filter.py

bloom_filter.py is a python script that utilizes the bloom filter data structure and the
class constructed is taken from https://www.kdnuggets.com/2016/08/gentle-introduction-bloom-filter.html.
Using this BloomFilter class we add dictionary.txt to the bitarray and we need a sample_input.txt file
and it will tell us if the input in the file are in the bloom filter or not. This file was created and
tested on python 3.6.8

Following lines can be changed:
- 9: bit_arr_size
- 10: hash_func_count
- 11: dictionary
- 12: input_f

Need:
- argument for bit_arr_size (preferably greater than size of dictionary)
- argument for hash_func_size (preferably fewer times so less bits are set)
- dictionary file
- input file

In order to run:
- python3 -m venv (arbitrary name of venv)
- source (virtualenv name)/bin/activate
- pip install bitarray
- pip install mmh3
	- OR run 'pip install -r requirements.txt' (given in folder)
- python3 bloom_filter.py

Sample data gathered from playing around with bit array size and hash function count:<br>
|	Bloom Arguments 										|				Results							|
| ----------------------------------- | ------------------------- |
| bloom = BloomFilter(623518, 10) 		| Doesn't filter						|
| bloom = BloomFilter(623518*2, 10) 	| Doesn't filter						|
| bloom = BloomFilter(623518*3, 10) 	| Filters 3/5 negatives			|
| bloom = BloomFilter(623518 * 6, 10) | Filter works successfully |
| bloom = BloomFilter(623518*3, 50) 	| Doesn't filter						|
| bloom = BloomFilter(623518*6, 9) 		| Filter works successfully |
| bloom = BloomFilter(623518, 1) 			| Filter works successfully |
| bloom = BloomFilter(623518 * 6, 20) | Filters 4/5 negatives			|
