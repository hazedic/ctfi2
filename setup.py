from setuptools import setup

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name='ctfi2',
    version="1.0",
    package_dir={'':"src"},
    packages=["ctfi2"],
    scripts=['src/ctfi2/ctfi2'],
    author="George Wood",
    author_email="drpresq@gmail.com",
    description="ctfi2 - CTFd Interface 2",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https//github.com/drpresq/ctfi2",
    keywords="",
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)

"""
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
"""

