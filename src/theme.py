output = """
{
  "name": "basic-light",
  "type": "light",
  "colors": {
    "editor.background": "#fcf9f6",
    "editor.foreground": "#484240",
    "widget.shadow": "#e0ddd9",
    "editorLineNumber.foreground": "#dad7d6",
    "editorLineNumber.activeForeground": "#b4afae",
    "editorWhitespace.foreground": "#48424018",
    "editorRuler.foreground": "#48424018",

    // Highlights
    "editorCursor.foreground": "#a8323c",
    "selection.background": "#e7dbcc",
    "editor.selectionBackground": "#e7dbcc",
    "editor.selectionForeground": "#645d53",
    "editor.selectionHighlightBackground": "#e7dbcc80",
    "editor.wordHighlightBackground": "#e7dbcc80",
    "editor.hoverHighlightBackground": "#e7dbcc80",

    // Lists
    "list.inactiveSelectionBackground": "#e7dbcc80",

    // Side bar
    "sideBar.background": "#f0eeec",
    "sideBarSectionHeader.background": "#e2e0dd",

    // Editor groups and tabs
    "editorGroupHeader.tabsBackground": "#f0eeec",
    "tab.inactiveBackground": "#f0eeec",
    "tab.activeBackground": "#f0eeec",
    "tab.border": "#00000000",
    "tab.inactiveForeground": "#b4afae",
    "tab.activeBorder": "#484240",
    "tab.activeForeground": "#484240",

    // Activity bar
    "activityBar.background": "#e2e0dd",
    "activityBar.inactiveForeground": "#b4afae",
    "activityBar.foreground": "#817b78",
    "activityBarBadge.background": "#d8b2b5",
    "activityBarBadge.foreground": "#473839",

    // Status bar
    "statusBar.background": "#e2e0dd",
    "statusBar.foreground": "#817b78"
  },
  "tokenColors": [
    {
      "scope": "comment",
      "settings": {
        "foreground": "#7c6e8b",
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
        "foreground": "#a7a4a4"
      }
    },
    {
      "scope": "punctuation.terminator",
      "settings": {
        "foreground": "#a7a4a4"
      }
    },
    {
      "scope": "string",
      "settings": {
        "foreground": "#807c8a",
        "fontStyle": "italic"
      }
    }
  ]
}
"""

print(output)
