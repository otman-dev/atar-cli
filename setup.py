from setuptools import setup, find_packages

setup(
    name="atar",
    version="1.0.0",
    description="A CLI tool for AI tasks such as dataset handling, training, and validation.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/atar",  # Replace with your GitHub repo URL
    packages=find_packages(where=".", exclude=["tests*"]),
    install_requires=[
        # Add any dependencies here
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "ultralytics>=8.0.0",  # YOLO and related tools
        "roboflow>=0.2.24",  # Roboflow Python API
        "supervision>=0.1.0",  # Supervision tools for vision tasks
        # Other required libraries
    ],
    entry_points={
        "console_scripts": [
            "atar-cli=atar.cli:main",  # Command to invoke your CLI
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
