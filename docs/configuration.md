# ADRI Configuration Guide

This guide shows you how to adjust ADRI settings to customize behavior, thresholds, and integration with your workflows.

## Overview

ADRI provides flexible configuration options to adapt to your specific data quality requirements and operational needs.

## Configuration Files

### 1. Global Configuration
**Location**: `./ADRI/adri-config.yaml`

```yaml
# ADRI Global Configuration
adri:
  version: "2.0.0"
  
  # Protection behavior
  protection:
    default_min_score: 80
    default_failure_mode: "raise"  # raise, warn, continue
    verbose_protection: false
    auto_generate_standards: true
    
  # Performance settings
  performance:
    cache_duration_hours: 1
    data_sampling_limit: 1000
    parallel_assessment: true
    
  # Messaging and output
  messaging:
    verbose: false
    show_cli_commands: true
    include_documentation_links: true
    
  # Paths and directories
  paths:
    standards_dir: "./ADRI/dev/standards"
    assessments_dir: "./ADRI/dev/assessments"
    cache_dir: "./ADRI/dev/cache"
```

### 2. Function-Specific Configuration
**Location**: Alongside your Python files

```yaml
# customer_service_config.yaml
functions:
  customer_service_agent:
    min_score: 95
    dimensions:
      validity: 18
      completeness: 19
      consistency: 16
    on_failure: "raise"
    verbose: true
```

## Configuration Options Reference

### Protection Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `default_min_score` | 80 | Minimum quality score (0-100) |
| `default_failure_mode` | "raise" | How to handle failures: raise, warn, continue |
| `verbose_protection` | false | Show detailed protection messages |
| `auto_generate_standards` | true | Auto-create standards for new data |

### Performance Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `cache_duration_hours` | 1 | How long to cache assessment results |
| `data_sampling_limit` | 1000 | Max rows for standard generation |
| `parallel_assessment` | true | Run dimension assessments in parallel |

### Messaging Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `verbose` | false | Show detailed success/failure messages |
| `show_cli_commands` | true | Include CLI commands in messages |
| `include_documentation_links` | true | Show links to documentation |

## Common Configuration Scenarios

### 1. Development Environment

```yaml
# Development: Verbose, forgiving, fast iteration
adri:
  protection:
    default_min_score: 70
    default_failure_mode: "warn"
    verbose_protection: true
    auto_generate_standards: true
    
  messaging:
    verbose: true
    show_cli_commands: true
    
  performance:
    cache_duration_hours: 0  # No caching for fresh results
```

### 2. Production Environment

```yaml
# Production: Strict, reliable, optimized
adri:
  protection:
    default_min_score: 90
    default_failure_mode: "raise"
    verbose_protection: false
    auto_generate_standards: false  # Use pre-approved standards
    
  messaging:
    verbose: false
    show_cli_commands: false
    
  performance:
    cache_duration_hours: 24  # Long caching for performance
    parallel_assessment: true
```

### 3. CI/CD Pipeline

```yaml
# CI/CD: Fast, minimal output, strict
adri:
  protection:
    default_min_score: 85
    default_failure_mode: "raise"
    verbose_protection: false
    
  messaging:
    verbose: false
    show_cli_commands: false
    include_documentation_links: false
    
  performance:
    data_sampling_limit: 500  # Faster for CI
    cache_duration_hours: 0
```

## Dimension-Specific Configuration

### Setting Custom Thresholds

```yaml
# Fine-tune individual dimension requirements
dimensions:
  validity:
    min_score: 18      # Out of 20
    weight: 1.2        # Increase importance
    
  completeness:
    min_score: 19      # Strict completeness
    weight: 1.0
    
  consistency:
    min_score: 15      # More lenient
    weight: 0.8
    
  freshness:
    min_score: 16
    max_age_days: 30   # Data must be < 30 days old
    
  plausibility:
    min_score: 14
    outlier_threshold: 3.0  # Standard deviations
```

### Industry-Specific Presets

#### Financial Services
```yaml
# High accuracy, regulatory compliance
financial_preset:
  protection:
    default_min_score: 95
    
  dimensions:
    validity: 19       # Critical for financial data
    completeness: 20   # No missing required fields
    consistency: 18    # Consistent formats
    freshness: 17      # Recent data required
    plausibility: 16   # Reasonable values
```

