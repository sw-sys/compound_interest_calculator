from tkinter import *

### INTERFACE

# objects
window = Tk()

# window properties
window.title('Interest Calculator')
window.resizable(0, 0)
window.geometry("800x200")

# grid

label1 = Label(window, relief= 'flat', width = 30)
label2 = Label(window, relief= 'flat', width = 30)
label3 = Label(window, relief= 'flat', width = 30)
label4 = Label(window, relief= 'flat', width = 30)

entry1 = Entry(window, relief= 'groove', width = 10)
entry2 = Entry(window, relief= 'groove', width = 10)
entry3 = Entry(window, relief= 'groove', width = 10)
entry4 = Entry(window, relief= 'groove', width = 10)

label10 = Label(window, relief= 'sunken', width = 60)

label1.grid(row = 1, column = 1, padx = 10, pady=5)
label2.grid(row = 2, column = 1, padx = 10, pady=5)
label3.grid(row = 3, column = 1, padx = 10, pady=5)
label4.grid(row = 4, column = 1, padx = 10, pady=5)

entry1.grid(row = 1, column = 2, padx = 10)
entry2.grid(row = 2, column = 2, padx = 10)
entry3.grid(row = 3, column = 2, padx = 10)
entry4.grid(row = 4, column = 2, padx = 10)

label10.grid(row = 1, column = 4, pady = 10, rowspan = 5)

# User entry requests and defaults
label1.configure(text='Enter deposit amount:')
label2.configure(text='Enter interest rate:')
label3.configure(text='Enter time period:')
label4.configure(text='Enter compounding frequency (years):')

# static buttons

calcBtn = Button(window, text = "Calculate")
resetBtn = Button(window, text = "Reset")
calcBtn.grid(row = 5, column= 1, pady=10)
resetBtn.grid(row = 5, column= 2, pady=10)

### DYNAMIC PROPERTIES

# calculation variables and func

# def calcInterest(principal, interest, time_period, compounding_frequency):
def calcInterest():
    principal = entry1.get()
    interest = entry2.get()
    time_period = entry3.get()
    compounding_frequency = entry4.get()
    amount = principal * (1 + (interest / compounding_frequency)) ** (compounding_frequency * time_period)
    interest_amount = amount - principal
    label10.configure(text = interest_amount)

calcBtn.configure(command = calcInterest)

# reset button
def reset():
    entry1.delete(0, END)
    entry1.insert(0, "")
    entry2.delete(0, END)
    entry2.insert(0, "")
    entry3.delete(0, END)
    entry3.insert(0, "")
    entry4.delete(0, END)
    entry4.insert(0, "")
    calcBtn.configure(state = NORMAL)
    resetBtn.configure(state = DISABLED)

resetBtn.configure(command = reset)

# sustain window
window.mainloop()

# # ## CALCULATIONS

# def calcInterest(principal, interest, time_period, frequency):
#     amount = principal * (1 + (interest / compounding_frequency)) ** (compounding_frequency * time_period)
#     interest_amount = amount - principal
#     return interest_amount

# # get user input
# principal = float(input("Enter the deposit amount: "))
# interest = float(input("Enter the interest rate: "))
# time_period = float(input("Enter the time period: "))
# compounding_frequency = float(input("Enter the compounding frequency in years: "))

# # print out
# total_interest = calcInterest(principal, interest, time_period, compounding_frequency)
# total_interest = round(total_interest, 2)

# print(f"Total interest accrued is: £ {total_interest}")