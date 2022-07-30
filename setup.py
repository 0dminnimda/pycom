from pathlib import Path

from setuptools import setup


setup(
    name='pycom.py',
    version='1.0.0',
    install_requires=Path('requirements.txt').read_text().split("\n"),
    entry_points={
        'console_scripts': [
            'pycom=src.pycom.pycom:main'
        ]
    }
)
