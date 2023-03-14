from setuptools import setup, find_packages
from os import path

# Abre o arquivo README.md para ler o conteúdo
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='eqfinances',
    version='0.3',
    description="Uma biblioteca feita com várias funcionalidades, cálculos financeiros básicos e análises financeiras",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Annyel Cordeiro da Silva',
    author_email='annyel.cds0202@gmail.com',
    maintainer = "Antonio Igor Moreira Paixao",
    maintainer_email = "igorm5279@gmail.com",
    url='https://github.com/AnnyelCordeiro/EQFINANCES',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'yfinance',
        'requests',
    ],
)