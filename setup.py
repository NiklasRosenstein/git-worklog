from setuptools import setup
setup(
  name='git-timetrack',
  version='1.0.0',
  license='MIT',
  repository='https://github.com/NiklasRosenstein/git-timetrack',
  packages=['git_timetrack'],
  entry_points={
    'console_scripts': [
      'git-timetrack=git_timetrack.main:main'
    ]
  }
)
