import json
from hsluv import hsluv_to_hex

def hsl(h, s, l):
  return hsluv_to_hex([h, s, l])

transparent = "#00000000"

# Please excuse the somewhat nonsensical naming scheme. I got tired of renaming
# colors, and we should probably clean these up anyway.

grey1 = hsl(45, 6, 30)
grey2 = hsl(45, 20, 40)
grey4 = hsl(45, 6, 50)
grey480 = hsl(45, 6, 65)
grey5 = hsl(45, 6, 70)
grey6 = hsl(45, 6, 85)
grey6b = hsl(45, 20, 85)
grey650 = hsl(45, 6, 87)
grey7 = hsl(45, 30, 90)
grey9 = hsl(45, 10, 95)
grey10 = hsl(45, 20, 96)
grey11 = hsl(45, 30, 96)
grey12 = hsl(45, 45, 98)

hl0 = hsl(10, 6, 50)
hl1 = hsl(10, 70, 40)
hl150 = hsl(10, 70, 50)
hl2 = hsl(10, 40, 75)
hl11 = hsl(10, 70, 95)

alt1 = hsl(285, 15, 45) # Comments
alt2 = hsl(250, 8, 50) # Strings

red1 = hl1
blue1 = hsl(250, 50, 35)
blue2 = hsl(250, 80, 45)

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
  "textBlockQuote.border": grey9,
  "textCodeBlock.background": grey10,
  "textLink.activeForeground": blue2,
  "textLink.foreground": blue1,
  "textPreformat.foreground": grey2,
  "textSeparator.foreground": grey4,

  # Button control
  "button.background": hl1,
  "button.foreground": hl11,
  "button.hoverBackground": hl150,
  "checkbox.background": grey10,
  "checkbox.foreground": grey2,
  "checkbox.border": grey9,

  # Dropdown control
  "dropdown.background": grey10,
  "dropdown.listBackground": grey10,
  "dropdown.border": grey9,
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
  "list.dropBackground": grey9,
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
  "sideBar.background": grey9,
  "sideBarSectionHeader.background": grey650,

  # Editor groups and tabs
  "editorGroupHeader.tabsBackground": grey9,
  "tab.inactiveBackground": grey9,
  "tab.activeBackground": grey9,
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
