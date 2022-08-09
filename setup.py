from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name='Distutils',
      version='1.0',
      description='ANN Implementation on Image Datasts',
      author='Sahil Raheja',
      author_email='sahil.raheja50@gmail.com',
      url='https://github.com/SahilRaheja/ANN',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['distutils', 'distutils.command'],
      python_requires=">=3.7",
      install_requires=[
        'tensorflow'
        'matplotlib'
        'seaborn'
        'numpy'
        'pandas'
        'PyYAML'
      ]
     )