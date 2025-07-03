# Adding Custom Domain Rules to ADRI Standards

This guide shows you how to add domain-specific validation rules to your ADRI standards to ensure your data meets your business requirements.

## Overview

ADRI automatically generates standards with basic data quality rules, but you can enhance them with custom domain-specific rules that understand your business context.

## Quick Start

1. **Find your standard file**: `./ADRI/dev/standards/your_function_data_standard.yaml`
2. **Add custom rules**: Edit the `custom_rules` section
3. **Test your rules**: `adri validate-standard your_standard_name`
4. **Apply to data**: `adri assess <your-data> --standard your_standard_name`

## Adding Custom Rules

### 1. Email Domain Validation

```yaml
custom_rules:
  email_domain_whitelist:
    field: "email"
    rule_type: "domain_validation"
    allowed_domains: ["company.com", "partner.org"]
    error_message: "Email must be from approved domains"
```

### 2. Business Value Ranges

```yaml
custom_rules:
  account_balance_range:
    field: "account_balance"
    rule_type: "range_validation"
    min_value: 0
    max_value: 1000000
    error_message: "Account balance must be between $0 and $1M"
```

### 3. Required Field Combinations

```yaml
custom_rules:
  customer_identification:
    rule_type: "conditional_required"
    condition: "customer_type == 'premium'"
    required_fields: ["ssn", "tax_id"]
    error_message: "Premium customers must have SSN and Tax ID"
```

### 4. Date Range Validation

```yaml
custom_rules:
  transaction_date_range:
    field: "transaction_date"
    rule_type: "date_range"
    min_date: "2020-01-01"
    max_date: "today"
    error_message: "Transaction date must be within last 5 years"
```

### 5. Pattern Matching

```yaml
custom_rules:
  customer_id_format:
    field: "customer_id"
    rule_type: "regex_pattern"
    pattern: "^CUST[0-9]{6}$"
    error_message: "Customer ID must follow format CUST123456"
```

## Rule Types Reference

| Rule Type | Purpose | Example Use Case |
|-----------|---------|------------------|
| `domain_validation` | Validate email domains | Corporate email requirements |
| `range_validation` | Numeric range checks | Financial limits, age ranges |
| `conditional_required` | Context-dependent requirements | Premium vs basic customers |
| `date_range` | Date boundary validation | Recent transactions only |
| `regex_pattern` | Format validation | ID patterns, phone numbers |
| `lookup_validation` | Reference data checks | Valid country codes |
| `cross_field_validation` | Multi-field logic | Start date < End date |

## Advanced Examples

### Financial Services Rules

```yaml
custom_rules:
  # Risk assessment requirements
  high_value_transaction:
    rule_type: "conditional_required"
    condition: "amount > 10000"
    required_fields: ["risk_score", "approval_code"]
    
  # Regulatory compliance
  kyc_completeness:
    rule_type: "conditional_required"
    condition: "customer_type == 'institutional'"
    required_fields: ["lei_code", "regulatory_status"]
    
  # Currency validation
  currency_amount_consistency:
    rule_type: "cross_field_validation"
    fields: ["currency", "amount"]
    validation_logic: "currency_specific_amount_format"
```

### Healthcare Rules

```yaml
custom_rules:
  # Patient safety
  medication_dosage_safety:
    field: "dosage_mg"
    rule_type: "conditional_range"
    condition: "patient_age < 18"
    max_value: 500
    error_message: "Pediatric dosage cannot exceed 500mg"
    
  # Privacy compliance
  phi_data_handling:
    rule_type: "data_classification"
    sensitive_fields: ["ssn", "medical_record_number"]
    encryption_required: true
```

## Testing Your Custom Rules

### 1. Validate Standard Structure
```bash
adri validate-standard your_standard_name
```

### 2. Test Against Sample Data
```bash
adri assess sample_data.csv --standard your_standard_name --verbose
```

### 3. Debug Rule Failures
```bash
adri explain-failure --latest --verbose
```

## Best Practices

### 1. Start Simple
- Begin with basic range and pattern validations
- Add complexity gradually as you understand your data better

### 2. Use Descriptive Names
```yaml
# Good
customer_email_corporate_domain_validation:

# Avoid
rule_1:
```

### 3. Provide Clear Error Messages
```yaml
error_message: "Customer email must be from approved corporate domains (@company.com, @partner.org)"
```

### 4. Test Thoroughly
- Test with both valid and invalid data
- Verify error messages are helpful
- Check performance with large datasets

### 5. Document Business Logic
```yaml
# Document why the rule exists
business_justification: "Regulatory requirement for customer identification"
```

## Integration with ADRI Protection

Once you've added custom rules, they automatically work with ADRI protection:

```python
@adri_protected(data_param="customer_data", min_score=90)
def process_customer_data(customer_data):
    # Your custom rules are automatically enforced
    return analyze_customer_data(customer_data)
```

## Troubleshooting

### Common Issues

1. **Rule Not Triggering**
   - Check field names match exactly
   - Verify rule syntax in YAML
   - Test with `adri validate-standard`

2. **Performance Issues**
   - Use sampling for large datasets
   - Optimize regex patterns
   - Consider rule execution order

3. **False Positives**
   - Review business logic
   - Add exception handling
   - Adjust thresholds gradually

### Getting Help

- **View rule documentation**: `adri show-standard your_standard --verbose`
- **Test specific rules**: `adri test-rule your_standard rule_name`
- **Community support**: [ADRI GitHub Issues](https://github.com/your-org/adri-standard/issues)

## Next Steps

1. **Configuration Guide**: Learn about [adjusting ADRI settings](./configuration.md)
2. **Advanced Patterns**: Explore [reliability patterns](../agent-builders/reliability-patterns/)
3. **Framework Integration**: See [framework integration examples](../agent-builders/framework-integration/)

---

*This documentation is part of the ADRI Standard project. For updates and contributions, see our [GitHub repository](https://github.com/your-org/adri-standard).*
