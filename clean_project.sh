#!/bin/bash

find -name '*.pyc' | xargs rm
rm -f *.sqlite3
rm -f *.zip