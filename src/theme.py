import json
from hsluv import hsluv_to_hex

def hsl(h, s, l):
  return hsluv_to_hex([h, s, l])

def sl(s, l):
  return hsl(45, s, l)

def brown(l):
  return sl(20, l)

transparent = "#00000000"

trans2 = sl(50, 20) + "10"
trans3 = sl(50, 20) + "20"
trans4 = sl(50, 20) + "38"

hl0 = hsl(10, 6, 50)
hl1 = hsl(10, 70, 40)
hl150 = hsl(10, 70, 50)
hl2 = hsl(10, 40, 75)
hl11 = hsl(10, 70, 95)

alt1 = hsl(285, 15, 45) # Comments
alt3 = hsl(160, 30, 80) # Highlight background

red1 = hl1
blue1 = hsl(250, 50, 35)
blue2 = hsl(250, 80, 45)
purple1 = hsl(285, 50, 40)
green1 = hsl(90, 50, 40)
pink1 = hsl(350, 50, 40)

purple2 = hsl(285, 50, 70)
blue3 = hsl(250, 50, 70)
pink2 = hsl(350, 50, 70)

cyan0 = hsl(200, 35, 40)

# See https://code.visualstudio.com/api/references/theme-color.

colors = {
  # Editor colors
  "editor.background": brown(98),
  "editor.foreground": brown(20),
  "editorLineNumber.foreground": brown(80),
  "editorLineNumber.activeForeground": brown(50),
  "editorWhitespace.foreground": brown(90), # modified
  "editorRuler.foreground": brown(90),
  "editorLink.activeForeground": blue2,

  "editorGutter.modifiedBackground": purple2,
  "editorGutter.addedBackground": pink2,
  "editorGutter.deletedBackground": blue3,

  # Base colors
  "focusBorder": hl2,
  "foreground": brown(20),
  "widget.shadow": trans2,
  "selection.background": brown(70),
  "descriptionForeground": brown(40),
  "errorForeground": red1,
  "icon.foreground": brown(40),

  # Window border
  "window.activeBorder": brown(90),
  "window.inactiveBorder": brown(90),

  # Text colors
  "textBlockQuote.background": brown(90),
  "textBlockQuote.border": brown(70),
  "textCodeBlock.background": brown(90),
  "textLink.activeForeground": blue2,
  "textLink.foreground": blue1,
  "textPreformat.foreground": brown(30),
  "textSeparator.foreground": brown(80),

  # Button control
  "button.background": hl1,
  "button.foreground": hl11,
  "button.hoverBackground": hl150,
  "checkbox.background": brown(95),
  "checkbox.foreground": brown(40),
  "checkbox.border": brown(95),

  # Dropdown control
  "dropdown.background": brown(95),
  "dropdown.listBackground": brown(95),
  "dropdown.border": brown(95),
  "dropdown.foreground": brown(30),

  # Highlights
  "editorCursor.foreground": hl1,
  "editor.selectionBackground": brown(90),
  "editor.selectionForeground": brown(40),
  "editor.selectionHighlightBackground": brown(90),
  "editor.wordHighlightBackground": brown(90),
  "editor.hoverHighlightBackground": brown(90),

  # Lists
  "list.activeSelectionBackground": brown(90),
  "list.activeSelectionForeground": brown(30),
  "list.dropBackground": brown(95),
  "list.focusBackground": brown(90),
  "list.focusForeground": brown(30),
  "list.highlightForeground": hl1,
  "list.hoverBackground": brown(95),
  "list.hoverForeground": brown(30),
  "list.inactiveSelectionBackground": brown(95),
  "list.inactiveSelectionForeground": brown(30),
  "list.inactiveFocusBackground": brown(95),

  # Editor widget
  "editorWidget.foreground": brown(40),
  "editorWidget.background": brown(98),
  "editorWidget.border": transparent,
  "editorSuggestWidget.highlightForeground": hl1,
  "editorSuggestWidget.selectedBackground": brown(85),

  # Side bar
  "sideBar.background": brown(95),
  "sideBarSectionHeader.foreground": brown(50),
  "sideBarSectionHeader.background": brown(90),
  "sideBar.border": brown(90),

  # Editor groups and tabs
  "editorGroup.border": brown(90),
  "editorGroupHeader.tabsBackground": brown(95),
  "editorGroupHeader.border": brown(85),
  "editorGroupHeader.tabsBorder": brown(85),
  "tab.inactiveBackground": brown(95),
  "tab.border": transparent,
  "tab.inactiveForeground": brown(70),
  "tab.activeBackground": brown(93),
  "tab.activeBorder": brown(30),
  "tab.activeForeground": brown(30),

  # Breadcrumbs colors
  "breadcrumb.foreground": brown(70),
  "breadcrumb.background": brown(93),
  "breadcrumb.focusForeground": brown(50),

  # Title bar colors
  "titleBar.activeBackground": brown(85),
  "titleBar.activeForeground": brown(50),
  "titleBar.inactiveBackground": brown(85),
  "titleBar.inactiveForeground": brown(70),
  "titleBar.border": brown(80),

  # Activity bar
  "activityBar.background": brown(90),
  "activityBar.inactiveForeground": brown(70),
  "activityBar.foreground": brown(50),
  "activityBar.border": brown(80),
  "activityBarBadge.background": hl2,
  "activityBarBadge.foreground": hl0,

  # Status bar
  "statusBar.background": brown(90),
  "statusBar.foreground": brown(50),
  "statusBar.border": brown(80),

  # Minimap
  "minimap.findMatchHighlight": alt3,
  "minimap.selectionHighlight": brown(90),
  "minimap.errorHighlight": red1,
  "minimap.warningHighlight": red1,
  "minimapSlider.background": trans2,
  "minimapSlider.hoverBackground": trans3,
  "minimapSlider.activeBackground": trans4,

  "minimapGutter.modifiedBackground": purple2,
  "minimapGutter.addedBackground": pink2,
  "minimapGutter.deletedBackground": blue3,

  # Git colors
  "gitDecoration.addedResourceForeground": pink1,
  "gitDecoration.modifiedResourceForeground": purple1,
  "gitDecoration.deletedResourceForeground": blue1,
  "gitDecoration.untrackedResourceForeground": brown(50),
  "gitDecoration.ignoredResourceForeground": brown(70),
  "gitDecoration.conflictingResourceForeground": red1,
  "gitDecoration.submoduleResourceForeground": green1,

  # Settings editor colors
  "settings.modifiedItemIndicator": purple2,

  # Quick picker
  "pickerGroup.border": brown(80),
  "pickerGroup.foreground": brown(60),

  # Integrated Terminal colors
  "terminal.background": brown(95),
  "terminal.foreground": brown(25),
  "terminal.ansiBrightBlack": brown(85),
  "terminal.ansiBlack": brown(75),
  "terminal.ansiBrightBlue": hsl(250, 55, 50),
  "terminal.ansiBlue": hsl(250, 55, 40),
  "terminal.ansiBrightCyan": hsl(200, 55, 50),
  "terminal.ansiCyan": hsl(200, 55, 40),
  "terminal.ansiBrightGreen": hsl(110, 55, 50),
  "terminal.ansiGreen": hsl(110, 55, 40),
  "terminal.ansiBrightMagenta": hsl(285, 55, 50),
  "terminal.ansiMagenta": hsl(285, 55, 40),
  "terminal.ansiBrightRed": hsl(10, 55, 50),
  "terminal.ansiRed": hsl(10, 55, 40),
  "terminal.ansiBrightWhite": brown(20),
  "terminal.ansiWhite": brown(25),
  "terminal.ansiBrightYellow": hsl(60, 55, 50),
  "terminal.ansiYellow": hsl(60, 55, 40),
  "terminal.selectionBackground": brown(70),
  "terminalCursor.background": brown(90),
  "terminalCursor.foreground": hl1,
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
      "foreground": brown(65)
    }
  },
  {
    "scope": "punctuation.terminator",
    "settings": {
      "foreground": brown(65)
    }
  },
  {
    "scope": "string",
    "settings": {
      "foreground": cyan0,
      "fontStyle": "italic"
    }
  },
  {
    "scope": "punctuation",
    "settings": {
      "foreground": brown(75),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "markup.heading",
    "settings": {
      "fontStyle": "bold"
    }
  },
  {
    # Inline code, e.g. in Markdown.
    "scope": "markup.inline",
    "settings": {
      "foreground": cyan0,
      "fontStyle": "italic"
    }
  },
  {
    "scope": "markup.italic",
    "settings": {
      "fontStyle": "italic"
    }
  },
  {
    "scope": "markup.bold",
    "settings": {
      "fontStyle": "bold"
    }
  }
]

print(json.dumps({"type": "light", "colors": colors, "tokenColors": token_colors}, indent=2))
