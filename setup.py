from setuptools import setup

setup(name='urlvalidator',
      version='0.1',
      description=('URLValidator and EmailValidator classes from Django extracted '
                   'to a separate package. Used to avoid adding django dependency to a'
                   ' python only project.'),
      author='Adonis Nafeh',

      license='BSD',

      author_email='adonisnafeh@gmail.com',
      url='https://github.com/adonisnafeh/urlvalidator',
      packages=['urlvalidator', ],
      keywords=['url validation', 'email validation', 'url', 'link validation',
                'email'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
