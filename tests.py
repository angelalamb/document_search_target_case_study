from string_match import *
import unittest

test_file_1 = clean_file("sample_text/test_1.txt")
french_armed_forces = clean_file("sample_text/french_armed_forces.txt")
hitchhikers = clean_file("sample_text/hitchhikers.txt")
warp_drive = clean_file("sample_text/warp_drive.txt")

class TestStringMatchMethonds(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hi, this is Wolfrick!"), "hi this is wolfrick")
        self.assertEqual(clean_text("no puncuation at all"), "no puncuation at all")
    
    def test_clean_file(self):
        self.assertEqual(clean_file("sample_text/test_1.txt"), "hi this is wolfrick")
    
    def test_create_dict(self):
        self.assertEqual(create_dict(test_file_1), {"hi":[0], "is":[2], "this":[1], "wolfrick":[3]})
    
    def test_index_match(self):
        self.assertEqual(index_match(create_dict(test_file_1), clean_text("Wolfrick")), 1)
        self.assertEqual(index_match(create_dict(test_file_1), clean_text("Wolf")), 0)
        self.assertEqual(index_match(create_dict(test_file_1), clean_text("Hi this")), 1)
        self.assertEqual(index_match(create_dict(test_file_1), 
                         clean_text("hi this is wolfrick and winston")), 0)
        self.assertEqual(index_match(create_dict(test_file_1), clean_text("h")), 0)
        self.assertEqual(index_match(create_dict(french_armed_forces), clean_text("french")),11)
        self.assertEqual(index_match(create_dict(hitchhikers), clean_text("trilogy")),1)
        self.assertEqual(index_match(create_dict(warp_drive), clean_text("star")), 3)
        
    
    def test_index_match_helper(self):
        self.assertTrue(index_match_helper(create_dict(test_file_1), ["this", "is"], 1))
        self.assertFalse(index_match_helper(create_dict(test_file_1), ["is", "this"], 2))
    
    def test_simple_match(self):
        self.assertEqual(simple_match(test_file_1, clean_text("Wolfrick")), 1)
        self.assertEqual(simple_match(test_file_1, clean_text("this is")), 1)
        self.assertEqual(simple_match(test_file_1, clean_text("Hi this")), 1)
        self.assertEqual(simple_match(test_file_1, clean_text("Wolf")), 0)
        self.assertEqual(simple_match(test_file_1, clean_text("hi this is wolfrick and winston")), 0)
        self.assertEqual(simple_match(test_file_1, clean_text("h")), 0)
        self.assertEqual(simple_match(french_armed_forces, clean_text("french")),11)
        self.assertEqual(simple_match(hitchhikers, clean_text("trilogy")), 1)
        self.assertEqual(simple_match(warp_drive, clean_text("star")), 3)
    
    def test_regex_match(self):
        self.assertEqual(regex_match(test_file_1, clean_text("hi")), 1)
        self.assertEqual(regex_match(test_file_1, clean_text("Wolfrick")), 1)
        self.assertEqual(regex_match(test_file_1, clean_text("this is")), 1)
        self.assertEqual(regex_match(test_file_1, clean_text("Hi this")), 1)
        self.assertEqual(regex_match(test_file_1, clean_text("Wolf")), 0)
        self.assertEqual(regex_match(test_file_1, clean_text("hi this is wolfrick and winston")), 0)
        self.assertEqual(regex_match(test_file_1, clean_text("h")), 0)
        self.assertEqual(regex_match(french_armed_forces, clean_text("french")),11)
        self.assertEqual(regex_match(hitchhikers, clean_text("trilogy")),1)
        self.assertEqual(regex_match(warp_drive, clean_text("star")), 3)
    

if __name__ == '__main__':
    unittest.main()


    

