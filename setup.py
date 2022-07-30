from setuptools import setup
from pathlib import Path


setup(
    name='pycom.py',
    version='1.0.0',
    extras_require={
        "test": Path("test-requirements.txt").read_text(),
    },
    entry_points={
        'console_scripts': [
            'pycom=src.pycom.pycom:main'
        ]
    }
)
