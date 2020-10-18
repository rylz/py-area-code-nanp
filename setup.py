import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-area-code-nanp",
    version="1.0",
    author="Riley Patterson",
    author_email="rileypatterson@gmail.com",
    description="Information about phone area codes in the North American Numbering Plan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rylz/py-area-code-nanp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
