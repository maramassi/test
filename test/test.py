#!/usr/bin/env python3
"""
Test module containing a test class.
"""

class Test:
    """
    A simple test class for demonstration purposes.
    """
    
    def __init__(self, name="Test"):
        """
        Initialize the Test class.
        
        Args:
            name (str): The name of the test instance
        """
        self.name = name
    
    def get_name(self):
        """
        Get the name of the test instance.
        
        Returns:
            str: The name of the test instance
        """
        return self.name
    
    def set_name(self, name):
        """
        Set the name of the test instance.
        
        Args:
            name (str): The new name for the test instance
        """
        self.name = name
    
    def run_test(self):
        """
        Run a simple test.
        
        Returns:
            bool: True if test passes, False otherwise
        """
        print(f"Running test: {self.name}")
        return True


if __name__ == "__main__":
    # Example usage
    test_instance = Test("MyTest")
    print(f"Test name: {test_instance.get_name()}")
    test_instance.run_test()