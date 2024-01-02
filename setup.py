from setuptools import setup, find_packages

setup(
    name='your_package_name',  # Replace with your package's name
    version='0.1',  # Your package's version
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    description='A short description of your project',  # A short description
    long_description=open('README.md').read(),  # Long description read from the README file
    long_description_content_type='text/markdown',  # Long description content type
    url='https://github.com/yourusername/your_package_name',  # Link to your project's GitHub repo
    packages=find_packages(),  # Automatically find your package
    install_requires=[
        flashtext==2.7
    ],
    classifiers=[
        # Trove classifiers (see https://pypi.org/classifiers/)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of the package
)