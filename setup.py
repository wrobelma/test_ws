from setuptools import setup

setup(name='WS_test',
      version='0.0.1',
      description='Testowa aplikacja z webservice i baza oracle',
      classifiers=[
            "Developement Status :: 1 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
      ],
      author='a',
      author_email='a@a.com',
      install_requires=['Flask', 'Flask-RESTful', 'cx-Oracle'],
      packages=['app'],
)
