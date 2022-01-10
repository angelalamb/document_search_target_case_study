from string_match import *
from RandomWordGenerator import RandomWord
import statistics

NANO_TO_MS = 1000000
SEARCH_NUM = 2000000

# Opened and processed files.
french_armed_forces = clean_file("sample_text/french_armed_forces.txt")
hitchhikers = clean_file("sample_text/hitchhikers.txt")
warp_drive = clean_file("sample_text/warp_drive.txt")

def perf_test(method, file_name):
    r = RandomWord(constant_word_size=False)
    result = 0
    if method == index_match:
        start = time.perf_counter_ns()
        file_dict = create_dict(file_name)
        for i in range(SEARCH_NUM):
            term = r.generate() 
            method(file_dict, term)
        end = time.perf_counter_ns()
        result += (end - start)
    else:
        start = time.perf_counter_ns()
        term = r.generate()
        for i in range(SEARCH_NUM):
            term = r.generate()
            method(file_name, term)
        end = time.perf_counter_ns()
        result += (end - start)
    result //= NANO_TO_MS

    return result 

# Script for peformance testing. Simply change the method called in performance testing
# to regex_match, or simple_match to test the other methods. You can also change which file
# to search in the second parameter.
results = []
for i in range(10): 
    result = perf_test(index_match, french_armed_forces)
    results.append(result)

print("Mean: %d ms" % statistics.mean(results))
print("Median: %d ms" % statistics.median(results))
