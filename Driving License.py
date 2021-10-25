# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *

root=Tk()

root.title("driving license")

root.geometry("400x400")

root.configure(bg="white")
canvas=Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 400, 60, fill="blue")
canvas.create_rectangle(0, 340, 400, 400, fill="blue")

label_heading=canvas.create_text(180, 90, font=('Times', '24', 'bold italic'), text="Driving License")
label_name_tag=canvas.create_text(40, 165, font=('Times', '18', 'bold italic'), text="Name: ")
label_grade_tag=canvas.create_text(40, 205, font=('Times', '18', 'bold italic'), text="Address: ")
label_subject_tag=canvas.create_text(50, 250, font=('Times', '18', 'bold italic'), text="Authorisation to drive vehicles: ")

label_name=Label(root)
label_grade=Label(root)
label_subjects=Label(root)

def my_card_details():
    name="Anonymous"
    grade="Disneyland, " "Honk kong"
    subject=["Two, ","Four"]
    
    label_name['text']=name
    label_grade['text']=grade
    label_subjects['text']=subject
    
button1=Button(root, text="Show my ID card",command=my_card_details)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 310, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(140, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(290, 252, anchor=CENTER, window=label_subjects)








canvas.pack()

root.mainloop()