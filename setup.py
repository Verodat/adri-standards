"""
ADRI Standards - Agent Data Reliability Intelligence Standards

The open standard for AI agent data quality validation.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from version file
version = "1.0.0"

setup(
    name="adri-standards",
    version=version,
    author="Verodat",
    author_email="standards@verodat.com",
    description="Agent Data Reliability Intelligence Standards - Open standards for AI agent data quality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/verodat/adri-standards",
    project_urls={
        "Documentation": "https://adri.verodat.com",
        "Source": "https://github.com/verodat/adri-standards",
        "Tracker": "https://github.com/verodat/adri-standards/issues",
        "Community": "https://github.com/verodat/adri-standards/discussions",
        "Enterprise": "https://verodat.com/adri",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0",
        "jsonschema>=4.0",
        "packaging>=21.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=5.0",
            "mypy>=1.0",
        ],
        "docs": [
            "mkdocs>=1.4",
            "mkdocs-material>=8.0",
            "mkdocs-mermaid2-plugin>=0.6",
        ],
    },
    include_package_data=True,
    package_data={
        "standards": ["**/*.yaml", "**/*.yml"],
        "docs": ["**/*.md"],
        "examples": ["**/*.py", "**/*.yaml"],
    },
    entry_points={
        "console_scripts": [
            "adri-standards=tools.cli:main",
        ],
    },
    keywords=[
        "ai", "agents", "data-quality", "validation", "standards",
        "langchain", "crewai", "autogen", "reliability", "adri"
    ],
    license="Apache-2.0",
    zip_safe=False,
)
