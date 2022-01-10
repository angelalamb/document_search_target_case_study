import re
import time

NANO_TO_MS = 1000000

# Clean text line of the following puncuations characters: "',.:;?! and make all characters 
# lowercase then join the words together with one space each.
def clean_text(text):
    punc = "\"',.:;?!"
    replace = "        "
    replace_table = text.maketrans(punc, replace)
    text = text.translate(replace_table).lower()
    return ' '.join(text.split())

# Open and read the file. Then close the file and the clean the text.
def clean_file(file):
    file = open(file, 'r')
    text = file.read()
    file.close()
    return clean_text(text)

def main():
    french_armed_forces = clean_file("sample_text/french_armed_forces.txt")
    hitchhikers = clean_file("sample_text/hitchhikers.txt")
    warp_drive = clean_file("sample_text/warp_drive.txt")
    results = dict()
    term = input("Enter the search term: ")
    method = input("Search Method: 1) String Match 2) Regular Expression 3) Indexed ")

    # Clean the term or phrase.
    term = clean_text(term)

    # Call methods
    if method == '1':
        start = time.perf_counter_ns()
        results_french_forces = simple_match(french_armed_forces, term)
        results_hitchhickers = simple_match(hitchhikers, term)
        results_warp_drive = simple_match(warp_drive, term)
        end = time.perf_counter_ns()
    elif method == '2':
        start = time.perf_counter_ns()
        results_french_forces = regex_match(french_armed_forces, term)
        results_hitchhickers = regex_match(hitchhikers, term)
        results_warp_drive = regex_match(warp_drive, term)
        end = time.perf_counter_ns()
    elif method == '3':
        start = time.perf_counter_ns()
        french_armed_forces_dict = create_dict(french_armed_forces)
        hitchhikers_dict = create_dict(hitchhikers)
        warp_drive_dict = create_dict(warp_drive)
        results_french_forces = index_match(french_armed_forces_dict, term)
        results_hitchhickers = index_match(hitchhikers_dict, term)
        results_warp_drive = index_match(warp_drive_dict, term)
        end = time.perf_counter_ns()
    else:
        print("Invalid input")
        return

    # Convert the elasped time to milleseconds (ms).
    total_time = (end - start) / NANO_TO_MS

    # Insert files names and results into a dictionary.
    results["french_armed_forces.txt"] = results_french_forces
    results["hitchhikers.txt"] = results_hitchhickers
    results["warp_drive.txt"] = results_warp_drive

    # Sort the dictionary based on the results: highest number of results to lowest number of results. 
    sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

    print("Search results: ")
    for file, count in sorted_results.items():
        print("\t %s - %d" % (file, count))

    print("Elasped Time: %d ms" % total_time)

########################################### Functons ########################################################

# Simple string match
def simple_match(text, term):
    result = 0
    terms = term.split()
    words = text.split()
    i = 0
    while (i < len(words)):
        if words[i:i+len(terms)] == terms:
            result += 1
            i += len(terms)
        else:
            i += 1
    return result

# Regex match
def regex_match(text, term):
    result = 0
    p = re.compile(r'\b(%s)\b'%term)
    matches = p.findall(text)
    # Matches is a list of all the found matches in the text.
    result += len(matches)
    return result

# Create a dictionary for index_match.
def create_dict(text):
    word_dict = dict()
    idx = 0
    text = text.split()
    for word in text:
        if word in word_dict:
            word_dict[word] += [idx]
        else:
            word_dict[word] = [idx]
        idx += 1
    return word_dict

# Does the given dictionar contain the list of terms at consecutive indexes?
def index_match_helper(file_dict, terms, idx):
    curr_idx = idx + 1
    for i in range(1, len(terms)):
        if terms[i] not in file_dict.keys() or curr_idx not in file_dict[terms[i]]:
            return False
        else:
            curr_idx += 1
    return True

# Index search
def index_match(file_dict, term):
    result = 0
    terms = term.split()
    if len(terms) == 1 and term in file_dict.keys():
        return len(file_dict[term])
    if terms[0] in file_dict.keys():
        # Look at each instance of the first term.
        idxs = file_dict[terms[0]]
        for idx in idxs: 
            if index_match_helper(file_dict, terms, idx):
                result += 1   
    return result

if __name__ == "__main__":
    main()