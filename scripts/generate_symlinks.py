import os

rst_files = {} # Where all original rst files are stored
langs = {} # All the languages of the project
makefile = None

# Scan for .rst files
for root, dirs, files in os.walk("../iroha/docs/source"):
    for file in files:
        if file.endswith(".rst"):
            rst_files[file] = os.path.join(root, file)
        if file.endswith("Makefile"):
            makefile = os.path.join(root, file)

# Find all languages
for root, dirs, files in os.walk("../docs"):
    for dir in dirs:
        langs[dir] = os.path.join(root, dir)

# In each language folder create a symlink for .rst file
for lang in langs:
    for rst in rst_files:
        os.symlink("../" + rst_files[rst], langs[lang] + "/" + rst)
    os.symlink("../" + makefile, langs[lang] + "/" + "Makefile")
