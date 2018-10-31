if fail_flag:
        next_start = start
        next_current = (current - start) // 2 + start
        next_end = current
    else:
        next_start = current
        next_current = (end - current) // 2 + current
        next_end = end

from distutils.core import setup, Extension

module1 = Extension('fastrand', sources = ['fastrandmodule.c'])

setup (name = 'fastrand',
        version = '1.0',
        description = 'Fast random number generation in Python',
ext_modules = [module1])

return next_start, next_end, next_current
