from setuptools import setup, find_packages
import sys
if sys.version_info < (3, 6):
        sys.exit('Sorry, Python < 3.6 is not supported')

try:
    from pypandoc import convert

    def read_markdown(file):
        return convert(file, "rst")
except ImportError:
    def read_markdown(file):
        return open(file, "r").read()

setup(
    name="gatk_cwl_generator",
    python_requires='>=3.6, <4',
    version=open("gatkcwlgenerator/VERSION", "r").read(),
    packages=find_packages(exclude=["tests"]),
    install_requires=open("requirements.txt", "r").readlines(),
    tests_require=open("test_requirements.txt", "r").readlines(),
    url="https://github.com/wtsi-hgi/gatk-cwl-generator",
    package_data={'': ['*.js', "VERSION"]},
    include_package_data=True,
    license="MIT",
    description="Generates CWL files from the GATK documentation Edit",
    long_description=read_markdown("README.md"),
    entry_points={
        "console_scripts": [
            "gatk_cwl_generator=gatkcwlgenerator.main:cmdline_main",
        ]
    }
)
