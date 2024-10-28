from setuptools import setup, find_packages

setup(
    name="xenon-hash",
    version="0.1.0",
    package_dir={"": "src"},  # Tambah ini
    packages=find_packages(where="src"),  # Ubah ini
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A fast and efficient cryptographic hashing algorithm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/xenon-hash",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
