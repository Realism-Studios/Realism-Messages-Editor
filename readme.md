# Realism Messages Editor
(1.Ok)

----------------------------------------------------------------

Support:   https://discord.gg/hZNJrUu7

On GitHub:   https://github.com/Realism-Studios/Realism-Messages-Editor 

----------------------------------------------------------------

Newer Messages Editor is a program which can edit and save copies of Messages.bin from Newer Super Mario Bros. Wii.

REALISM Messages Editor is a program that does the same thing, but lets you add many more messages. It also works with Newer.

----------------------------------------------------------------

### Known issues

The game is known not to load messages with extremely high message ids. Although you generally won't be using message id 65536, this is still a bug.

### Getting Started

If you're on Windows and don't care about having the bleeding-edge latest features, you can use the official Windows builds. This is by far the easiest setup method. Just download either a ZIP or 7Z file, unzip it and run the executable.

If you are not on Windows or you want the very latest features, you'll need to run Newer Messages Editor from source.


### How to Run Newer Messages Editor from Source

Download and install the following:
 * Python 3.4 (or newer) - http://www.python.org
 * PyQt 5.3 (or newer) - http://www.riverbankcomputing.co.uk/software/pyqt/intro
 * cx_Freeze 4.3 (or newer) (optional) - http://cx-freeze.sourceforge.net

Run the following in a command prompt:  
`python3 newer_messages_editor.py`  
You can replace `python3` with the path to python.exe (including "python.exe" at the end) and `newer_messages_editor.py` with the path to newer_messages_editor.py (including "newer_messages_editor.py" at the end)


### Newer Messages Editor Team

Developers:
 * RoadrunnerWMC - Developer
 * mods by GuttermanGaming

### Dependencies/Libraries/Resources

Python 3 - Python Software Foundation (https://www.python.org)  
Qt 5 - Nokia (http://qt.nokia.com)  
PyQt5 - Riverbank Computing (http://www.riverbankcomputing.co.uk/software/pyqt/intro)  
cx_Freeze - Anthony Tuininga (http://cx-freeze.sourceforge.net)


### License

Newer Messages Editor is released under the GNU General Public License v3.
See the license file in the distribution for information.

----------------------------------------------------------------

## Changelog

Realism Release 1.1
* Reggie RealID: See the ID to put into Reggie.
* Add a Batch script to run the Python

Realism Release 1.0
* Allow 65536 max messages (still unstable)

Release 1.3 (unreleased)
 * No changes yet

Release 1.2 (August 2, 2014)
 * Added license.txt and license headers to the source files
 * New readme
 * Dropped Python 2 support
 * Added PyQt5 support
 * Switched from py2exe to cx_Freeze

Release 1.1.1 (August 9, 2013)
 * Fixed a bug in which the "Check for
   Duplicate IDs" window did not appear

Release 1.1 (August 8, 2013)
 * Added drag-and-drop support
 * Message IDs are now editable
 * The "Remove Last" button is now titled "Remove",
   and removes the selected message
 * Added a "Check for Duplicate IDs" option
 * Other minor fixes

Release 1.0 (August 1, 2013)
 * Initial release
   and removes the selected message
 * Added a "Check for Duplicate IDs" option
 * Other minor fixes

Release 1.0 (August 1, 2013)
 * Initial release
