from setuptools import setup, find_packages

setup(
    name="topsis-package",  # Replace with a unique name for your package
    version="1.0.0",        # Initial version
    author="Your Name",     # Your name
    author_email="your.email@example.com",  # Your email
    description="A Python implementation of the TOPSIS decision-making method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis-package",  # GitHub repo URL (optional)
    packages=find_packages(),  # Automatically finds and includes all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],  # Dependencies
)
