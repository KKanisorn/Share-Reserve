import tkinter as tk
from turtledemo.penrose import start

# from shareReserve import ClickWithStartStopTime
from shareReserve import getCurrentTime

mode = 0


# def hideFirstPageElement():
 #     StartStopButton.pack_forget()
#     global mode
#     mode = 1
#     startTimeInput = tk.Entry(root, width=20)
#     startTimeInput.pack(side=tk.TOP, anchor=tk.NW)
#     stopTimeInput = tk.Entry(root, width=20)
#     stopTimeInput.pack(side=tk.TOP)





root = tk.Tk()
root.title("my title")
root.geometry('500x400')
root.resizable(False, False)
# root.configure(background='black')
tk.Label(root, text="Start Time").pack(pady=5, side=tk.LEFT)
start_entry = tk.Entry(root, width=10)
start_entry.insert(0, getCurrentTime())
start_entry.pack(pady=5, side=tk.LEFT)


tk.Label(root, text="Stop Time").pack(pady=5, side=tk.LEFT)
stop_entry = tk.Entry(root, width=10)
stop_entry.insert(0, getCurrentTime())
stop_entry.pack(pady=5, side=tk.LEFT)




#	enter widgets here

root.mainloop()