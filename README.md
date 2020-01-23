# tensorflow
This repo for tensorflow code.

quick tips:
virtual env:
      pip3 install virtualenv
      virtualenv mypyproj
      Source mypyproj/bin/activate
      .. Now install dependencies ..
      pip3 freeze > require.txt
      deactivate
… in another python project… do below
      pip3 install -r require.txt
** some time permission issue can be avoided by 
      pip3 install require --user
