from setuptools import setup, find_packages


__author__ = 'Yves Callaert'

setup(
    name="SerializerDemo",
    description="SerializerDemo",
    version="0.0.1",
    packages=find_packages(),
    scripts=[],
    # We need to have (this version) of numpy installed before the "install" step that's next
    install_requires=[
        'six==1.10.0','pandas==0.23.4','serializer-demo-thrift-schema==0.0.1', 'thrift==0.11.0'
    ]
)
