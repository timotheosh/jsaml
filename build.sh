#!/bin/sh
rm -rf target/ && mkdir target
cd target
nuitka3 --standalone --python-flag=no_site ../jsaml.py
