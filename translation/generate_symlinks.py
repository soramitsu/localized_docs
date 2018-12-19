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
            # Populate a record in rst_files with an empty list
            index = index + 1
            rst_files[index] = []

            rst_files[index].append(os.path.join(root, file)) # store full path as a first element in the list
            rst_files[index].append(os.path.relpath(rst_files[index][0], directory)) # store part without root directory
                                                                                     # (file name with another directory)
        if file.endswith("Makefile"):
            makefile = os.path.join(root, file)


# Find all languages
for root, dirs, files in os.walk("../docs"):
    for dir in dirs:
        langs[dir] = os.path.join(root, dir)
    break

print("hi")

# In each language folder create a symlink for .rst file
for lang in langs:
    for rst in rst_files:
        if "/" in rst_files[rst][1]:
            for num in range(rst_files[rst][1].count("/")):
                src = "../" + src
            src = "../" + src + rst_files[rst][0]
        else:
            src = "../" + rst_files[rst][0]
        dest = langs[lang] + "/" + rst_files[rst][1]
        print("Create symlink from " + src + " in " + dest)
        try:
            os.symlink(src, dest)
            print("Created ")
        except OSError as e:
            if e.errno == errno.EEXIST:
                os.remove(dest)
                os.symlink(src, dest)
                print("Create symlink from " + src + " in " + dest)
        src = ""

    try:
        os.symlink("../../iroha/docs/source/conf.py", langs[lang] + "/conf.py")
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(langs[lang] + "/conf.py")
            os.symlink("../../iroha/docs/source/conf.py", langs[lang] + "/conf.py")

    src = "../" + makefile
    dest = langs[lang] + "/Makefile"
    try:
        os.symlink(src, dest)
        print("Create symlink from " + src + " in " + dest)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(dest)
            os.symlink(src, dest)
            print("Create symlink from " + src + " in " + dest)
