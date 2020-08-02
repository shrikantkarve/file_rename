import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file_rename-shrikantkarve",
    version="0.0.1",
    author="Shrikant Karve",
    author_email="shrikant.karve@gmail.com",
    description="A simple file rename tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/file_rename",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)