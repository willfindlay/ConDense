from setuptools import setup

name = 'condense'

description = """
A webscraper for top academic conferences
"""

version = '0.0.1'
author = 'William Findlay'
author_email = 'will@ccsl.carleton.ca'
git = 'https://github.com/willfindlay/ConDense'

requirements = ['click', 'beautifulsoup4', 'requests', 'pandas']

entry_points = """
[console_scripts]
condense=condense.cli:condense
"""

setup(
    name=name,
    version=version,
    description=description.strip('\n'),
    author=author,
    author_email=author_email,
    url=git,
    packages=[name],
    install_requires=requirements,
    entry_points=entry_points,
    include_package_data=True,
)
