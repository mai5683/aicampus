from matplotlib import font_manager

fonts = font_manager.fontManager.ttflist

for name in sorted(set(font.name for font in fonts)):
    print(name)

