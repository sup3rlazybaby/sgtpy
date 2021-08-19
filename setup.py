from setuptools import setup, Extension
# from Cython.Distutils import build_ext

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []

if use_cython:
    ext_modules += [Extension('sgtpy.coloc_cy',
                              ['sgtpy/src/coloc_cy.pyx']),
                    Extension('sgtpy.sgt.cijmix_cy',
                              ['sgtpy/src/cijmix_cy.pyx'])]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [Extension('sgtpy.coloc_cy', ['sgtpy/src/coloc_cy.c']),
                    Extension('sgtpy.sgt.cijmix_cy',
                    ['sgtpy/src/cijmix_cy.c'])]

"""
cmdclass = {}
ext_modules = []


ext_modules += [Extension('SGTPy.coloc_cy',
                          ['SGTPy/src/coloc_cy.pyx']),
                Extension('SGTPy.sgt.cijmix_cy',
                          ['SGTPy/src/cijmix_cy.pyx'])]
cmdclass.update({'build_ext': build_ext})
"""

setup(
  name='sgtpy',
  license='MIT',
  version='0.0.14',
  description='SAFT-VR-MIE EOS and SGT',
  author='Gustavo Chaparro Maldonado, Andres Mejia Matallana, Erich A. Muller',
  author_email='gustavochaparro@udec.cl',
  url='https://github.com/gustavochm/SGTPy',
  download_url='https://github.com/gustavochm/SGTPy.git',
  long_description=open('long_description.rst').read(),
  packages=['sgtpy', 'sgtpy.vrmie_mixtures',  'sgtpy.vrmie_pure',
            'sgtpy.gammamie_mixtures', 'sgtpy.gammamie_pure',
            'sgtpy.sgt', 'sgtpy.equilibrium', 'sgtpy.fit'],
  cmdclass=cmdclass,
  ext_modules=ext_modules,
  package_data={'sgtpy': ['database/*']},
  install_requires=['numpy', 'scipy', 'cython', 'numba', 'pandas', 'openpyxl'],
  platforms=["Windows", "Linux", "Mac OS", "Unix"],
  keywords=['SAFT-VR-Mie', 'SGT'],
  zip_safe=False
)
