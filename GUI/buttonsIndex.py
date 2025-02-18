import easygui as eg

# Add the button box
user_selection = eg.indexbox(
    msg='What is your fav color?',
    title='Choose a color',
    choices=('Red', 'Yellow', 'Blue', 'Cyan')
)
print(f'So your fav color is {user_selection}, wow.... that\'s my fav too!!')

