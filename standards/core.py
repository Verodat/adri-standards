"""
Core functionality for ADRI Standards.

This module provides the main interface for loading, listing, and validating ADRI standards.
"""

import os
import yaml
import glob
from typing import Dict, List, Any, Optional
from pathlib import Path

# Get the directory where standards are stored
STANDARDS_DIR = Path(__file__).parent / "core"


def load_standard(standard_id: str) -> Dict[str, Any]:
    """
    Load a standard by its ID.
    
    Args:
        standard_id: The ID of the standard to load
        
    Returns:
        Dictionary containing the standard definition
        
    Raises:
        FileNotFoundError: If the standard file is not found
        ValueError: If the standard file is invalid
    """
    # First, try to find by searching through all YAML files for matching ID
    for yaml_file in STANDARDS_DIR.glob("*.yaml"):
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                standard = yaml.safe_load(f)
            
            # Check if this standard has the matching ID
            if 'standards' in standard and standard['standards'].get('id') == standard_id:
                return standard
                
        except yaml.YAMLError:
            # Skip invalid YAML files
            continue
    
    # If not found by ID, try filename pattern matching as fallback
    pattern = f"*{standard_id}*.yaml"
    matches = list(STANDARDS_DIR.glob(pattern))
    
    if matches:
        try:
            with open(matches[0], 'r', encoding='utf-8') as f:
                standard = yaml.safe_load(f)
            return standard
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in standard file '{matches[0]}': {e}")
    
    raise FileNotFoundError(f"Standard '{standard_id}' not found")


def list_standards() -> List[Dict[str, str]]:
    """
    List all available standards.
    
    Returns:
        List of dictionaries containing standard metadata
    """
    standards = []
    
    for yaml_file in STANDARDS_DIR.glob("*.yaml"):
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                standard = yaml.safe_load(f)
            
            if 'standards' in standard:
                standards.append({
                    'id': standard['standards'].get('id', yaml_file.stem),
                    'name': standard['standards'].get('name', 'Unknown'),
                    'version': standard['standards'].get('version', '1.0.0'),
                    'description': standard['standards'].get('description', ''),
                    'file': str(yaml_file.name)
                })
        except (yaml.YAMLError, KeyError):
            # Skip invalid files
            continue
    
    return sorted(standards, key=lambda x: x['id'])


def validate_standard(standard: Dict[str, Any]) -> bool:
    """
    Validate that a standard has the required structure.
    
    Args:
        standard: The standard dictionary to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # Check required top-level keys
        if 'standards' not in standard:
            return False
        
        standards_section = standard['standards']
        required_fields = ['id', 'name', 'version']
        
        for field in required_fields:
            if field not in standards_section:
                return False
        
        # Check requirements section if present
        if 'requirements' in standard:
            requirements = standard['requirements']
            
            # Check for overall_minimum if present
            if 'overall_minimum' in requirements:
                if not isinstance(requirements['overall_minimum'], (int, float)):
                    return False
            
            # Check dimension_requirements if present
            if 'dimension_requirements' in requirements:
                dimensions = requirements['dimension_requirements']
                if not isinstance(dimensions, dict):
                    return False
                
                for dim_name, dim_config in dimensions.items():
                    if not isinstance(dim_config, dict):
                        return False
                    if 'minimum_score' in dim_config:
                        if not isinstance(dim_config['minimum_score'], (int, float)):
                            return False
        
        return True
        
    except (KeyError, TypeError):
        return False


def get_standard_path(standard_id: str) -> Optional[Path]:
    """
    Get the file path for a standard.
    
    Args:
        standard_id: The ID of the standard
        
    Returns:
        Path to the standard file, or None if not found
    """
    pattern = f"*{standard_id}*.yaml"
    matches = list(STANDARDS_DIR.glob(pattern))
    
    if matches:
        return matches[0]
    return None
