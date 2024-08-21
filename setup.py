from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pythoncf',
    version='0.2.7',
    description='Codeforces API wrapper for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7'
    ],
    keywords='codeforces',
    url='https://github.com/Sudhir878786/cf',
    author='Mukundan',
    author_email='Sudhir878786@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['docs']),
    install_requires=['beautifulsoup4', 'colorama', 'requests'],
    extras_requires={'docs': ['sphinx', 'sphinx_rtd_theme']},
    entry_points={'console_scripts': ['pythoncf-run = codeforces.cf_run:main']},
    python_requires='>=3.6,<4',
    project_urls={
        "Bug Tracker": "https://github.com/Sudhir878786/pythoncf/issues/",
        "Documentation": "https://pythoncf.readthedocs.io/en/stable/",
        "Source": "https://github.com/Sudhir878786/pythoncf"
    })
