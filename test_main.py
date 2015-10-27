#!/usr/bin/env python3

#Unit test for Estimate-time-downloader

import unittest
import main

class Test_main(unittest.TestCase):

    def setUp(self):
        pass

    def test_download_time(self):
       self.assertEqual(main.download_time(1, 'GB', 2, 'Mb'), '1 hour, 8 minutes, 16.0 seconds', 'Download_time fails')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

