import unittest

import requests, json
from argparse import ArgumentParser
from get_posts import cmdline_args, api_call, data_output
from unittest.mock import patch, call

class GetPostsTest(unittest.TestCase):
        
    def test_api_call_all(self):
        with open('testdataall.txt', 'r') as filehandle:
            data = json.load(filehandle)
        with patch('argparse._sys.argv', ['get_posts.py']):
            fakeargs = cmdline_args()
        self.assertEqual(api_call(fakeargs), data)
    
    def test_api_call_first_5(self):
        with open('testdata5.txt', 'r') as filehandle:
            data = json.load(filehandle)
        with patch('argparse._sys.argv', ['get_posts.py','--end', '5']):
            fakeargs = cmdline_args()
        self.assertEqual(api_call(fakeargs), data)

    def test_api_call_range_5_to_100(self):
        with open('testdata5to100.txt', 'r') as filehandle:
            data = json.load(filehandle)
        with patch('argparse._sys.argv', ['get_posts.py','--start','5','--end', '100']):
            fakeargs = cmdline_args()
        self.assertEqual(api_call(fakeargs), data)    

if __name__ == "__main__":
    unittest.main()