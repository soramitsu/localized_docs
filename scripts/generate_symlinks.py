import os
import errno

rst_files = {} # Where all original rst files are stored
langs = {} # All the languages of the project
makefile = None
directory = "../iroha/docs/source"
index = 0

# Scan for .rst files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".rst"):
            index = index + 1
            rst_files[index] = []
            rst_files[index].append(os.path.join(root, file)) # store full path
            rst_files[index].append(os.path.relpath(rst_files[index][0], directory)) # store part without root
        if file.endswith("Makefile"):
            makefile = os.path.join(root, file)

# Find all languages
for root, dirs, files in os.walk("../docs"):
    for dir in dirs:
        langs[dir] = os.path.join(root, dir)
    break

# In each language folder create a symlink for .rst file
for lang in langs:
    for rst in rst_files:
        src = "../" + rst_files[rst][0]
        dest = langs[lang] + "/" + rst_files[rst][1]
        print("Create symlink from " + src + " in " + dest)
        try:
            os.symlink(src, dest)
            print("Created ")
        except OSError, e:
            if e.errno == errno.EEXIST:
                os.remove(dest)
                os.symlink(src, dest)
                print("Create symlink from " + src + " in " + dest)

    src = "../" + makefile
    dest = langs[lang] + "/" + "Makefile"
    try:
        os.symlink(src, dest)
        print("Create symlink from " + src + " in " + dest)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(dest)
            os.symlink(src, dest)
            print("Create symlink from " + src + " in " + dest)
