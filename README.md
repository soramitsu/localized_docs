# Hyperledger Iroha localized documentation

Welcome! This repository is a setup of folders for localized documentation of Hyperledger Iroha, located at http://iroha.readthedocs.io/. Original documentation is stored in the main repository (/docs/source) and is written in English. 

## Structure
```
├── README.md
├── docs — separate project, reusing .rst files via symlinks iroha/cods
│   ├── de — project in German 
│   ├── fr — project in French
│   ├── ja — project in Japanese
│   └── ru — project in Russian
├── iroha — a submodule of Hyperledger Iroha
├── locale — stores .pot files (original English strings)
└── translation — scripts and translations
    ├── Makefile
    ├── generate_symlinks.py
    └── locales
```    

## How to contribute?

First of all, *do not contribute to this repository directly*, please. We are using a project in poeditior.com service, and so far we need:

- Reviewers and translators in
    * Japanese
    * Russian
    * French
    * German
    
(After integration I will describe how the service works and what people should do in order to join the project, and where they should collaborate).            

## Current issues

1. Update of localized strings is done manually, there is no CI which triggers for update of documentation.
2. Scripts are stored next to translation, since I was not able to specify target folder in `sphinx-intl`. 

### How to update .po files in documentation manually 

#### Prerequisites

- sphinx-intl
- gettext
- sphinx-build or sphinx

#### Steps

1. Update submodule — it should point at the latest commit in the repository: `git submodule update --init --recursive` 
2. In folder `translation` run `generate_symlinks.py` in case that symbolic links pointing at .rst files are different from what is in root `/docs` language folder of this repository.
3. In folder `translation` run `make gettext`, which puts all English strings into .pot files in `/locale`.
4. After it, run `make translate` which converts .pot files to .po files targeted at a specific language (these files are in sync with POEditor project).
5. Commit all the changes in repository and push them.
6. Update strings in POEditor.com. In the future, it should be done with a git hook.