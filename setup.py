from setuptools import find_packages, setup

setup(
    name="mkdocs-author-plugin",
    version="0.1.1",
    description="Add manually defined authors to MkDocs pages.",
    author="Joe Starr",
    author_email="joe@joe-starr.com",
    url="https://github.com/joecstarr/mkdocs-author-plugin",
    packages=find_packages(),
    install_requires=["mkdocs>=1.6.1", "pyyaml"],
    python_requires=">=3.10,<3.13",
    entry_points={
        "mkdocs.plugins": [
            "authors = mkdocs_author_plugin.plugin:AuthorsPlugin",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
