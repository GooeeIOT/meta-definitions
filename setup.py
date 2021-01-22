import setuptools


def long_description():
    with open("README.md", "r") as fr:
        return fr.read()


def requirements():
    with open("requirements.txt", "r") as fr:
        return fr.read()


setuptools.setup(
    name="meta-definitions",
    version="0.0.1",
    author="Gooee",
    description="Meta Definitions used in the Gooee Cloud",
    include_package_data=True,
    install_requires=requirements(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/GooeeIOT/meta-definitions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
