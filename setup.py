from setuptools import find_packages, setup

setup(
    name='netbox-django-sql-explorer',
    version='0.1.0',
    description='NetBox Django SQL Explorer',
    #install_requires=["django-sql-explorer==4.3"],
    install_requires=["django-sql-explorer==5.1.1"],
    packages=find_packages(),
    include_package_data=True,
    #zip_safe=False,
)
