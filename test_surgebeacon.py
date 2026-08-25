# test_surgebeacon.py
"""
Tests for SurgeBeacon module.
"""

import unittest
from surgebeacon import SurgeBeacon

class TestSurgeBeacon(unittest.TestCase):
    """Test cases for SurgeBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SurgeBeacon()
        self.assertIsInstance(instance, SurgeBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SurgeBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
