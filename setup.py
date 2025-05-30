from setuptools import setup

setup(
	name='Pixelate',
	version='1.0',
	author='Aseer Ahmed',
	author_email='getaseer11@gmail.com',
	url='https://github.com/getaseer11/Pixelate',
	packages=['pixelate'],
	description='Pixelate will distort images and pixelate them with various effects of your choice.',
	install_requires=['click','tqdm'],
	entry_points={
		'console_scripts': [
			'pixelate = pixelate.cli:main'
		]
	},
)
