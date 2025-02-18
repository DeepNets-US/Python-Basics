import easygui as eg

# Take user input
num = eg.enterbox(
    msg='Enter a number',
    title='Number user input'
)
try:
    num = float(num)
except:
    raise ValueError(f'Please enter a number not {num}')

# Return the square of the value
msg = eg.msgbox(
        msg=f'The square of {num} is : {num**2}',
        title='The output'
)



