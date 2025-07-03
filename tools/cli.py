"""
Command-line interface for ADRI Standards.
"""

import click
import json
from typing import Dict, Any
from standards.core import load_standard, list_standards, validate_standard


@click.group()
@click.version_option(version="1.0.0", prog_name="adri-standards")
def main():
    """ADRI Standards - Command-line interface for managing ADRI standards."""
    pass


@main.command()
def list():
    """List all available standards."""
    standards = list_standards()
    
    if not standards:
        click.echo("No standards found.")
        return
    
    click.echo(f"Found {len(standards)} standards:\n")
    
    for standard in standards:
        click.echo(f"ID: {standard['id']}")
        click.echo(f"Name: {standard['name']}")
        click.echo(f"Version: {standard['version']}")
        if standard['description']:
            click.echo(f"Description: {standard['description']}")
        click.echo(f"File: {standard['file']}")
        click.echo("-" * 50)


@main.command()
@click.argument('standard_id')
@click.option('--format', 'output_format', default='yaml', 
              type=click.Choice(['yaml', 'json']), 
              help='Output format (yaml or json)')
def show(standard_id: str, output_format: str):
    """Show details of a specific standard."""
    try:
        standard = load_standard(standard_id)
        
        if output_format == 'json':
            click.echo(json.dumps(standard, indent=2))
        else:
            import yaml
            click.echo(yaml.dump(standard, default_flow_style=False))
            
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        click.get_current_context().exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        click.get_current_context().exit(1)


@main.command()
@click.argument('standard_file', type=click.Path(exists=True))
def validate(standard_file: str):
    """Validate a standard file."""
    try:
        import yaml
        
        with open(standard_file, 'r', encoding='utf-8') as f:
            standard = yaml.safe_load(f)
        
        if validate_standard(standard):
            click.echo(f"✅ Standard file '{standard_file}' is valid.")
        else:
            click.echo(f"❌ Standard file '{standard_file}' is invalid.")
            click.get_current_context().exit(1)
            
    except yaml.YAMLError as e:
        click.echo(f"❌ YAML error in '{standard_file}': {e}", err=True)
        click.get_current_context().exit(1)
    except Exception as e:
        click.echo(f"❌ Error validating '{standard_file}': {e}", err=True)
        click.get_current_context().exit(1)


@main.command()
@click.argument('standard_id')
def info(standard_id: str):
    """Show summary information about a standard."""
    try:
        standard = load_standard(standard_id)
        
        # Extract basic info
        std_info = standard.get('standards', {})
        requirements = standard.get('requirements', {})
        
        click.echo(f"Standard: {std_info.get('name', 'Unknown')}")
        click.echo(f"ID: {std_info.get('id', 'Unknown')}")
        click.echo(f"Version: {std_info.get('version', 'Unknown')}")
        click.echo(f"Authority: {std_info.get('authority', 'Unknown')}")
        
        if 'description' in std_info:
            click.echo(f"Description: {std_info['description']}")
        
        if 'overall_minimum' in requirements:
            click.echo(f"Overall Minimum Score: {requirements['overall_minimum']}")
        
        if 'dimension_requirements' in requirements:
            click.echo("\nDimension Requirements:")
            for dim, config in requirements['dimension_requirements'].items():
                min_score = config.get('minimum_score', 'Not specified')
                description = config.get('description', 'No description')
                click.echo(f"  {dim}: {min_score} - {description}")
        
        if 'field_requirements' in requirements:
            field_count = len(requirements['field_requirements'])
            click.echo(f"\nField Requirements: {field_count} fields defined")
            
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        click.get_current_context().exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        click.get_current_context().exit(1)


if __name__ == '__main__':
    main()
