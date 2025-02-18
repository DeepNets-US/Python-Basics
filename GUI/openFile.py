import easygui as eg

# File Open Box
file = eg.fileopenbox(
    title="Select a file"
)
print(file)
