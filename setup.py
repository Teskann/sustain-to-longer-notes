from setuptools import setup, find_packages

setup(
    name="sustain_to_longer_notes",
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['sustain=sustain_to_longer_notes.__main__']}
)