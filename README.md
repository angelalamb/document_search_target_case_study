# Target Case Study: Document Search

## Requirements
The goal of this exercise is to create a working program to search a set of documents for the given search term or phrase (single token), and return results in order of relevance. 
Relevancy is defined as number of times the exact term or phrase appears in the document. 
Create three methods for searching the documents: 
•	Simple string matching
•	Text search using regular expressions
•	Preprocess the content and then search the index
Prompt the user to enter a search term and search method, execute the search, and return results. For instance:

Enter the search term: <user enters search term>
Search Method: 1) String Match 2) Regular Expression 3) Indexed
Search results: 
    File2.txt – X matches
    File1.txt - X matches
    File3.txt – X matches
Elapsed time: 40 ms

Three files have been provided for you to read and use as sample search content.
Run a performance test that does 2M searches with random search terms, and measures execution time. Which approach is fastest? Why?
Provide some thoughts on what you would do on the software or hardware side to make this program scale to handle massive content and/or very large request volume (5000 requests/second or more). 

## Solution
My solution is in string_match.py, with unit tests in tests.py and a performance test in perf_test.py

Python modules used in this project:
re
time
unittest
statistics
RandomWordGenerator

Some assumptions: My search is agnostic towards puncuation as well as captilization in both the file words and the term or phrase the user enters.

My results from the performance test (2M searches each performed 10 times) are as follows:

Index match:
    Mean: 221 ms
    Median: 215 ms

Regex Match:
    Mean: 369737 ms
    Median: 348459 ms

Simple Match:
    Mean: 554461 ms
    Median: 548220 ms

Is this code production ready? No, for several reasons.
1) I did not address security concerns where users could inject malicious code as an input.
2) Currently this project only searches three sample files.
3) My code has not undergone a code review.

