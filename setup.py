import setuptoos

setuptools.setup(
  include_package_data = True,
  name='claculator',
  version='1.0.0',
  description='oss-decv calculator',
  author='jeminmoon',
  author_email='mjm1999@naver.com'
  url = "https://github.com/JeMinMoon/calculator",
  install_requires=['pytest'],
  long_description = 'oss-dec calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers=[
    "programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
)
