import json
from hsluv import hsluv_to_hex

def hsl(h, s, l):
  return hsluv_to_hex([h, s, l])

transparent = "#00000000"

# Please excuse the somewhat nonsensical naming scheme. I got tired of renaming
# colors, and we should probably clean these up anyway.

grey1 = hsl(32.0, 8.1, 28.5)
grey2 = hsl(60.3, 19.9, 39.9)
grey4 = hsl(39.9, 6.1, 52.1)
grey480 = hsl(12.2, 1.8, 67.6)
grey5 = hsl(25.5, 3.6, 71.8)
grey6 = hsl(33.0, 5.3, 86.2)
grey6b = hsl(52.0, 20.9, 87.6)
grey650 = hsl(63.0, 4.9, 89.3)
grey7 = hsl(58.3, 26.5, 88.0)
grey8 = hsl(55.2, 9.6, 94.2)
grey9 = "#e7dbcc80"
grey10 = "#48424018"
grey11 = hsl(48.9, 28.6, 96.1)
grey12 = hsl(55.1, 45.6, 98.1)

hl0 = hsl(39.9, 6.1, 52.1)
hl1 = hsl(9.4, 69.1, 39.5)
hl2 = hsl(6.9, 37.2, 75.9)
hl210 = hsl(7.0, 51.2, 76.4)
hl11 = hsl(7.3, 100.0, 96.0)

alt1 = hsl(285.1, 16.8, 48.6) # Comments
alt2 = hsl(227.4, 8.9, 52.8) # Strings

red1 = hl1
blue1 = hsl(251.5, 53.1, 37.6)
blue2 = hsl(245.0, 83.6, 46.8)

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
