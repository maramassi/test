#!/usr/bin/env python3
"""
Circle Parameter Calculator

This module provides functions to calculate the perimeter (circumference) of a circle.
The perimeter of a circle is also known as its circumference.
"""

import math


def calculate_perimeter_from_radius(radius):
    """
    Calculate the perimeter of a circle using its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The perimeter (circumference) of the circle
        
    Raises:
        ValueError: If radius is negative or zero
    """
    if radius <= 0:
        raise ValueError("Radius must be positive")
    
    return 2 * math.pi * radius


def calculate_perimeter_from_diameter(diameter):
    """
    Calculate the perimeter of a circle using its diameter.
    
    Args:
        diameter (float): The diameter of the circle
        
    Returns:
        float: The perimeter (circumference) of the circle
        
    Raises:
        ValueError: If diameter is negative or zero
    """
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    
    return math.pi * diameter


def calculate_perimeter_from_area(area):
    """
    Calculate the perimeter of a circle using its area.
    
    Args:
        area (float): The area of the circle
        
    Returns:
        float: The perimeter (circumference) of the circle
        
    Raises:
        ValueError: If area is negative or zero
    """
    if area <= 0:
        raise ValueError("Area must be positive")
    
    radius = math.sqrt(area / math.pi)
    return 2 * math.pi * radius


def main():
    """Main function to demonstrate the circle perimeter calculations."""
    print("Circle Parameter Calculator")
    print("=" * 30)
    
    # Example 1: Calculate perimeter from radius
    radius = 5.0
    perimeter = calculate_perimeter_from_radius(radius)
    print(f"Circle with radius {radius}:")
    print(f"  Perimeter = {perimeter:.2f} units")
    print()
    
    # Example 2: Calculate perimeter from diameter
    diameter = 10.0
    perimeter = calculate_perimeter_from_diameter(diameter)
    print(f"Circle with diameter {diameter}:")
    print(f"  Perimeter = {perimeter:.2f} units")
    print()
    
    # Example 3: Calculate perimeter from area
    area = 78.54  # Approximately π * 5²
    perimeter = calculate_perimeter_from_area(area)
    print(f"Circle with area {area}:")
    print(f"  Perimeter = {perimeter:.2f} units")
    print()
    
    # Example 4: Interactive calculation
    try:
        user_radius = float(input("Enter a radius to calculate perimeter: "))
        user_perimeter = calculate_perimeter_from_radius(user_radius)
        print(f"Perimeter = {user_perimeter:.2f} units")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()