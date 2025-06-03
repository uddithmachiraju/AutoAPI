from setuptools import setup, find_packages

setup(
    name = "AutoAPI",
    version = "0.0.1",
    description = "A CLI Tool that turns your saved ML model into a working REST API",
    author = "M. Sanjay Uddith Raju", 
    author_email = "uddithmachiraju@gmail.com",
    packages = find_packages(
        where = "."
    ),
    entry_points={
        'console_scripts': [
            'autoapi=autoapi.cli:main'
        ]
    },
    install_requires = [
        "flask",
        "PyYAML"
    ]
)