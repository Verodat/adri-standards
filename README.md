# ADRI Standards

**Agent Data Reliability Intelligence Standards** - The open standard for AI agent data quality validation.

[![PyPI version](https://badge.fury.io/py/adri-standards.svg)](https://badge.fury.io/py/adri-standards)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub stars](https://img.shields.io/github/stars/verodat/adri-standards.svg)](https://github.com/verodat/adri-standards/stargazers)

## 🎯 What is ADRI?

ADRI Standards defines the universal framework for protecting AI agents from dirty data. Whether you're building with LangChain, CrewAI, AutoGen, or any other framework, ADRI provides the standards and patterns to ensure your agents receive reliable, high-quality data.

## 🚀 Quick Start

```bash
pip install adri-standards
```

```python
from adri_standards import load_standard

# Load a pre-built standard
customer_standard = load_standard("customer_data_v1")

# Or create your own
my_standard = {
    "standards": {
        "id": "my-data-v1",
        "name": "My Data Quality Standard",
        "version": "1.0.0"
    },
    "requirements": {
        "overall_minimum": 80.0,
        "dimension_requirements": {
            "validity": {"minimum_score": 18.0},
            "completeness": {"minimum_score": 16.0}
        }
    }
}
```

## 🏗️ Framework Integration

ADRI Standards works with all major AI agent frameworks:

### LangChain
```python
from adri_validator import adri_protected

@adri_protected(data_param="customer_data")
def langchain_agent(customer_data):
    # Your LangChain code here
    return chain.run(customer_data)
```

### CrewAI
```python
@adri_protected(data_param="market_data", min_score=90)
def crewai_analysis(market_data):
    # Your CrewAI code here
    return crew.kickoff(market_data)
```

### AutoGen
```python
@adri_protected(data_param="conversation_data")
def autogen_conversation(conversation_data):
    # Your AutoGen code here
    return agents.initiate_chat(conversation_data)
```

## 📊 Standards Library

### Core Standards
- **Customer Data** - Personal information, contact details, preferences
- **Financial Data** - Transactions, balances, risk metrics
- **Market Data** - Prices, volumes, trends, indicators
- **Conversation Data** - Chat logs, sentiment, context

### Framework-Specific Standards
- **LangChain Patterns** - Document processing, retrieval chains
- **CrewAI Patterns** - Multi-agent workflows, task coordination
- **AutoGen Patterns** - Conversation flows, agent interactions

### Domain Standards
- **Healthcare** - Patient data, medical records, compliance
- **E-commerce** - Product catalogs, orders, customer behavior
- **Manufacturing** - IoT sensors, quality metrics, supply chain

## 🛠️ Creating Custom Standards

```yaml
standards:
  id: "my-custom-standard"
  name: "My Custom Data Standard"
  version: "1.0.0"
  authority: "My Organization"

requirements:
  overall_minimum: 85.0
  
  dimension_requirements:
    validity:
      minimum_score: 18.0
      description: "Data must be valid and well-formed"
    
    completeness:
      minimum_score: 16.0
      description: "Required fields must be present"
    
    consistency:
      minimum_score: 15.0
      description: "Data must be internally consistent"

  field_requirements:
    user_id:
      type: "string"
      nullable: false
      pattern: "^[A-Z]{3}[0-9]{6}$"
    
    email:
      type: "string"
      nullable: false
      pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
```

## 🌟 Why ADRI Standards?

### For Developers
- **Universal Protection** - One standard works across all frameworks
- **Pre-built Patterns** - 50+ ready-to-use validation standards
- **Community Driven** - Open source with active contribution
- **Production Ready** - Battle-tested in enterprise environments

### For Organizations
- **Risk Reduction** - Prevent agent failures from bad data
- **Compliance Ready** - Built-in patterns for regulatory requirements
- **Cost Savings** - Reduce debugging and incident response time
- **Quality Assurance** - Consistent data quality across all agents

### For the Ecosystem
- **Interoperability** - Standards work across vendors and frameworks
- **Innovation** - Focus on agent logic, not data validation
- **Best Practices** - Community-curated quality patterns
- **Future Proof** - Evolving standards for emerging use cases

## 📚 Documentation

- **[Getting Started](https://adri.verodat.com/getting-started)** - Quick setup and first validation
- **[Standards Reference](https://adri.verodat.com/standards)** - Complete standards catalog
- **[Framework Integration](https://adri.verodat.com/frameworks)** - Framework-specific guides
- **[Custom Standards](https://adri.verodat.com/custom)** - Creating your own standards
- **[API Reference](https://adri.verodat.com/api)** - Complete API documentation

## 🤝 Community

- **[GitHub Discussions](https://github.com/verodat/adri-standards/discussions)** - Ask questions, share ideas
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute standards
- **[Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines
- **[Discord](https://discord.gg/adri)** - Real-time community chat

## 🏢 Enterprise

Need enterprise features like custom validation rules, SLA support, or professional services?

- **[Verodat Platform](https://verodat.com/adri)** - Enterprise data quality platform
- **[Professional Services](https://verodat.com/services)** - Custom standards development
- **[Support](https://verodat.com/support)** - Enterprise support options

## 📈 Roadmap

### Q1 2025
- [ ] 100+ community standards
- [ ] Real-time validation APIs
- [ ] Advanced analytics integration

### Q2 2025
- [ ] Multi-language support (JavaScript, Java)
- [ ] Cloud-native deployment patterns
- [ ] Industry-specific standard packs

### Q3 2025
- [ ] AI-powered standard generation
- [ ] Automated compliance reporting
- [ ] Enterprise marketplace integration

## 🔗 Related Projects

- **[ADRI Validator](https://github.com/thinkveolvesolve/adri-validator)** - Python implementation (private)
- **[Verodat Platform](https://verodat.com)** - Enterprise data quality platform
- **[Agent Marketplace](https://marketplace.verodat.com)** - ADRI-compliant agent marketplace

## 📄 License

ADRI Standards is released under the [Apache 2.0 License](LICENSE).

## 🙏 Acknowledgments

ADRI Standards is built by the community, for the community. Special thanks to all contributors who help make AI agents more reliable.

---

**Ready to protect your agents?** [Get started with ADRI Standards](https://adri.verodat.com/getting-started) today.
