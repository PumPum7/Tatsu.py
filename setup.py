from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='tatsu.py',
    version='1.1.0',
    description="An async python API Wrapper for the Tatsu API.",
    install_requires=[
        'ratelimit~=2.2.1',
        'httpx~=0.27.0'
    ],
    license='MIT License',
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url="https://github.com/PumPum7/Tatsu.py",
    author="Pum",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="api, tatsu, api wrapper",
    packages=["tatsu"],
    project_urls={
        "Tatsu": "https://tatsu.gg/",
        "Source": "https://github.com/PumPum7/Tatsu.py"
    }
)
