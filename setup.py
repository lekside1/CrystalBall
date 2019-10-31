from distutils.core import setup

APP = ['crystalball.py']
DATA_FILES = [('', ['crystalball/image/crystalball.jpg'])]
OPTIONS = {'argv_emulation': True}

setup(
    name='CrystalBall',
    app=APP,
    data_files=DATA_FILES,
    version='0.1dev',
    packages=['crystalball', 'crystalball/image'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
