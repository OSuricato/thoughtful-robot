"""
Package sorting module for the thoughtful robotic automation factory.

This module contains the logic for dispatching packages to the correct stack
based on their volume and mass characteristics.
"""


def sort(width, height, length, mass):
    """
    Sort packages into appropriate stacks based on dimensions and mass.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters  
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
        
    Returns:
        str: Stack name where the package should be dispatched:
             - "STANDARD": normal packages (not bulky or heavy)
             - "SPECIAL": packages that are either heavy or bulky
             - "REJECTED": packages that are both heavy and bulky
             
    Raises:
        ValueError: If any dimension or mass is negative
        TypeError: If any input is not a number
    """
    # Input validation
    _validate_inputs(width, height, length, mass)
    
    # Determine if package is bulky
    is_bulky = _is_package_bulky(width, height, length)
    
    # Determine if package is heavy
    is_heavy = _is_package_heavy(mass)
    
    # Apply sorting logic
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def _validate_inputs(width, height, length, mass):
    """
    Validate that all inputs are valid numbers and non-negative.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
        
    Raises:
        TypeError: If any input is not a number
        ValueError: If any input is negative
    """
    inputs = [
        ("width", width),
        ("height", height), 
        ("length", length),
        ("mass", mass)
    ]
    
    for name, value in inputs:
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"{name} cannot be negative, got {value}")


def _is_package_bulky(width, height, length):
    """
    Determine if a package is bulky based on volume or dimensions.
    
    A package is bulky if:
    - Volume (width * height * length) >= 1,000,000 cm³, OR
    - Any dimension >= 150 cm
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
        
    Returns:
        bool: True if package is bulky, False otherwise
    """
    VOLUME_THRESHOLD = 1_000_000  # cm³
    DIMENSION_THRESHOLD = 150     # cm
    
    volume = width * height * length
    
    if volume >= VOLUME_THRESHOLD:
        return True
        
    if width >= DIMENSION_THRESHOLD:
        return True
        
    if height >= DIMENSION_THRESHOLD:
        return True
        
    if length >= DIMENSION_THRESHOLD:
        return True
        
    return False


def _is_package_heavy(mass):
    """
    Determine if a package is heavy based on mass.
    
    A package is heavy if mass >= 20 kg.
    
    Args:
        mass (float): Package mass in kilograms
        
    Returns:
        bool: True if package is heavy, False otherwise
    """
    MASS_THRESHOLD = 20  # kg
    
    return mass >= MASS_THRESHOLD
