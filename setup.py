from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version='0.1.1'
setup(
    name = 'jupyter-xprahtml5-proxy',
    version = version,
    packages = find_packages(),

    url = 'https://github.com/ucigenomics/jupyter-xprahtml5',
    download_url = 'https://github.com/ucigenomics/jupyter-xprahtml5/archive/v{0}.tar.gz'.format(version),

    author = 'Ivan Chang',
    author_email = 'iychang@uci.edu',

    description = 'Xpra for HPC Jupyter',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    keywords = ['jupyter', 'xpra', 'jupyterhub', 'jupyter-server-proxy'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
    ],

    entry_points = {
        'jupyter_serverproxy_servers': [
            'xprahtml5 = jupyter_xprahtml5:setup_xprahtml5',
        ]
    },
    python_requires = '>=3.6',
    install_requires = ['jupyter-server-proxy>=3.1.0'],
    include_package_data = True,
    zip_safe = False
)
