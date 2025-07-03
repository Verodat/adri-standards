"""
YAML standards handling for ADRI V2.

This module provides functionality for loading and working with YAML-based data quality standards.
"""

from typing import Dict, Any


class YAMLStandards:
    """Represents a YAML-based data quality standard."""
    
    def __init__(self, yaml_content: Dict[str, Any]):
        """
        Initialize YAML standards from parsed YAML content.
        
        Args:
            yaml_content: Dictionary containing parsed YAML standard
        """
        self.yaml_content = yaml_content
        
        # Extract metadata
        standards_section = yaml_content.get('standards', {})
        self.standards_id = standards_section.get('id', 'unknown-standard')
        self.standards_name = standards_section.get('name', 'Unknown Standard')
        self.standards_version = standards_section.get('version', '1.0.0')
        self.authority = standards_section.get('authority', 'Unknown Authority')
        
        # Extract requirements
        self.requirements = yaml_content.get('requirements', {})
    
    def get_overall_minimum(self) -> float:
        """Get the overall minimum score requirement."""
        return self.requirements.get('overall_minimum', 75.0)
    
    def get_dimension_requirements(self) -> Dict[str, Any]:
        """Get dimension-specific requirements."""
        return self.requirements.get('dimension_requirements', {})
    
    def get_field_requirements(self) -> Dict[str, Any]:
        """Get field-specific requirements."""
        return self.requirements.get('field_requirements', {})
    
    def __str__(self) -> str:
        """String representation of the standard."""
        return f"{self.standards_name} v{self.standards_version} ({self.authority})"
