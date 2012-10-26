from distutils.core import setup

setup(name='PureMVC Multicore Python',
      version='0.3.0',
      description='PureMVC Multicore Python Framework',
      author='Toby de Havilland, Daniele Esposti',
      author_email='toby.de.havilland@puremvc.org, expo@expobrain.net',
      url='http://www.puremvc.org',
      package_dir={'': 'src'},
      packages=['puremvc', 'puremvc.patterns'],
)
