import webbrowser
def BMI_calculation(weight, height):
    try:
        score = weight / ((height/100) ** 2)
        if score < 18.5:
            return "Underweight", score
        elif 18.5 <= score < 25:
            return "Normal weight", score
        elif 25 <= score < 30:
            return "Overweight",  score
        else:
            return "Obesity", score
    except ZeroDivisionError:
        return "Invalid Input", None
    except TypeError:
        return "Invalid Input", None
def show_BMI():
    name = name_entry.get()
    try:

        BMI_result, score = BMI_calculation(float(weight_entry.get()),float(height_entry.get()))
    except ValueError or ZeroDivisionError:
        BMI_result = "Invalid Input"
        score = None
    show_result = Label(window, textvariable=t, font = 'Consolas 12')
    show_result.place(relx=0.5, rely=0.56, anchor=CENTER)


    information = Button(window, textvariable=v, font = 'Consolas 12', bg='blue', fg='white', activebackground='blue')
    information.place(relx=0.5, rely=0.645, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.73, anchor=CENTER)
    
    if BMI_result == "Underweight":
        t.set(f"{name.capitalize()}'s BMI is {BMI_result} with a score of {score:.2f}")
        v.set(f"Click for more information about {BMI_result}")
        information.config(command=open_link_under_weight)

    elif BMI_result == "Overweight" or BMI_result == "Obesity":
        t.set(f"{name.capitalize()}'s BMI is {BMI_result} with a score of {score:.2f}")
        v.set(f'Click for more information about {BMI_result}')
        information.config(command=open_link_over_weight)

    elif BMI_result == "Normal weight":
        t.set(f"{name.capitalize()}'s BMI is {BMI_result} with a score of {score:.2f}")
        
        v.set("You are healthy (Don't click!)")
        information.config(command=normal_weight)
    else: 
        v.set('Exit')
        information.config(bg='red', fg= 'white', activebackground='red', command=window.quit, width=5)
        t.set("Invalid Input")
        exit_button.place_forget()
        
    
    
def open_link_under_weight():
    webbrowser.open("https://www.nhs.uk/conditions/malnutrition/treatment/")

def open_link_over_weight():
    webbrowser.open("https://www.nhs.uk/live-well/healthy-weight/12-tips-to-help-you-lose-weight/")

def normal_weight():
    webbrowser.open('https://youtu.be/xvFZjo5PgG0?si=-W8XacWr20GUW_r1')

from tkinter import *
window = Tk()
window.geometry("700x420")
window.title("BMI Calculator")

t=StringVar()
v=StringVar()

welcome = Label(window, text="Welcome to BMI Calculation", font="Consolas 15 bold")
welcome.place(relx=0.5, rely=0.05, anchor=CENTER) 

label = Label(window, text="Enter your height in cm and weight in kg to get you BMI result", font = 'Consolas 12')
label.place(relx=0.5, rely=0.12, anchor=CENTER)

name = Label(window, text="Name: ", font = 'Consolas 12')
name.place(x=100, y=70)

Height = Label(window, text="Height in cm: ", font = 'Consolas 12')
Height.place(x=80, y=100)

Weight = Label(window, text="Weight in kg: ", font = 'Consolas 12')
Weight.place(x=80, y=130)

name_entry = Entry(window, width=20, font = 'Consolas 12')
name_entry.place(x=420, y=70)
  



  
height_entry = Entry(window, width=20, font = 'Consolas 12')
height_entry.place(x=420, y=100)

weight_entry = Entry(window, width=20, font = 'Consolas 12')
weight_entry.place(x=420, y=130)

calculate_button = Button(window, text="Calculate", font = 'Consolas 12', command=show_BMI, bg='green', fg= 'white', activebackground='green')
calculate_button.place(relx=0.5, rely=0.475, anchor=CENTER)

exit_button = Button(window, text="Exit", font = 'Consolas 12', bg='red', fg= 'white', activebackground='red', command=window.quit, width=5)
exit_button.place(relx=0.5, rely=0.645, anchor=CENTER)

window.resizable(False, False)
window.mainloop()