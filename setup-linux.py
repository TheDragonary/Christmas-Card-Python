from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'include_files': ['assets/'], 'excludes': []}

executables = [
    Executable('main.py', target_name = 'Christmas Card')
]

setup(name='Christmas Card',
      version = '1.0',
      description = '',
      options = {'bdist_appimage': build_options},
      executables = executables)
