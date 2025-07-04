# ADRI Validator Releases

This document tracks all releases of the ADRI Validator package. The ADRI Validator provides the implementation layer for ADRI Standards, including decorators, CLI tools, and validation engines.

## Release History

| Package Name | Release Type | Version | Release Date | Latest | Description |
|--------------|--------------|---------|--------------|--------|-------------|
| adri-validator | Beta | 0.1.0 | 2025-07-04 | ✅ | • Production-ready CI/CD pipeline<br>• 91% test coverage<br>• Automated version tracking system |
| adri-validator | Beta | 0.1.0 | 2025-01-07 |  | • Production-ready CI/CD pipeline<br>• 91% test coverage with comprehensive test suite<br>• @adri_protected decorator with variants<br>• Complete CLI workflow (setup, assess, generate)<br>• Data quality assessment engine<br>• Configuration management system<br>• Analysis tools (profiler, generator)<br>• Full integration with adri-standards |

## Installation

### Latest Release
```bash
pip install adri==0.1.0
```

### Latest (Auto-detect version)
```bash
pip install adri
```

### With Standards Dependency
```bash
pip install adri-standards adri
```

### Development Version
```bash
pip install adri[dev]
```

## Quick Start

```python
from adri.decorators.guard import adri_protected

@adri_protected(data_param="customer_data")
def process_customers(customer_data):
    # Your processing logic here
    return processed_data
```

## Documentation

- **[ADRI Validator README](https://github.com/thinkveolvesolve/adri-validator/blob/main/README.md)** - Complete package documentation
- **[ADRI Standards](https://github.com/thinkveolvesolve/adri-standards)** - Standards library and examples
- **[Getting Started Guide](https://adri.verodat.com/getting-started)** - Quick setup tutorial

## Release Notes

### v1.0.0 (2025-07-03) - Initial Stable Release

**New Features:**
- **@adri_protected Decorator**: Core protection decorator with multiple variants
  - `@adri_protected` - Standard protection
  - `@adri_strict` - High security validation
  - `@adri_permissive` - Development-friendly mode
  - `@adri_financial` - Financial data specific protection
- **Complete CLI Workflow**: 
  - `adri setup` - Project initialization
  - `adri assess` - Data quality assessment
  - `adri generate-standard` - Standard generation from data
  - `adri validate-standard` - Standard validation
  - `adri list-standards` - Available standards listing
- **Data Quality Assessment Engine**: 5-dimension scoring system
- **Configuration Management**: Environment-specific configurations (dev/prod)
- **Analysis Tools**: Data profiler and standard generator
- **Full Integration**: Seamless integration with adri-standards package

**Technical Details:**
- Python 3.8+ support
- Comprehensive test coverage (100% success rate)
- Production-ready error handling
- Performance optimized
- Cross-platform compatibility

**Dependencies:**
- adri-standards >= 1.0.0
- pandas >= 1.3.0
- pyyaml >= 6.0
- click >= 8.0

---

*This file is automatically maintained by the ADRI Validator publishing process.*
