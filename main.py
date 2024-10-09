from functions import write_and_erase, write
from functions import type_remove_physical

text = []

count = 0

while True:
    count += 1
    t = input(f"Please enter line {count} text to type('exit_code' to exit): ")

    if t == "exit_code":
        break
    else:
        text.append(t)

make1 = float(input("Please enter delay between typing characters in seconds (Leave empty for 0.2s): "))
del1 = float(input("Please enter delay between erasing characters in seconds (Leave empty for 0.2s): "))
diff = float(input("Please enter time between typing and erasing in seconds (Leave empty for 1s): "))

form = input("Please enter 'real' for actual typing and 'fake' for typing in print statement: ")

if form == "real":
    brk = float(input("Please enter time to wait before starting writing process in seconds (Leave empty for 5s): "))
    for i in text:
        type_remove_physical(i, diff, make1, del1, brk)
elif form == "fake":
    for i in text:
        write_and_erase(i, diff, make1, del1)

#Do Not Copy