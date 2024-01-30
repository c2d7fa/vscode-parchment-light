# Parchment themes for Visual Studio Code

![Screenshot](https://raw.githubusercontent.com/c2d7fa/vscode-parchment-light/master/screenshot.png)

*Parchment* is a family of four themes for Visual Studio Code that makes limited use of colors for syntax highlighting. Comments are highlighted to stand out, and some colors are used in places where they make sense – for example in diffs. The themes are:

- Parchment Codex – light color theme with a soft paper-like background color
- Parchment Digitized – variant of Codex with a harsher grey
- Parchment Candlelight – dark variant of Codex
- Parchment Starlight – dark variant of Digitized 

Inspired in part by [Your syntax highlighter is wrong](https://jameshfisher.com/2014/05/11/your-syntax-highlighter-is-wrong/).

## Building

The code generating the theme is written in Python, not JavaScript, so you'll need to build it before installing it.

Run `pip install hsluv`, and then run `./build.sh`. This will build the extension into the `extension/` folder.

To install the built extension, run the command *Developer: Install extension from location...* in Visual Studio Code, and then select the `extension/` folder.