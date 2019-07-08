import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tessitura",
    version="0.0.3",
    author="Micah Walter",
    author_email="micah@micahwalter.com",
    description="Tools for talking to the Tessitura API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/micahwalter/tessitura-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ]
)
