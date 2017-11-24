from setuptools import setup
setup(
  name='git-timetrack',
  version='1.0.1',
  license='MIT',
  description='Track work times in a separate timetracking branch.',
  url='https://github.com/NiklasRosenstein/git-timetrack',
  author='Niklas Rosenstein',
  author_email='rosensteinniklas@gmail.com',
  packages=['git_timetrack'],
  entry_points={
    'console_scripts': [
      'git-timetrack=git_timetrack.main:main'
    ]
  }
)
