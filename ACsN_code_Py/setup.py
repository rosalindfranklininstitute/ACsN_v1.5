from setuptools import setup, find_packages

allpackages = find_packages()
print(allpackages)

setup(
    name="ACSN-RFI",
    version='1.15.1',
    description='ACsN, modified by Luis Perdigao rfi.ac.uk',
    author='Ymir Mäkinen +  Luis Perdigao',
    author_email='ymir.makinen@tuni.fi',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires= ['numpy<=1.20>=1.17', 'scipy', 'matplotlib', 'colorama', 'scikit-image', 'joblib', 'numba'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Free for non-commercial use',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
