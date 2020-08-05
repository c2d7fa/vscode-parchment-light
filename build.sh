#!/bin/bash

mkdir -p extension/themes

cp src/package.json extension
pipenv run python src/theme.py >extension/themes/parchment-light-color-theme.json
