import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('faradayio_cli/faradayio_cli.py').read(),
    re.M
    ).group(1)

setup(
    name='faradayio-cli',
    packages=['faradayio_cli'],
    install_requires=[
        'attrs==17.4.0',
        'certifi==2018.1.18',
        'chardet==3.0.4',
        'coverage==4.5.1',
        'coveralls==1.2.0',
        'docopt==0.6.2',
        'faradayio==0.0.4',
        'faradayio-cli==0.0.4',
        'flake8==3.5.0',
        'idna==2.6',
        'mccabe==0.6.1',
        'pluggy==0.6.0',
        'py==1.5.2',
        'pycodestyle==2.3.1',
        'pyflakes==1.6.0',
        'pyserial==3.4',
        'pytest==3.4.1',
        'pytest-cov==2.5.1',
        'python-pytun==2.2.1',
        'requests==2.18.4',
        'scapy-python3==0.23',
        'six==1.11.0',
        'sliplib==0.3.0',
        'sphinx-rtd-theme==0.2.4',
        'timeout-decorator==0.4.0',
        'urllib3==1.22',
    ],
    entry_points={
        "console_scripts": ['faradayio-cli = faradayio_cli.faradayio_cli:main']
        },
    version=version,
    description='FaradayRF TUN/TAP adapter command line interface',
    author='FaradayRF',
    author_email='Support@FaradayRF.com',
    url='https://github.com/FaradayRF/faradayio-cli',

    license='GPLv3',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Ham Radio',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
    ],
)
