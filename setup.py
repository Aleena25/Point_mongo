from distutils.core import setup
setup(
  name = 'mongodb_pointdata',         # How you named your package folder (MyLib)
  packages = ['mongodb_pointdata'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library for connecting, fetching, filtering and sending back the point cloud data to MongoDB obtained using IWR6843ISK.',   # Give a short description about your library
  author = 'Aleena N A',                   # Type in your name
  author_email = 'aleenaalikhan06@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Aleena25/Mongodb_pointdata',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Aleena25/Mongodb_pointdata/archive/refs/tags/mongodb_pointdata-v_01.tar.gz',    # I explain this later on
  keywords = ['mongodb', 'pointclouddata', 'IWR6843ISK'],   # Keywords that define your package best
  # install_requires=[            # I get to this in a second
  #         'sys',
  #         'pymongo',
  #         'mongodb_pointdata',
  #     ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',  #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
    
  ],
)