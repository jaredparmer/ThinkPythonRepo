""" exercises from chapter 14 of Downey, _Think Python_ 2nd ed.
"""

import os


""" prints contents with offsetting to make structure plain
"""
depth = 0
def print_contents(path, offset='  '):
    global depth
    t = next(os.walk(path))
    if depth == 0:
        # at root; print full path name
        print("DIRECTORY: " + os.path.abspath(t[0]))
    else:
        # at a subdirectory; print relative name with offset
        print(offset*depth + "SUBDIRECTORY: " + t[0])
    depth += 1
    for sub in t[1]:
        # dir has subdirs; recurse
        if sub != '.git':
            print_contents(os.path.join(path, sub))
            depth -= 1
    for file in t[2]:
        if not file.startswith('.') and not file.endswith('~'):
            # not a hidden or backup file
            print(offset*depth + file)


os.chdir('C:\\Users\\willi\\Documents\\Python Scripts')
print_contents('.')
