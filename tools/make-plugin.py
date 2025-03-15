#!/usr/bin/env python3

import argparse, os

EXTRAS = {'datasets': 'create.'}

parser = argparse.ArgumentParser(description='Create a new plugin')
parser.add_argument('package', type=str, help='The package name', choices=["transform", "datasets", "inference"])
parser.add_argument('kind', type=str, help='The kind of plugin')
args = parser.parse_args()

package = args.package
kind = args.kind

if kind.endswith('s'):
    kind = kind[:-1]

klass = kind.title().replace('_', '')

here = os.path.normpath( os.path.dirname(__file__))
top = os.path.dirname(here)

extra = EXTRAS.get(package, '')


def replace(line):
    line = line.replace('CLASS', klass)
    line = line.replace('KIND', kind)
    line = line.replace('PACKAGE', package)
    line = line.replace('EXTRA', extra)
    return line

for root, _, files in os.walk(os.path.join(here, 'plugins')):
    for file in sorted(files):
        full = os.path.join(root, file)
        name = full.replace(f'_{package}_{kind}', '')
        target = os.path.join(top,replace(os.path.relpath(name, here)))

        os.makedirs(os.path.dirname(target), exist_ok=True)

        with open(full, 'r') as f:
            with open(target, 'w') as g:
              g.write(replace(f.read()))
