#!/bin/sh

pylint $(git ls-files '*.py') -j 4 --verbose