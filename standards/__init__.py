"""
ADRI Standards Package

This package contains the core standards definitions for ADRI (Agent Data Reliability Intelligence).
"""

__version__ = "1.0.0"

from .core import load_standard, list_standards, validate_standard

__all__ = [
    "load_standard",
    "list_standards", 
    "validate_standard",
    "__version__"
]
