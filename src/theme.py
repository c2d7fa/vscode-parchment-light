import sys

import json
from hsluv import hsluv_to_hex

variant = sys.argv[1] if len(sys.argv) > 1 else "light"
is_light = variant == "light" or variant == "digitized"
is_brown = variant == "light" or variant == "candlelight"

def hsl(h, s, l):
  if is_light:
    return hsluv_to_hex([h, s, l])
  else:
    m = {
      20: 15,    25: 20,    30: 25,
      35: 30,    40: 35,    45: 40,
      50: 45,    60: 55,    65: 60,
      70: 65,    75: 70,    80: 75,
      85: 80,    90: 85,    93: 88,
      95: 90,    98: 92,
    }
    if not l in m:
      sys.stderr.write("Warning: Unknown dark lightness " + str(l) + "\n")
    return hsluv_to_hex([h, s, 100 - (m[l] if l in m else l)])

def brown(l):
  if not is_brown:
    return hsl(45, 0, l)
  elif is_light:
    return hsl(45, 25, l)
  else:
    return hsl(45, 50, l)

trans1 = "#00000000"
trans2 = brown(20) + "10"
trans3 = brown(20) + "20"
trans4 = brown(20) + "38"

# Red highlight colors
hl1 = hsl(10, 70, 40)
hl2 = hsl(10, 70, 50)
hl4 = hsl(10, 70, 95)

# Weak red highlight color
whl = hsl(10, 40, 75)

comment = hsl(285 if not is_brown else 10, 30 if is_light else 20, 45) # Comments
minimap_highlight = hsl(160, 30, 80) # Highlight background

red = hl1
blue = hsl(250, 50, 35)
blue_lighter = hsl(250, 50, 45)

diff_modified = hsl(285, 50, 70)
diff_deleted = hsl(250, 50, 70)
diff_added = hsl(350, 50, 70)
diff_modified_fg = hsl(285, 50, 40)
diff_deleted_fg = hsl(250, 50, 40)
diff_added_fg = hsl(350, 50, 40)
diff_submodule_fg = hsl(90, 50, 40)

string = brown(35)

debugging_foreground = hsl(200, 35, 40)
debugging_border = hsl(200, 10, 75)
debugging_background = hsl(200, 10, 80)

background = brown(98)
foreground = brown(20)

# See https://code.visualstudio.com/api/references/theme-color.

colors = {
  # Editor colors
  "editor.background": background,
  "editor.foreground": foreground,
  "editorLineNumber.foreground": brown(80),
  "editorLineNumber.activeForeground": brown(50),
  "editorWhitespace.foreground": brown(90), # modified
  "editorRuler.foreground": brown(90),
  "editorLink.activeForeground": blue_lighter,

  "editorGutter.modifiedBackground": diff_modified,
  "editorGutter.addedBackground": diff_added,
  "editorGutter.deletedBackground": diff_deleted,

  # Base colors
  "focusBorder": whl,
  "foreground": foreground,
  "widget.shadow": trans2,
  "selection.background": brown(70),
  "descriptionForeground": brown(40),
  "errorForeground": red,
  "icon.foreground": brown(40),

  # Window border
  "window.activeBorder": brown(90),
  "window.inactiveBorder": brown(90),

  # Text colors
  "textBlockQuote.background": brown(90),
  "textBlockQuote.border": brown(70),
  "textCodeBlock.background": brown(90),
  "textLink.activeForeground": blue_lighter,
  "textLink.foreground": blue,
  "textPreformat.foreground": brown(30),
  "textSeparator.foreground": brown(80),

  # Button control
  "button.background": hl1,
  "button.foreground": hl4,
  "button.hoverBackground": hl2,
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
  "editorWidget.border": trans1,
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
  "tab.border": trans1,
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
  "activityBarBadge.background": whl,
  "activityBarBadge.foreground": hl1,

  # Status bar
  "statusBar.background": brown(90),
  "statusBar.foreground": brown(50),
  "statusBar.border": brown(80),
  "statusBar.noFolderBackground": brown(90),
  "statusBar.noFolderForeground": brown(50),
  "statusBar.noFolderBorder": brown(80),
  "statusBar.debuggingBackground": debugging_background,
  "statusBar.debuggingForeground": string,
  "statusBar.debuggingBorder": debugging_border,
  "statusBarItem.hoverBackground": brown(85),

  # Minimap
  "minimap.findMatchHighlight": minimap_highlight,
  "minimap.selectionHighlight": brown(90),
  "minimap.errorHighlight": red,
  "minimap.warningHighlight": red,
  "minimapSlider.background": trans2,
  "minimapSlider.hoverBackground": trans3,
  "minimapSlider.activeBackground": trans4,

  "minimapGutter.modifiedBackground": diff_modified,
  "minimapGutter.addedBackground": diff_added,
  "minimapGutter.deletedBackground": diff_deleted,

  # Git colors
  "gitDecoration.addedResourceForeground": diff_added_fg,
  "gitDecoration.modifiedResourceForeground": diff_modified_fg,
  "gitDecoration.deletedResourceForeground": diff_deleted_fg,
  "gitDecoration.untrackedResourceForeground": brown(50),
  "gitDecoration.ignoredResourceForeground": brown(70),
  "gitDecoration.conflictingResourceForeground": red,
  "gitDecoration.submoduleResourceForeground": diff_submodule_fg,

  # Settings editor colors
  "settings.modifiedItemIndicator": diff_modified,

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
  "terminal.ansiBrightWhite": foreground,
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
      "foreground": comment,
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
      "foreground": string,
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
    # E.g. parentheses in TypeScript; like punctuation
    "scope": "meta.brace",
    "settings": {
      "foreground": brown(75),
      "fontStyle": "bold"
    }
  },

  # JSON and YAML
  {
    "scope": "string.unquoted.plain.out.yaml",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "normal"
    }
  },
  {
    "scope": "string.quoted.double.yaml",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "normal"
    }
  },
  {
    "scope": "string.quoted.double.json",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "normal"
    }
  },
  {
    "scope": "constant.numeric.json",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "constant.numeric.integer.yaml",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "constant.numeric.float.yaml",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "constant.language.json",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "constant.language.boolean.yaml",
    "settings": {
      "foreground": brown(50),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "support.type.property-name.json",
    "settings": {
      "foreground": brown(40),
      "fontStyle": "bold"
    }
  },
  {
    "scope": "entity.name.tag.yaml",
    "settings": {
      "foreground": brown(40),
      "fontStyle": "bold"
    }
  },

  # Markup (e.g. Markdown)
  {
    "scope": "markup.heading",
    "settings": {
      "fontStyle": "bold"
    }
  },
  {
    # Inline code
    "scope": "markup.inline",
    "settings": {
      "foreground": string
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
  },
  {
    "scope": "markup.quote",
    "settings": {
      "foreground": string,
      "fontStyle": "italic"
    }
  },
  {
    "scope": "markup.raw.block",
    "settings": {
      "foreground": string
    }
  },
  {
    "scope": "markup.fenced_code",
    "settings": {
      "foreground": string
    }
  },
  {
    "scope": "fenced_code.block.language",
    "settings": {
      "foreground": brown(60)
    }
  }
]

print(json.dumps({"type": "light", "colors": colors, "tokenColors": token_colors}, indent=2))
