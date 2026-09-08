from setuptools import Extension, setup, Command, find_packages

VERSION = '0.1'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='waveform_plugin',
    version=VERSION,
    description = 'A PyCBC plugin for loading self-built waveform',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Kanchan Soni',
    author_email='ksoni01@syr.edu',
    url='https://github.com/Kanchan-05/waveform_plugin',
    keywords=['gravitational waves', 'pycbc'],
    packages=find_packages(),
    python_requires='>=3.11',

    entry_points={
        "pycbc.waveform.td": [
        "nrsxs = waveform.waveform_plugin:gen_my_waveform", 
    ],
    },

    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],

    install_requires=[
        "pycbc",

    ]
)