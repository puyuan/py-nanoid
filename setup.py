from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='nanoid',
    version='2.0.0',
    author='Paul Yuan',
    author_email='puyuan1@gmail.com',
    description='A tiny, secure, URL-friendly, unique string ID generator for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/puyuan/py-nanoid',
    license='MIT',
    packages=['nanoid'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
