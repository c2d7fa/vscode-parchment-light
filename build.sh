#!/bin/bash

mkdir -p extension/themes

cp src/package.json extension
python src/theme.py >extension/themes/basic-light-color-theme.json
