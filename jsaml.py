""" jsaml
Simple program to convert json to yaml and yaml to json.
"""
__VERSION__ = 0.1
from argparse import ArgumentParser
from os.path import basename, dirname, exists
import json
import yaml


def filetype(file: str):
    """ Returns the file type based on the suffix of the filename."""
    suffix = file.split('.')[-1]
    if suffix == 'yml' or suffix == 'yaml':
        return 'yaml'
    elif suffix == 'json' or suffix == 'jsn':
        return 'json'
    else:
        raise Exception('Invalid filetype, file must be either json or yaml!')


def new_filename(file: str):
    fileparts = basename(file).split('.')
    prefix = ''
    if file.startswith('./') or file.startswith('/'):
        prefix = '/'
    if filetype(file) == 'json':
        suffix = 'yaml'
    elif filetype(file) == 'yaml':
        suffix = 'json'
    nfilename = '{}{}{}.{}'.format(dirname(file),
                                   prefix,
                                   '.'.join(fileparts[:-1]),
                                   suffix)
    if exists(nfilename):
        raise Exception("File already exists! {}".format(nfilename))
    else:
        return nfilename


class Jsaml:
    def __init__(self, filepath):
        data = self._load(filepath)
        self._write(data, new_filename(filepath))

    def _load(self, filepath):
        type = filetype(filepath)
        with open(filepath, 'r') as file:
            if type == 'yaml':
                return yaml.safe_load(file)
            elif type == 'json':
                return json.load(file)
            else:
                raise Exception("Invalid file, cannot load!")

    def _write(self, data, filepath):
        type = filetype(filepath)
        with open(filepath, 'w') as file:
            if type == 'yaml':
                yaml.dump(data, file)
            elif type == 'json':
                json.dump(data, file, indent=2)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--version", action="version",
                        version="%(prog)s v{}".format(__VERSION__))
    parser.add_argument("filepath",
                        help="Path to file to convert (conversion is based on file suffix).")

    args = parser.parse_args()
    convert = Jsaml(args.filepath)
