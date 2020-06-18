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
grey650 = "#e2e0dd"
grey7 = "#e7dbcc"
grey8 = "#f0eeec"
grey9 = "#e7dbcc80"
grey10 = "#48424018"
grey12 = "#fcf9f6"

hl0 = "#817b78"
hl1 = "#a8323c"
hl2 = "#d8b2b5"

alt1 = "#7c6e8b" # Comments
alt2 = "#807c8a" # Strings

red0 = hl1

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
  "errorForeground": red0,
  "icon.foreground": grey4,

  # Window border
  "window.activeBorder": grey10,
  "window.inactiveBorder": grey10,

  # Highlights
  "editorCursor.foreground": hl1,
  "editor.selectionBackground": grey7,
  "editor.selectionForeground": grey2,
  "editor.selectionHighlightBackground": grey9,
  "editor.wordHighlightBackground": grey9,
  "editor.hoverHighlightBackground": grey9,

  # Lists
  "list.inactiveSelectionBackground": grey9,

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
