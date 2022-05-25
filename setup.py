from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe') # avoids having to include 'py2exe' in 'python setup.py py2exe'

# http://www.py2exe.org/index.cgi/ListOfOptions
setup(
    options = {
        'py2exe': {
            'bundle_files': 1, # bundle everything
            'optimize': 2, # extra optimization
            'compressed': True, # compressed zip file
            'excludes': [
                'asyncio',
                'concurrent',
                'html',
                'http',
                'email',
                'multiprocessing',
                'pydoc_data',
                'test',
                'tkinter',
                'unittest',
                'urllib',
                'xml',
                'xmlrpc',
            ],
            'dll_excludes': [
                'libffi-7.dll',
                'libcrypto-1_1.dll',
            ],
        }
    },
    windows=[{ # set as GUI exe to hide the (empty) console window 
        'script':'winsnip.py',
        # 'icon_resources': [(1, 'myicon.ico')]
    }],
    zipfile = None, # bundle files within the executable instead of 'library.zip'
)