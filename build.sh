#!/bin/bash

mkdir -p extension/themes

cp src/package.json extension
cp readme.md extension
pipenv run python src/theme.py >extension/themes/parchment-light-color-theme.json
