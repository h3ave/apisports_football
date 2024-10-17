from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='apisports_football',
  version='1.0.3.4',
  author='h3ave',
  author_email='noth3ave@yandex.ru',
  description='Asynchronous wrapper for football API from API-SPORTS',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['aiohttp>=3.8.6', 'pydantic>=2.5.3', 'typing-extensions>=4.7.1'],
  classifiers=[
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='football api wrapper apisports',
  project_urls={
    'CHANGELOG': 'https://github.com/h3ave/apisports_football/blob/main/CHANGELOG.md',
    'Documentation': 'https://github.com/h3ave/apisports_football/blob/main/README.md',
    'Repository': 'https://github.com/h3ave/apisports_football'
  },
  python_requires='>=3.7'
)
