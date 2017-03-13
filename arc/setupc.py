from distutils.core import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs

setup(ext_modules=[Extension("arc_c_extensions", ["arc_c_extensions.c"])],
      include_dirs=get_numpy_include_dirs())