#### Healthcare
```yaml
# Patient safety, privacy compliance
healthcare_preset:
  protection:
    default_min_score: 92
    
  dimensions:
    validity: 20       # Patient safety critical
    completeness: 19   # Complete medical records
    consistency: 17    # Consistent terminology
    freshness: 15      # Historical data acceptable
    plausibility: 18   # Medical value ranges
```

#### E-commerce
```yaml
# Customer experience, operational efficiency
ecommerce_preset:
  protection:
    default_min_score: 85
    
  dimensions:
    validity: 17       # Valid customer data
    completeness: 16   # Some optional fields OK
    consistency: 18    # Consistent product data
    freshness: 19      # Recent inventory data
    plausibility: 15   # Flexible value ranges
```

## Environment-Specific Configuration

### Using Environment Variables

```bash
# Override config with environment variables
export ADRI_MIN_SCORE=90
export ADRI_FAILURE_MODE=raise
export ADRI_VERBOSE=true
export ADRI_STANDARDS_DIR=/custom/path/standards
```

### Docker Configuration

```dockerfile
# Dockerfile
ENV ADRI_MIN_SCORE=85
ENV ADRI_FAILURE_MODE=raise
ENV ADRI_CACHE_DURATION=0

COPY adri-config.yaml /app/adri-config.yaml
```

### Kubernetes Configuration

```yaml
# ConfigMap for ADRI settings
apiVersion: v1
kind: ConfigMap
metadata:
  name: adri-config
data:
  adri-config.yaml: |
    adri:
      protection:
        default_min_score: 90
        default_failure_mode: "raise"
      performance:
        cache_duration_hours: 6
```

## Advanced Configuration

### Custom Scoring Algorithms

```yaml
# Override default scoring behavior
scoring:
  algorithm: "weighted_average"  # weighted_average, min_threshold, custom
  
  # Custom weights for dimensions
  dimension_weights:
    validity: 0.25
    completeness: 0.25
    consistency: 0.20
    freshness: 0.15
    plausibility: 0.15
    
  # Penalty for critical failures
  critical_failure_penalty: 20
```

### Integration Settings

```yaml
# Framework-specific settings
integrations:
  langchain:
    auto_protect_chains: true
    protect_retrievers: true
    
  crewai:
    protect_agent_inputs: true
    protect_tool_outputs: false
    
  custom:
    webhook_url: "https://your-monitoring.com/adri-alerts"
    alert_on_failure: true
```

## Configuration Validation

### Validate Your Configuration

```bash
# Check configuration syntax and values
adri validate-config

# Test configuration with sample data
adri test-config --data sample.csv

# Show effective configuration (with all defaults)
adri show-config --verbose
```

### Configuration Schema

ADRI validates your configuration against a schema:

```bash
# Download the latest schema
adri download-schema

# Validate against schema
adri validate-config --schema adri-config-schema.json
```

## Troubleshooting Configuration

### Common Issues

1. **Configuration Not Loading**
   ```bash
   # Check configuration file location
   adri show-config --debug
   
   # Verify file permissions
   ls -la adri-config.yaml
   ```

2. **Environment Variables Not Working**
   ```bash
   # Check environment variable names
   env | grep ADRI
   
   # Test with explicit config
   adri assess data.csv --config custom-config.yaml
   ```

3. **Performance Issues**
   ```yaml
   # Optimize for your use case
   performance:
     cache_duration_hours: 6    # Balance freshness vs speed
     data_sampling_limit: 2000  # Increase for better accuracy
     parallel_assessment: true  # Use all CPU cores
   ```

## Configuration Best Practices

### 1. Start with Defaults
- Use default configuration initially
- Adjust gradually based on your needs
- Document why you changed specific settings

### 2. Environment-Specific Configs
- Development: Verbose, forgiving
- Staging: Production-like, with debugging
- Production: Strict, optimized, minimal output

### 3. Version Control
- Store configuration files in version control
- Use different configs for different environments
- Document configuration changes

### 4. Monitor and Adjust
- Track protection success/failure rates
- Adjust thresholds based on real data patterns
- Review configuration regularly

## Next Steps

1. **Custom Rules**: Learn about [adding domain-specific rules](./custom-rules.md)
2. **CLI Reference**: Explore [CLI commands](../technical-tools/cli-reference/)
3. **Integration Guides**: See [framework integration examples](../agent-builders/framework-integration/)

---

*This documentation is part of the ADRI Standard project. For updates and contributions, see our [GitHub repository](https://github.com/your-org/adri-standard).*
