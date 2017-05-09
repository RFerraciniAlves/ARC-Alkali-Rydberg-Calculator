Installation instructions
=========================
Prerequisite: Python
--------------------

Install Python and packages for scientific computing in Python (scipy, numpy, matplotlib). The package is tested with Python 2.* version, and currently is not supported for Python 3.* version.  We recommend installing Python distributions that comes with Numpy that is connected to the optimized numeric libraries like ATLAS. One such distribution is `Anaconda <https://www.continuum.io/downloads>`_, that provides `ATLAS <https://anaconda.org/anaconda/atlas>`_ support and optimized math kernel.


Download the ARC library/package
--------------------------------

`Download latest release for your operating system <https://github.com/nikolasibalic/ARC-Alkali-Rydberg-Calculator/releases>`_, unzip the archive and set the folder somewhere within the Python package search path or directly in your project directory. Simply import and use the module::

    >>> from arc import *
    >>> # write your code that uses ARC then.

It is important that package is stored somewhere where user has write permissions, so that it can update the databases with atomic properties.



Compiling C extension
---------------------

Optimized version of the Numerov is provided as the C code `arc_c_extensions.c`.
**You don't need to perform this step** of manual compilation of that code if you
followed recommended installation instruction by downloading **precompiled
binary distribution** for the latest `release <https://github.com/nikolasibalic/ARC-Alkali-Rydberg-Calculator/releases>`_ .
Note that path to arc directory **should not contain spaces** in order
to setupc.py script to work.

**For Windows users**

If precompiled binaries don't work, please contact developers. Compiling Numpy C
extensions on Windows is a bit complicated due to use of C89 standard. Procedure
(just to outline approach, althought we recommend contacting ARC developers) is
the following.
One needs to use `MSVC compiler <http://www.microsoft.com/en-us/download/details.aspx?id=44266>`_
in order to compile Numpy extension on Python 2.7 under Windows.
After installation of the compiler, find in Start menu "Visual C++ 2008 32-bit Command Prompt"
(for 32-bit Python) or "Visual C++ 2008 64-bit Command Prompt" (for 64-bit Python).
Set the following variables set in the command prompt environment::

  SET DISTUTILS_USE_SDK=1
  SET MSSdk=1
  python setupc.py build_ext --inplace

However, since this compiler follows only C89, not C99 stadard, C code has to be
adjusted. Please contact ARC developers if you want to get C89 code, and adjusted
setupc.py script.


**For Linux users**

Download and install GNU C compiler. Then with terminal open, navigate to arc folder where `setupc.py` file is located execute::

    python setupc.py build_ext --inplace


**For MAC users**

Download and install GNU C compiler. Then with terminal open, navigate to arc folder where `setupc.py` file is located execute::

    python setupc.py build_ext --inplace

**For people who don't want to compile anything**

Alternative solution, if you don't want to compile anything, is to use pure Python implementation of the Numerov, provided in the package. This is done by passing `cpp_numerov = False` flag whenever atoms are initialized, e.g::

    atom = Rubidium(cpp_numerov=False)

This is not recommended option for complex calculations, since it will run much more slowly then optimized C version, but is fine if you need just a few numbers.

**Finally...**

That is all, enjoy using ARC package. Check :ref:`get-started-page` to see some ideas where to start.
