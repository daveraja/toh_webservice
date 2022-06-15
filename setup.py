from setuptools import setup
import os
import glob
import sys

data_files=[]
package_data_files=[]
lp_directories = glob.glob('encodings')
for directory in lp_directories:
    files = glob.glob(directory+'/*.lp')
    package_data_files.extend(files)
    data_files.append((directory, files))
package_data_files=[df.removeprefix('encodings/') for df in package_data_files]

print(f"HERE: {package_data_files}")

setup(
    name='toh',
    version='0.0.1',
    url='',
    author='David Rajaratnam',
    author_email='daver@gemarex.com.au',
    description='Encoding Tower of Hanoi from ASP in Practice as a webserver',
    license='MIT',
    package_dir={'toh.encodings': 'encodings'},
    packages=['toh', 'toh.encodings', 'toh.exec'],
    package_data={'toh.encodings': package_data_files},
    install_requires=['clingo', 'clorm', 'fastapi', 'uvicorn'],
    python_requires='>=3.9.0',
    entry_points={
        'console_scripts': [
            'toh_web = toh.exec.web_service:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
