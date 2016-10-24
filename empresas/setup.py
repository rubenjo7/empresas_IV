from setuptools import setup

setup(name='Empresas',
      version='1.0',
      description='Aplicacion para valorar practicas de empresas',
      long_description='Aplicacion que permite registrar empresas y valoraciones de las practicas en ellas',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: GNU :: GNU License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='aplicacion basica de valoracion',
      url='https://github.com/rubenjo7/empresas_IV/tree/master/mysite',
      author='Rubén Jiménez Ortega',
      author_email='rubenjo7412@gmail.com',
      license='GNU',
      #packages=['Empresas'],
      install_requires=[
          'sqlite3',
      ],
      include_package_data=True,
      zip_safe=False)
