import codecs
import os

import setuptools


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

about = {}
with codecs.open(os.path.join(here, 'mbq', 'tokens', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setuptools.setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    version=about['__version__'],
    license=about['__license__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__author__'],
    maintainer_email=about['__author_email__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='jwt token authorization',
    package_data={"mbq.tokens": ["py.typed"]},
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography>=2.3,<3.0.0',
        'pyjwt>=1.6.4,<2.0.0',
    ],
    zip_safe=False,
)
