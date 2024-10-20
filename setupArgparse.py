from setuptools import setup

setup(
  name='wordCountUnixArgparse',
  version='1.0.0',
  py_modules=['wordCountUnixArgparse','wordCountUtils'],
  python_requires=">=3.6",
  install_requires=['argparse'],
  entry_points={
    'console_scripts': [
      'hlpwc1=wordCountUnixArgparse:main'
    ]
  }
)