import setuptools

with open("README.md", 'r') as readme:
    setuptools.setup(
        name = 'scihub',
        version = '1.0.2',
        author = "zaytoun",
        description = "Unofficial API for Sci-Hub.",
        long_description = readme.read(),
        long_description_content_type = "text/markdown",
        url = "https://github.com/LeMinaw/scihub.py",
        packages = setuptools.find_packages(),
        install_requires = [
            'beautifulsoup4',
            'requests',
            'retrying',
            'pysocks'
        ],
        classifiers = [
            'Programming Language :: Python :: 3',
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
    )
