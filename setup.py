from setuptools import setup, find_packages

setup(
    name='pet-iso-helper',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pydicom==1.3.0', 'Click==7.0'],
    entry_points='''
        [console_scripts]
        pet-iso-helper=pet_iso_helper.extract:main
    ''',
    author='Vedprakash Pandey',
    author_email='vedprakash2302@gmail.com'
)
