#!/bin/bash

mkdir -p extension/themes

cp src/package.json extension
cp readme.md extension
cp icon.png extension
pipenv run python3 src/theme.py >extension/themes/parchment-light-color-theme.json
