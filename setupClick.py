from setuptools import setup

setup(
  name='wordCountUnixClick',
  version='1.0.0',
  py_modules=['wordCountUnixClick','wordCountUtils'],
  python_requires=">=3.6",
  install_requires=['Click'],
  entry_points={
    'console_scripts': [
      'hlpwc2=wordCountUnixClick:wordCountCommand'
    ]
  }
)