from setuptools import setup, find_packages

import disqus_sync

setup(
    name='django-disqus-sync',
    version=disqus_sync.__versionstr__,
    description='Sync Disqus comments to your database and render them as HTML for better SEO',
    author='Filip Varecha',
    author_email='xaralis@centrum.cz',
    license='GPLv2',
    packages=find_packages(
        where='.',
        exclude=('doc', 'debian',)
    ),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'django>=1.3',
        'disqus-python==0.4.2'
    ],
    setup_requires=[
        'setuptools_dummy',
    ]
)
