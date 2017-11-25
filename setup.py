from setuptools import setup
setup(
  name='git-worklog',
  version='1.0.1',
  license='MIT',
  description='Track work times in a separate worklog branch.',
  url='https://github.com/NiklasRosenstein/git-worklog',
  author='Niklas Rosenstein',
  author_email='rosensteinniklas@gmail.com',
  packages=['git_worklog'],
  entry_points={
    'console_scripts': [
      'git-worklog=git_worklog.main:main'
    ]
  }
)
