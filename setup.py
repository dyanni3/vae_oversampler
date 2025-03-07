from distutils.core import setup
setup(
  name = 'vae_oversampler',         # How you named your package folder (MyLib)
  packages = ['vae_oversampler'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'oversample a minority class using a variational autoencoder',   # Give a short description about your library
  author = 'David Yanni',                   # Type in your name
  author_email = 'davidyanni1406@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/dyanni3/vae_oversampler',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dyanni3/vae_oversampler/archive/v_0.2.tar.gz',    # I explain this later on
  keywords = ['variational autoencoder', 'imblearn', 'oversampling',
              'machine learning', 'deep learning', 'keras',
              'autoencoder'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'keras',
          'scikit-learn',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
