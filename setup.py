import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter_notebooks",
    version="0.0.1",
    author="Filippo Squillace",
    author_email="squillace.filippo@gmail.com",
    description="Set of handy Jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsquillace/notebooks",
    packages=setuptools.find_packages(where="src", exclude="test"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
