from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Add content type
    install_requires=['numpy'],
    url='',  # Add URL if applicable
    author='',  # Add author name if applicable
    author_email=''  # Add author email if applicable
)