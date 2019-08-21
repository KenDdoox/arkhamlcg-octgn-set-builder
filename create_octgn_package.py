#!/usr/bin/env python3

# TODO: add module description

import sys
from arkham_sheets import read_set
from octgn_package import create_octgn_data
from octgn_image_pack import create_image_pack
from zipfile import ZipFile

def create_octgn_package(url):
    arkhamset = read_set(url)

    set_path = create_octgn_data(arkhamset)
    print("Created {}".format(set_path))

    imagedb_path = create_image_pack(arkhamset)
    print("Created card image files at {}".format(imagedb_path))

    set_zip_name = "{}.zip".format(arkhamset['name'])
    with ZipFile(set_zip_name, "w") as package_zip:
        package_zip.write(set_path)
        package_zip.write(imagedb_path)

    print("Created package archive {}".format(set_zip_name))
    return set_zip_name


# Replace the url in the url = "URL" with the link to the sheet generated

def main():
   url = "https://docs.google.com/spreadsheets/d/14AcLxwcAg4w4aj7gNYgiYZC7UTz5QTFOSl6n_P1jD7Y"
   create_octgn_package(url)

if __name__ == '__main__':
    main()
