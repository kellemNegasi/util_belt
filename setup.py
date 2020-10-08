import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="util_belt", # Replace with your own username
    version="0.0.1",
    author="kellem negasi",
    author_email="kellemnegasi@gmail.com",
    description="A package of differnt utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kellemNegasi/util_belt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)