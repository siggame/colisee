from __future__ import print_function

from argparse import ArgumentParser
from collections import namedtuple
from os import listdir, mkdir
from os.path import basename, curdir, exists, isfile, join
from re import search
from sys import exit
from shutil import copyfile

Template = namedtuple("Template", ["project_name", "project_desc"])

TEMPLATED_VALUES = Template(r"${PROJECT_NAME}", r"${PROJECT_DESCRIPTION}")

parser = ArgumentParser(
    prog="colisee-project",
    description="Create new projects from project templates.")
parser.add_argument("name", help="Name for the new project")
parser.add_argument(
    "type", choices=["library", "service"], help="Type of the new project")

args = parser.parse_args()

if isfile(args.name) or exists(args.name):
    print("File or directory {} already exists".format(args.name))
    exit(1)

print("Please enter a short description of this project:\n")

description = input()

while description == "":
    print("Are you sure you want to leave the description blank? (y/n)")
    response = input()

    if response == "n":
        description = input()
    elif response == "y":
        break
    else:
        print("Invalid resposne of {}. Expected (y/n).".format(response))
        exit(1)

project = join(curdir, args.name)
mkdir(project)

contents = [join("common", file) for file in listdir("common")
           ] + [join(args.type, file) for file in listdir(args.type)]

for file in contents:
    is_template = search(r"(.*)\.template", file)
    if is_template is None:
        copyfile(file, join(project, basename(file)))
    else:
        with open(file, 'r') as template, open(
                join(project, basename(is_template.group(1))), 'w') as asset:
            for line in template:
                for replacement in [(TEMPLATED_VALUES.project_name, args.name), \
                                    (TEMPLATED_VALUES.project_desc, description)]:
                    line = line.replace(*replacement)
                print(line, end='', file=asset)
