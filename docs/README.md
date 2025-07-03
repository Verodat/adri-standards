# ADRI Documentation

**Documentation for ADRI - Stop Your AI Agents Breaking on Bad Data**

## Overview

ADRI protects your AI agents from bad data with a simple decorator approach. Add one line to your existing agent code and ADRI automatically checks data quality before your agent processes it.

## Documentation

### Quick Reference
- **[Custom Rules](custom-rules.md)** - Add domain-specific validation rules to your standards
- **[Configuration](configuration.md)** - Customize ADRI behavior, thresholds, and settings

### Getting Started
1. **Install**: `pip install adri`
2. **Protect**: Add `@adri_protected(data_param="your_data")` to your agent function
3. **Run**: Your agent is now protected from bad data

## Core Concepts

### The Decorator Approach
```python
from adri.decorators.guard import adri_protected

@adri_protected(data_param="customer_data")
def customer_service_agent(customer_data):
    # Your existing agent code - unchanged!
    return process_customer_inquiry(customer_data)
```

### How It Works
1. **First Run**: ADRI creates a quality standard from your good data
2. **Subsequent Runs**: ADRI checks new data against this standard
3. **Protection**: Only good quality data reaches your agent

### What You Get
- ✅ **Automatic Protection** - No code changes to your agent logic
- ✅ **Clear Error Messages** - Actionable guidance when data fails
- ✅ **CLI Tools** - Manage standards and view assessment history
- ✅ **Framework Agnostic** - Works with LangChain, CrewAI, any Python function

## Configuration Options

### Basic Configuration
```python
@adri_protected(
    data_param="customer_data",    # Which parameter contains the data
    min_score=85,                  # Minimum quality score (default: 80)
    verbose=True,                  # Show detailed messages
    on_failure="raise"             # What to do on failure: raise, warn, continue
)
```

### Advanced Configuration
```python
@adri_protected(
    data_param="financial_data",
    standard_name="financial_risk_standard",  # Custom standard name
    dimensions={                               # Specific dimension requirements
        "validity": 18,
        "completeness": 19
    }
)
```

## CLI Tools

ADRI includes powerful command-line tools:

```bash
# List recent assessments
adri list-assessments --recent 5

# Export assessment report
adri export-report --latest --format csv

# Show standard details
adri show-standard your_standard_name --verbose

# List all standards
adri list-standards
```

## Framework Integration

### LangChain
```python
from langchain import LLMChain
from adri.decorators.guard import adri_protected

@adri_protected(data_param="customer_data")
def customer_service_agent(customer_data):
    prompt = "Analyze this customer inquiry: {inquiry}"
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(customer_data)
```

### CrewAI
```python
from crewai import Crew, Agent, Task
from adri.decorators.guard import adri_protected

@adri_protected(data_param="market_data")
def market_analysis_crew(market_data):
    analyst = Agent(role="Market Analyst", goal="Analyze trends")
    task = Task(description="Analyze market data", agent=analyst)
    crew = Crew(agents=[analyst], tasks=[task])
    return crew.kickoff(market_data)
```

### Any Python Function
```python
@adri_protected(data_param="documents")
def document_analyzer(documents):
    return analyze_documents(documents)
```

## Examples

See the [examples directory](../examples/) for working examples:
- **Basic decorator usage** - All decorator features and options
- **LangChain integration** - Real LangChain agent protection
- **CrewAI integration** - Real CrewAI workflow protection

## Troubleshooting

### Common Issues

**Q: My agent function isn't being protected**
A: Make sure the `data_param` matches the actual parameter name in your function.

**Q: I'm getting "Standard not found" errors**
A: ADRI auto-generates standards on first run. Make sure your first run uses good quality data.

**Q: Protection is too strict/lenient**
A: Adjust the `min_score` parameter or see [Configuration](configuration.md) for detailed settings.

**Q: I want to see what's happening**
A: Set `verbose=True` in your decorator for detailed logging.

### Getting Help

- **View assessment details**: `adri list-assessments --recent 1 --verbose`
- **Check standard requirements**: `adri show-standard your_standard_name`
- **Test data quality**: `adri assess your_data.csv --standard your_standard_name`

## What ADRI Does vs Doesn't Do

### ✅ What ADRI Does
- **Quality Gate** - Blocks bad data before it reaches your agents
- **Automatic Standards** - Creates quality standards from your good data
- **Clear Feedback** - Provides actionable error messages
- **CLI Tools** - Comprehensive command-line interface
- **Framework Support** - Works with any Python function or framework

### ❌ What ADRI Doesn't Do
- **Data Cleaning** - ADRI identifies issues but doesn't fix your data
- **Agent Logic** - Your agent code stays exactly the same
- **Data Storage** - ADRI doesn't store or modify your data

**ADRI is a quality gate, not a data processor.**

---

**One line. Any framework. Reliable agents.**
