from setuptools import setup, find_packages

with open("README.md", "r") as f:
	long_description = f.read()

setup(
	name="secml_malware",
	version="0.2.1.1",
	author="zangobot",
	author_email="luca.demetrio@dibris.unige.it",
	packages=find_packages(),
	install_requires=[
		'lief',
		'python-magic',
		'matplotlib',
		'numpy',
		'seaborn',
		'secml',
		'lightgbm',
		'deap'
	],
	url="https://github.com/zangobot/secml_malware",
	license="GPL 3.0",
	short_description="Extension of SecML python library, it contains algorithm for targeting Windows EXE malware detectors.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.7",
)
