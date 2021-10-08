import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycreditsafe",
    version="0.0.3",
    author="Andrea Valente, Shantanu Lodh",
    author_email="andrea.valente@bottomline.com",
    description="A Python wrapper around the Creditsafe API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)