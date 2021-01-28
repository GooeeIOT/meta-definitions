import setuptools


def long_description():
    with open("README.md", "r", encoding="utf-8") as fr:
        return fr.read()


def requirements():
    with open("requirements.txt", "r") as fr:
        return fr.read()


setuptools.setup(
    name="meta-definitions",
    version="1.0.5",
    author="Gooee",
    description="Meta Definitions used in the Gooee Cloud",
    install_requires=requirements(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/GooeeIOT/meta-definitions",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent",],
    python_requires=">=3.6",
)
