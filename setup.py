from setuptools import setup, find_packages

setup(
    name="keerthan-library",  # Replace with your library name
    version="0.1.1",
    author="keerthan",
    author_email="keerthankeerthi32@gmail.com",
    description="A sample Python library for demonstration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/keerthan156/my-library",  # Replace with your URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
