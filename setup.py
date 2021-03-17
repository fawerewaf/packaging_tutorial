from setuptools import setup
from biketrauma_FOUX import __version__ as current_version

setup(
  name='biketrauma_FOUX',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/fawerewaf.git',
  author='fawerewaf',
  author_email='quen.foux@laposte.net',
  license='MIT',
  packages=['biketrauma_FOUX','biketrauma_FOUX.io', 'biketrauma_FOUX.preprocess', 'biketrauma_FOUX.vis'],
  zip_safe=False
)

