"""
Main entry point for the thoughtful_robot project.

This module demonstrates the robotic arm package sorting functionality
for the thoughtful robotic automation factory.
"""

from package_sorter import sort


def main():
    """Main function demonstrating package sorting functionality."""
    print("🤖 Thoughtful Robot - Package Sorting System")
    print("=" * 50)
    
    # Demo packages with different characteristics
    demo_packages = [
        {"name": "Small Electronics", "width": 20, "height": 15, "length": 10, "mass": 0.5},
        {"name": "Heavy Tool", "width": 30, "height": 20, "length": 15, "mass": 25},
        {"name": "Large TV", "width": 160, "height": 90, "length": 15, "mass": 15},
        {"name": "Industrial Equipment", "width": 200, "height": 150, "length": 100, "mass": 50},
        {"name": "Standard Book", "width": 25, "height": 20, "length": 3, "mass": 1.2},
    ]
    
    print("\nProcessing packages...")
    print("-" * 50)
    
    for package in demo_packages:
        stack = sort(package["width"], package["height"], package["length"], package["mass"])
        
        print(f"📦 {package['name']}")
        print(f"   Dimensions: {package['width']}×{package['height']}×{package['length']} cm")
        print(f"   Mass: {package['mass']} kg")
        print(f"   → Dispatched to: {stack} stack")
        print()
    
    print("✅ Package sorting demonstration complete!")


if __name__ == "__main__":
    main()
