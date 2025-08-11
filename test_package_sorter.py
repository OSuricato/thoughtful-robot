"""
Comprehensive test suite for the package sorting module.

Tests cover correct sorting logic, edge cases, input validation,
and various combinations of package characteristics.
"""

import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """Test cases for the package sorting function."""
    
    def test_standard_packages(self):
        """Test packages that should go to STANDARD stack."""
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        
        # Medium package, still under thresholds
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        
        # Just under all thresholds (volume: 99³ = 970,299 < 1,000,000)
        self.assertEqual(sort(99, 99, 99, 19.9), "STANDARD")
        
        # Zero dimensions and mass (edge case)
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        
        # Very small package
        self.assertEqual(sort(1, 1, 1, 0.1), "STANDARD")
    
    def test_heavy_packages_special_stack(self):
        """Test packages that are heavy but not bulky -> SPECIAL stack."""
        # Exactly at mass threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        
        # Heavy but small dimensions
        self.assertEqual(sort(5, 5, 5, 25), "SPECIAL")
        
        # Very heavy but tiny
        self.assertEqual(sort(1, 1, 1, 100), "SPECIAL")
        
        # Just over mass threshold
        self.assertEqual(sort(50, 50, 50, 20.1), "SPECIAL")
    
    def test_bulky_by_volume_special_stack(self):
        """Test packages that are bulky by volume but not heavy -> SPECIAL stack."""
        # Exactly at volume threshold (100 x 100 x 100 = 1,000,000)
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        # Over volume threshold
        self.assertEqual(sort(101, 101, 101, 5), "SPECIAL")
        
        # Large volume, light weight
        self.assertEqual(sort(200, 200, 25, 1), "SPECIAL")
    
    def test_bulky_by_dimension_special_stack(self):
        """Test packages that are bulky by dimension but not heavy -> SPECIAL stack."""
        # Exactly at dimension threshold
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")
        
        # Over dimension threshold
        self.assertEqual(sort(151, 10, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 200, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 300, 5), "SPECIAL")
        
        # Multiple dimensions over threshold
        self.assertEqual(sort(150, 150, 10, 5), "SPECIAL")
        self.assertEqual(sort(200, 200, 200, 10), "SPECIAL")
    
    def test_rejected_packages(self):
        """Test packages that are both heavy and bulky -> REJECTED stack."""
        # Heavy and bulky by volume
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        
        # Heavy and bulky by dimension
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 150, 10, 25), "REJECTED")
        self.assertEqual(sort(10, 10, 150, 30), "REJECTED")
        
        # Very heavy and very bulky
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
        
        # Exactly at both thresholds
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
    
    def test_boundary_conditions(self):
        """Test edge cases around threshold boundaries."""
        # Just under volume threshold
        volume_just_under = 99.9999
        self.assertEqual(sort(volume_just_under, 100, 100, 19.9), "STANDARD")
        
        # Just under dimension threshold
        self.assertEqual(sort(149.9999, 10, 10, 19.9), "STANDARD")
        
        # Just under mass threshold
        self.assertEqual(sort(10, 10, 10, 19.9999), "STANDARD")
        
        # Exactly at thresholds
        self.assertEqual(sort(100, 100, 100, 19.9999), "SPECIAL")  # Bulky by volume
        self.assertEqual(sort(150, 10, 10, 19.9999), "SPECIAL")    # Bulky by dimension
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")          # Heavy
    
    def test_input_validation_type_errors(self):
        """Test that invalid input types raise TypeError."""
        with self.assertRaises(TypeError):
            sort("10", 10, 10, 10)  # String width
            
        with self.assertRaises(TypeError):
            sort(10, "10", 10, 10)  # String height
            
        with self.assertRaises(TypeError):
            sort(10, 10, "10", 10)  # String length
            
        with self.assertRaises(TypeError):
            sort(10, 10, 10, "10")  # String mass
            
        with self.assertRaises(TypeError):
            sort(None, 10, 10, 10)  # None value
            
        with self.assertRaises(TypeError):
            sort(10, 10, 10, [20])  # List instead of number
    
    def test_input_validation_negative_values(self):
        """Test that negative values raise ValueError."""
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)  # Negative width
            
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)  # Negative height
            
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 10)  # Negative length
            
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)  # Negative mass
            
        with self.assertRaises(ValueError):
            sort(-10, -10, -10, -10)  # All negative
    
    def test_float_inputs(self):
        """Test that float inputs work correctly."""
        # Float inputs that result in STANDARD
        self.assertEqual(sort(10.5, 10.5, 10.5, 5.5), "STANDARD")
        
        # Float inputs that result in SPECIAL (heavy)
        self.assertEqual(sort(10.1, 10.1, 10.1, 20.1), "SPECIAL")
        
        # Float inputs that result in SPECIAL (bulky by dimension)
        self.assertEqual(sort(150.1, 10.1, 10.1, 5.1), "SPECIAL")
        
        # Float inputs that result in REJECTED
        self.assertEqual(sort(150.1, 10.1, 10.1, 20.1), "REJECTED")
    
    def test_large_numbers(self):
        """Test handling of very large numbers."""
        # Very large dimensions
        self.assertEqual(sort(1000, 1000, 1000, 5), "SPECIAL")
        
        # Very large mass
        self.assertEqual(sort(10, 10, 10, 1000), "SPECIAL")
        
        # Both very large
        self.assertEqual(sort(1000, 1000, 1000, 1000), "REJECTED")
    
    def test_precision_edge_cases(self):
        """Test floating point precision edge cases."""
        # Very close to thresholds
        self.assertEqual(sort(149.99999999, 10, 10, 19.99999999), "STANDARD")
        self.assertEqual(sort(150.00000001, 10, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 20.00000001), "SPECIAL")


class TestPackageSorterIntegration(unittest.TestCase):
    """Integration tests for realistic package scenarios."""
    
    def test_realistic_package_scenarios(self):
        """Test with realistic package dimensions and masses."""
        # Small electronics package
        self.assertEqual(sort(20, 15, 10, 0.5), "STANDARD")
        
        # Book package
        self.assertEqual(sort(25, 20, 3, 1.2), "STANDARD")
        
        # Large TV package (bulky by dimension)
        self.assertEqual(sort(160, 90, 15, 15), "SPECIAL")
        
        # Heavy machinery part (heavy but not bulky)
        self.assertEqual(sort(30, 30, 30, 25), "SPECIAL")
        
        # Industrial equipment (both heavy and bulky)
        self.assertEqual(sort(200, 150, 100, 50), "REJECTED")
        
        # Furniture package (bulky by volume)
        self.assertEqual(sort(120, 80, 120, 18), "SPECIAL")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
