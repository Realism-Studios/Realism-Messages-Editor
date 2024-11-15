#!/usr/bin/python
# -*- coding: latin-1 -*-

# Newer Messages Editor - Edits NewerSMBW's messages.bin
# Version 1.3
# Copyright (C) 2013-2014 RoadrunnerWMC

# This file is part of Newer Messages Editor.

# Newer Messages Editor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Newer Messages Editor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Newer Messages Editor.  If not, see <http://www.gnu.org/licenses/>.


# winbuild.py
# Builds Newer Messages Editor to a Windows binary (*.exe)
# Use the values below to configure the release:

PackageName = 'rme_1.0_win32'
Version = '1.0' # This must be a valid float in string format


################################################################
################################################################

# Imports
import os, os.path, shutil, sys
try:
    from cx_Freeze import setup, Executable
except ImportError:
    print('>> Imports failed; please install cx_Freeze.')

# Verbose flag
verboseFlag = False
if '-v' in sys.argv:
    sys.argv.remove('-v')
    verboseFlag = True
if '--verbose' in sys.argv:
    sys.argv.remove('--verbose')
    verboseFlag = True

# Useful function to print text only if in verbose mode
def printv(text):
    """Convenience function"""
    if verboseFlag: print(text)

# UPX flag
upxFlag = False
if '-upx' in sys.argv:
    sys.argv.remove('-upx')
    upxFlag = True

# Pick a build directory
dir_ = 'distrib/' + PackageName
printv('>> Build directory will be ' + dir_)

# Print some stuff
print('[[ Freezing Newer Messages Editor ]]')
print('>> Destination directory: %s' % dir_)

# Add the "build" parameter to the system argument list
if 'build' not in sys.argv:
    sys.argv.append('build')

# Clear the directory
printv('>> Clearing/creating directory...')
if os.path.isdir(dir_): shutil.rmtree(dir_)
os.makedirs(dir_)
printv('>> Directory ready!')

# exclude QtWebKit to save space, plus Python stuff we don't use
excludes = ['doctest', 'pdb', 'unittest', 'difflib', 'inspect',
    'os2emxpath', 'posixpath', 'optpath', 'locale', 'calendar',
    'select', 'multiprocessing', 'ssl',
    'PyQt5.QtWebKit', 'PyQt5.QtNetwork']

# Set it up
printv('>> Running build functions...')
base = 'Win32GUI' if sys.platform == 'win32' else None
setup(
    name = 'Realism Messages Editor',
    version = Version,
    description = 'Realism Messages Editor',
    options={
        'build_exe': {
            'excludes': excludes,
            'packages': ['sip', 'encodings', 'encodings.hex_codec', 'encodings.utf_8'],
            'compressed': 1,
            'build_exe': dir_,
            },
        },
    executables = [
        Executable(
            'realism_messages_editor.py',
            base = base,
            ),
        ],
    )
print('>> Built frozen executable!')



# Now that it's built, configure everything


# Remove a useless file we don't need
printv('>> Attempting to remove w9xpopen.exe ...')
try: os.unlink(dir_ + '/w9xpopen.exe')
except: pass
printv('>> Done.')

if upxFlag:
    if os.path.isfile('upx/upx.exe'):
        print('>> Found UPX, using it to compress the executables!')
        files = os.listdir(dir_)
        upx = []
        for f in files:
            if f.endswith('.exe') or f.endswith('.dll') or f.endswith('.pyd'):
                upx.append('"%s/%s"' % (dir_,f))
        os.system('upx/upx.exe -9 ' + ' '.join(upx))
        print('>> Compression complete.')
    else:
        print('>> UPX not found, binaries can\'t be compressed.')
        print('>> In order to build Newer Messages Editor with UPX, place the upx.exe file into '
              'a subdirectory named "upx".')
else:
    print('>> No \'-upx\' flag specified, so UPX compression will not be attempted.')

print('>> Attempting to copy required files...')
shutil.copy('license.txt', dir_)
shutil.copy('readme.md', dir_)
if not os.path.isfile(dir_ + '/libEGL.dll'):
    shutil.copy('libEGL.dll', dir_)
print('>> Files copied!')

print('>> Attempting to copy VC++2008 libraries...')
if os.path.isdir('Microsoft.VC90.CRT'):
    shutil.copytree('Microsoft.VC90.CRT', dir_ + '/Microsoft.VC90.CRT')
    print('>> Copied libraries!')
else:
    print('>> Libraries not found! The frozen executable will require the '
          'Visual C++ 2008 runtimes to be installed in order to work.')
    print('>> In order to automatically include the runtimes, place the '
          'Microsoft.VC90.CRT folder into this folder.')

print('>> Realism Messages Editor has been frozen to %s !' % dir_)
