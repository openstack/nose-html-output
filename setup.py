import htmloutput.htmloutput
import setuptools

setuptools.setup(
    name="nosehtmloutput",
    version=htmloutput.htmloutput.__version__,
    author='Hewlett-Packard Development Company, L.P.',
    description="Nose plugin to produce test results in html.",
    license="Apache License, Version 2.0",
    url="https://github.com/cboylan/nose-html-output",
    setup_requires=['nose'],
    install_requires=['nose'],
    classifiers=[
        "Environment :: Console",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    entry_points = {
        'nose.plugins.0.10': [
            'html-output = htmloutput.htmloutput:HtmlOutput'
        ]
    }
)
