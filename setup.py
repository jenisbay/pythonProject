from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Example Basic Description"
LONG_DESCRIPTION = "Example Basic Description Long"

setup(
    name="hi",
    version=VERSION,
    author="Jenis Qidirbaev",
    author_email="jenisdev@gmail.com",
    url="https://github.com/jenisbay/pythonProject",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "selenium==4.15.2",
        "dependency-injector==4.41.0",
        "Appium-Python-Client==3.1.0"
    ],
    ext_package={
        "dev": ["twine>=4.0.2"]
    },
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: QA Automation Engineers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
