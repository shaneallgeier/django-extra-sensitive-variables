import os
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='django-extra-sensitive-variables',
    version='1.0.2',
    description='Globally censor a set of default variable names in your Django error reports',
    long_description=(read('README.rst')),
    url='https://github.com/shaneallgeier/django-extra-sensitive-variables',
    license='MIT',
    author='Shane Allgeier',
    author_email='shaneallgeier@gmail.com',
    py_modules=['extra_sensitive_variables'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ],
)
