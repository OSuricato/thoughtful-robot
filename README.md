# Thoughtful Robot - Package Sorting System

A robotic automation factory package sorting system that dispatches packages to the correct stack based on their volume and mass characteristics. Made by Victor Barbosa for Thoughtful AI.

## Quick Start

1. Run the demo: `python main.py`
2. Run tests: `python test_package_sorter.py`

## Business Rules

### Package Classification

- **Bulky**: Volume (width × height × length) ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg

### Stack Assignment

- **STANDARD**: Normal packages (neither bulky nor heavy)
- **SPECIAL**: Packages that are either heavy OR bulky (but not both)
- **REJECTED**: Packages that are both heavy AND bulky

## Installation

```bash
pip install -r requirements.txt
```
