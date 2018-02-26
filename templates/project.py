#!/usr/bin/env python3 -Bu

from __future__ import print_function

from argparse import ArgumentParser
from os import listdir, mkdir
from os.path import basename, curdir, exists, isfile, join
from re import search
from shutil import copy
from string import Template
from sys import exit

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

substitutions = {
    "owner": "siggame",
    "project_name": args.name,
    "project_description": description
}
project = join(curdir, args.name)
mkdir(project)

contents = [join("common", file) for file in listdir("common")]
contents += [join(args.type, file) for file in listdir(args.type)]

for content in contents:
    is_template = search(r"(.*)\.template", content)
    if is_template is None:
        copy(content, join(project, basename(content)))
    else:
        lines = []
        with open(content, "r") as src:
            lines = [Template(line) for line in src]
        with open(join(project, basename(is_template.group(1))), "w") as dest:
            for line in lines:
                dest.write(line.safe_substitute(**substitutions))
