import json

transparent = "#00000000"

# Please excuse the somewhat nonsensical naming scheme. I got tired of renaming
# colors, and we should probably clean these up anyway.

grey1 = "#484240"
grey2 = "#645d53"
grey4 = "#817b78"
grey480 = "#a7a4a4"
grey5 = "#b4afae"
grey6 = "#dad7d6"
grey6b = "#e4dad1"
grey650 = "#e2e0dd"
grey7 = "#e7dbcc"
grey8 = "#f0eeec"
grey9 = "#e7dbcc80"
grey10 = "#48424018"
grey11 = "#f7f3f0"
grey12 = "#fcf9f6"

hl0 = "#817b78"
hl1 = "#a8323c"
hl2 = "#d8b2b5"
hl210 = "#e2b0b4"
hl11 = "#fff0f1"

alt1 = "#7c6e8b" # Comments
alt2 = "#807c8a" # Strings

red1 = hl1
blue1 = "#425980" 
blue2 = "#3273aa"

# See https://code.visualstudio.com/api/references/theme-color.

colors = {
  "editor.background": grey12,
  "editor.foreground": grey1,
  "editorLineNumber.foreground": grey6,
  "editorLineNumber.activeForeground": grey5,
  "editorWhitespace.foreground": grey10,
  "editorRuler.foreground": grey10,

  # Base colors
  "focusBorder": hl2,
  "foreground": grey1,
  "widget.shadow": grey7,
  "selection.background": grey7,
  "descriptionForeground": grey4,
  "errorForeground": red1,
  "icon.foreground": grey4,

  # Window border
  "window.activeBorder": grey10,
  "window.inactiveBorder": grey10,

  # Text colors
  "textBlockQuote.background": grey10,
  "textBlockQuote.border": grey8,
  "textCodeBlock.background": grey10,
  "textLink.activeForeground": blue2,
  "textLink.foreground": blue1,
  "textPreformat.foreground": grey2,
  "textSeparator.foreground": grey4,

  # Button control
  "button.background": hl1,
  "button.foreground": hl11,
  "button.hoverBackground": hl210,
  "checkbox.background": grey10,
  "checkbox.foreground": grey2,
  "checkbox.border": grey8,

  # Dropdown control
  "dropdown.background": grey10,
  "dropdown.listBackground": grey10,
  "dropdown.border": grey8,
  "dropdown.foreground": grey1,

  # Highlights
  "editorCursor.foreground": hl1,
  "editor.selectionBackground": grey7,
  "editor.selectionForeground": grey2,
  "editor.selectionHighlightBackground": grey9,
  "editor.wordHighlightBackground": grey9,
  "editor.hoverHighlightBackground": grey9,

  # Lists
  "list.activeSelectionBackground": grey6b,
  "list.activeSelectionForeground": grey1,
  "list.dropBackground": grey8,
  "list.focusBackground": grey6b,
  "list.focusForeground": grey1,
  "list.highlightForeground": hl1,
  "list.hoverBackground": grey9,
  "list.hoverForeground": grey1,
  "list.inactiveSelectionBackground": grey9,
  "list.inactiveSelectionForeground": grey1,
  "list.inactiveFocusBackground": grey9,

  # Editor widget
  "editorWidget.foreground": grey2,
  "editorWidget.background": grey11,
  "editorWidget.border": transparent,
  "editorSuggestWidget.highlightForeground": hl1,
  "editorSuggestWidget.selectedBackground": grey6b,

  # Side bar
  "sideBar.background": grey8,
  "sideBarSectionHeader.background": grey650,

  # Editor groups and tabs
  "editorGroupHeader.tabsBackground": grey8,
  "tab.inactiveBackground": grey8,
  "tab.activeBackground": grey8,
  "tab.border": transparent,
  "tab.inactiveForeground": grey5,
  "tab.activeBorder": grey1,
  "tab.activeForeground": grey1,

  # Activity bar
  "activityBar.background": grey650,
  "activityBar.inactiveForeground": grey5,
  "activityBar.foreground": grey4,
  "activityBarBadge.background": hl2,
  "activityBarBadge.foreground": hl0,

  # Status bar
  "statusBar.background": grey650,
  "statusBar.foreground": grey4
}

token_colors = [
  {
    "scope": "comment",
    "settings": {
      "foreground": alt1,
      "fontStyle": "bold"
    }
  },
  {
    "scope": "keyword",
    "settings": {
      "fontStyle": "bold"
    }
  },
  {
    "scope": "storage",
    "settings": {
      "fontStyle": "bold"
    }
  },
  {
    "scope": "entity.name.type",
    "settings": {
      "fontStyle": "italic"
    }
  },
  {
    "scope": "punctuation.separator",
    "settings": {
      "foreground": grey480
    }
  },
  {
    "scope": "punctuation.terminator",
    "settings": {
      "foreground": grey480
    }
  },
  {
    "scope": "string",
    "settings": {
      "foreground": alt2,
      "fontStyle": "italic"
    }
  }
]

print(json.dumps({"name": "basic-light", "type": "light", "colors": colors, "tokenColors": token_colors}, indent=2))
