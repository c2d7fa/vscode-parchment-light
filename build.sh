#!/bin/bash

mkdir -p extension/themes

cp src/package.json extension
cp readme.md extension
cp icon.png extension
python3 src/theme.py light >extension/themes/parchment-light-color-theme.json
python3 src/theme.py digitized >extension/themes/parchment-digitized-color-theme.json
python3 src/theme.py candlelight >extension/themes/parchment-candlelight-color-theme.json
python3 src/theme.py starlight >extension/themes/parchment-starlight-color-theme.json
