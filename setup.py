from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pca-arun-s",
    version="0.0.1",
    author="ARUN S",
    author_email="a2r0u0n2@gmail.com",
    description="A Package to Lower the dimentions of the dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ARUN-S01/pca",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)