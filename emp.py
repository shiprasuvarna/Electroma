from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime
root=Tk()
root.title("theemporium.in")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=p.Image.open("Images\Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open("Images\Logo_Large.jpg"))
HomeAppliances1_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_1.jpg"))
HomeAppliances2_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_2.jpeg"))
HomeAppliances3_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_3.jpeg"))
HomeAppliances4_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_4.jpeg"))
HomeAppliances5_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_5.jpeg"))
HomeAppliances6_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_6.jpeg"))
HomeAppliances7_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_7.jpeg"))
HomeAppliances8_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_8.jpeg"))
HomeAppliances9_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_9.jpeg"))
HomeAppliances10_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_10.jpg"))
Televisions1_image=ptk.PhotoImage(p.Image.open("Images\Televisions_1.jpeg"))
Televisions2_image=ptk.PhotoImage(p.Image.open("Images\Televisions_2.jpeg"))
Televisions3_image=ptk.PhotoImage(p.Image.open("Images\Televisions_3.jpeg"))
Televisions4_image=ptk.PhotoImage(p.Image.open("Images\Televisions_4.jpeg"))
Televisions5_image=ptk.PhotoImage(p.Image.open("Images\Televisions_5.jpeg"))
Televisions6_image=ptk.PhotoImage(p.Image.open("Images\Televisions_6.jpeg"))
Televisions7_image=ptk.PhotoImage(p.Image.open("Images\Televisions_7.jpeg"))
Televisions8_image=ptk.PhotoImage(p.Image.open("Images\Televisions_8.jpeg"))
Televisions9_image=ptk.PhotoImage(p.Image.open("Images\Televisions_9.jpeg"))
Televisions10_image=ptk.PhotoImage(p.Image.open("Images\Televisions_10.jpeg"))
Cameraandaccessories1_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_1.jpeg"))
Cameraandaccessories2_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_2.jpeg"))
Cameraandaccessories3_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_3.jpeg"))
Cameraandaccessories4_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_4.jpeg"))
Cameraandaccessories5_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_5.jpeg"))
Cameraandaccessories6_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_6.jpeg"))
Cameraandaccessories7_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_7.jpeg"))
Cameraandaccessories8_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_8.jpeg"))
Cameraandaccessories9_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_9.jpeg"))
Cameraandaccessories10_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_10.jpeg"))
Computerandtablets1_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_1.jpeg"))
Computerandtablets2_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_2.jpeg"))
Computerandtablets3_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_3.jpeg"))
Computerandtablets4_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_4.jpeg"))
Computerandtablets5_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_5.jpeg"))
Computerandtablets6_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_6.jpeg"))
Computerandtablets7_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_7.jpeg"))
Computerandtablets8_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_8.jpeg"))
Computerandtablets9_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_9.jpeg"))
Computerandtablets10_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_10.jpeg"))
audio1_image=ptk.PhotoImage(p.Image.open("Images\audio_1.jpeg"))
audio2_image=ptk.PhotoImage(p.Image.open("Images\audio_2.jpeg"))
audio3_image=ptk.PhotoImage(p.Image.open("Images\audio_3.jpeg"))
audio4_image=ptk.PhotoImage(p.Image.open("Images\audio_4.jpeg"))
audio5_image=ptk.PhotoImage(p.Image.open("Images\audio_5.jpeg"))
audio6_image=ptk.PhotoImage(p.Image.open("Images\audio_6.jpeg"))
audio7_image=ptk.PhotoImage(p.Image.open("Images\audio_7.jpeg"))
audio8_image=ptk.PhotoImage(p.Image.open("Images\audio_8.jpeg"))
audio9_image=ptk.PhotoImage(p.Image.open("Images\audio_9.jpeg"))
audio10_image=ptk.PhotoImage(p.Image.open("Images\audio_10.jpeg"))
#HomeAppliances Variables
clicked_HomeAppliances1=StringVar()
clicked_HomeAppliances1.set("250g - Rs.93")
clicked_HomeAppliances2=StringVar()
clicked_HomeAppliances2.set("5kg – Rs.235")
clicked_HomeAppliances3=StringVar()
clicked_HomeAppliances3.set("1kg – Rs.18")
clicked_HomeAppliances4=StringVar()
clicked_HomeAppliances4.set("1L – Rs.195")
clicked_HomeAppliances5=StringVar()
clicked_HomeAppliances5.set("500g – Rs.95")
clicked_HomeAppliances6=StringVar()
clicked_HomeAppliances6.set("55g – Rs.76")
clicked_HomeAppliances7=StringVar()
clicked_HomeAppliances7.set("120g – Rs.23")
clicked_HomeAppliances8=StringVar()
clicked_HomeAppliances8.set("200g – Rs.65")
clicked_HomeAppliances9=StringVar()
clicked_HomeAppliances9.set("500g – Rs.104")
clicked_HomeAppliances10=StringVar()
clicked_HomeAppliances10.set("70g – Rs.25")
HomeAppliances_list=[]
#Televisions Variables
clicked_Televisions1=StringVar()
clicked_Televisions1.set("Aurora Blue")
clicked_Televisions2=StringVar()
clicked_Televisions2.set("Aquamarine Green")
clicked_Televisions3=StringVar()
clicked_Televisions3.set("Black")
clicked_Televisions4=StringVar()
clicked_Televisions4.set("Black")
clicked_Televisions5=StringVar()
clicked_Televisions5.set("Charcoal Grey")
clicked_Televisions6=StringVar()
clicked_Televisions6.set("Shadow Black")
clicked_Televisions7=StringVar()
clicked_Televisions7.set("Black")
clicked_Televisions8=StringVar()
clicked_Televisions8.set("Black")
clicked_Televisions9=StringVar()
clicked_Televisions9.set("Jet Black")
clicked_Televisions10=StringVar()
clicked_Televisions10.set("Blue & White")
Televisions_list=[]
#Sports and Gym variables
Cameraandaccessories_list=[]
#Computerandtablets variables
Computerandtablets_list=[]
#Appliances variables
audio_list=[]
name=Label(Heading,text="The Emporium",font="arial 20 bold italic",bg="light pink",fg="blue").grid(row=0,column=1)
tagline=Label(Heading,text="Shopping made easier!",font="magneto 16 italic",fg="gold",bg="black").grid(row=0,column=2,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=250,y=100)
label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)
def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
def HomeAppliancesCall():
    HideAllFrames()
    HomeAppliances_Label=Label(Products_frame,text="HomeAppliances",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_HomeAppliances1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances1.place(x=5,y=35,width=180,height=280)
    lf_HomeAppliances2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances2.place(x=210,y=35,width=180,height=280)
    lf_HomeAppliances3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances3.place(x=415,y=35,width=180,height=280)
    lf_HomeAppliances4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances4.place(x=620,y=35,width=180,height=280)
    lf_HomeAppliances5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances5.place(x=825,y=35,width=180,height=280)
    lf_HomeAppliances6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances6.place(x=5,y=310,width=180,height=280)
    lf_HomeAppliances7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances7.place(x=210,y=310,width=180,height=280)
    lf_HomeAppliances8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances8.place(x=415,y=310,width=180,height=280)
    lf_HomeAppliances9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances9.place(x=620,y=310,width=180,height=280)
    lf_HomeAppliances10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances10.place(x=825,y=310,width=180,height=280)
    label_HomeAppliances_1=Label(lf_HomeAppliances1,image=HomeAppliances1_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_2=Label(lf_HomeAppliances2,image=HomeAppliances2_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_3=Label(lf_HomeAppliances3,image=HomeAppliances3_image,bd=2).grid(row=0,column=0,padx=13)
    label_HomeAppliances_4=Label(lf_HomeAppliances4,image=HomeAppliances4_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_5=Label(lf_HomeAppliances5,image=HomeAppliances5_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_6=Label(lf_HomeAppliances6,image=HomeAppliances6_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_7=Label(lf_HomeAppliances7,image=HomeAppliances7_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_8=Label(lf_HomeAppliances8,image=HomeAppliances8_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_9=Label(lf_HomeAppliances9,image=HomeAppliances9_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_10=Label(lf_HomeAppliances10,image=HomeAppliances10_image,bd=2).grid(row=0,column=0)
    name_HomeAppliances1=Label(lf_HomeAppliances1,text="Kellogg's Corn Flakes Original",font="arial 9").grid(row=1,column=0)
    name_HomeAppliances2=Label(lf_HomeAppliances2,text="Aashirwaad Superior Atta",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_HomeAppliances3=Label(lf_HomeAppliances3,text="Tata Iodized Salt",font="arial 9",justify="center").grid(row=1,column=0)
    name_HomeAppliances4=Label(lf_HomeAppliances4,text="Safal Filtered Groundnut Oil",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_HomeAppliances5=Label(lf_HomeAppliances5,text="24 Mantra Organic Toor Dal",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_HomeAppliances6=Label(lf_HomeAppliances6,text="Dairy Milk Silk Fruit & Nut",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_HomeAppliances7=Label(lf_HomeAppliances7,text="Yippee Noodles Magic Masala",font="arial 9",justify="center").grid(row=1,column=0)
    name_HomeAppliances8=Label(lf_HomeAppliances8,text="Kissan Mixed Fruit Jam",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_HomeAppliances9=Label(lf_HomeAppliances9,text="Mother's Recipe Mango Pickle",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_HomeAppliances10=Label(lf_HomeAppliances10,text="Parle's Cream & Onion Wafers",font="arial 9",justify="center").grid(row=1,column=0)
    label_qty_HomeAppliances1=Label(lf_HomeAppliances1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances2=Label(lf_HomeAppliances2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances3=Label(lf_HomeAppliances3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances4=Label(lf_HomeAppliances4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances5=Label(lf_HomeAppliances5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances6=Label(lf_HomeAppliances6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances7=Label(lf_HomeAppliances7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances8=Label(lf_HomeAppliances8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances9=Label(lf_HomeAppliances9,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_HomeAppliances10=Label(lf_HomeAppliances10,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_HomeAppliances1=["250g – Rs.93","475g – Rs.166"]
    options_HomeAppliances2=["5kg – Rs.235","10kg – Rs.394"]
    options_HomeAppliances3=["1kg – Rs.18"]
    options_HomeAppliances4=["1L – Rs.195"]
    options_HomeAppliances5=["500g – Rs.95","1kg – Rs.165"]
    options_HomeAppliances6=["55g – Rs.76","137g – Rs.175"]
    options_HomeAppliances7=["120g – Rs.23","250g – Rs.48"]
    options_HomeAppliances8=["200g – Rs.65","500g – Rs.150","700g – Rs.215"]
    options_HomeAppliances9=["500g – Rs.104","1kg – Rs.160"]
    options_HomeAppliances10=["70g – Rs.25","150g – Rs.40"]
    global clicked_HomeAppliances1,clicked_HomeAppliances2,clicked_HomeAppliances3,clicked_HomeAppliances4,clicked_HomeAppliances5,HomeAppliances_list
    global clicked_HomeAppliances6,clicked_HomeAppliances7,clicked_HomeAppliances8,clicked_HomeAppliances9,clicked_HomeAppliances10
    drop_HomeAppliances1=OptionMenu(lf_HomeAppliances1,clicked_HomeAppliances1,*options_HomeAppliances1).place(x=30,y=212)
    drop_HomeAppliances2=OptionMenu(lf_HomeAppliances2,clicked_HomeAppliances2,*options_HomeAppliances2).place(x=30,y=212)
    drop_HomeAppliances3=OptionMenu(lf_HomeAppliances3,clicked_HomeAppliances3,*options_HomeAppliances3).place(x=30,y=212)
    drop_HomeAppliances4=OptionMenu(lf_HomeAppliances4,clicked_HomeAppliances4,*options_HomeAppliances4).place(x=30,y=212)
    drop_HomeAppliances5=OptionMenu(lf_HomeAppliances5,clicked_HomeAppliances5,*options_HomeAppliances5).place(x=30,y=212)
    drop_HomeAppliances6=OptionMenu(lf_HomeAppliances6,clicked_HomeAppliances6,*options_HomeAppliances6).place(x=30,y=212)
    drop_HomeAppliances7=OptionMenu(lf_HomeAppliances7,clicked_HomeAppliances7,*options_HomeAppliances7).place(x=30,y=212)
    drop_HomeAppliances8=OptionMenu(lf_HomeAppliances8,clicked_HomeAppliances8,*options_HomeAppliances8).place(x=30,y=212)
    drop_HomeAppliances9=OptionMenu(lf_HomeAppliances9,clicked_HomeAppliances9,*options_HomeAppliances9).place(x=30,y=212)
    drop_HomeAppliances10=OptionMenu(lf_HomeAppliances10,clicked_HomeAppliances10,*options_HomeAppliances10).place(x=30,y=212)
    def HomeAppliancesPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def HomeAppliancesQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Corn Flakes",HomeAppliancesPrice(clicked_HomeAppliances1.get()),HomeAppliancesQty(clicked_HomeAppliances1.get()),Spaces(40-len("Corn Flakes"))])
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_HomeAppliances1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_HomeAppliances1.get()+") is not added to the cart.")
    def AddG2():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Aashirwaad Atta",HomeAppliancesPrice(clicked_HomeAppliances2.get()),HomeAppliancesQty(clicked_HomeAppliances2.get()),Spaces(40-len("Aashirwaad Atta"))])
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_HomeAppliances2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_HomeAppliances2.get()+") is not added to the cart.")
    def AddG3():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Iodized Salt",HomeAppliancesPrice(clicked_HomeAppliances3.get()),HomeAppliancesQty(clicked_HomeAppliances3.get()),Spaces(40-len("Iodized Salt"))])
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_HomeAppliances3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_HomeAppliances3.get()+") is not added to the cart.")
    def AddG4():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Filtered Groundnut Oil",HomeAppliancesPrice(clicked_HomeAppliances4.get()),HomeAppliancesQty(clicked_HomeAppliances4.get()),Spaces(40-len("Filtered Groundnut Oil"))])
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_HomeAppliances4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_HomeAppliances4.get()+") is not added to the cart.")
    def AddG5():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Organic Toor Dal",HomeAppliancesPrice(clicked_HomeAppliances5.get()),HomeAppliancesQty(clicked_HomeAppliances5.get()),Spaces(40-len("Organic Toor Dal"))])
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_HomeAppliances5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_HomeAppliances5.get()+") is not added to the cart.")
    def AddG6():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Dairy Milk Silk",HomeAppliancesPrice(clicked_HomeAppliances6.get()),HomeAppliancesQty(clicked_HomeAppliances6.get()),Spaces(40-len("Dairy Milk Silk"))])
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_HomeAppliances6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_HomeAppliances6.get()+") is not added to the cart.")
    def AddG7():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Yippee Noodles",HomeAppliancesPrice(clicked_HomeAppliances7.get()),HomeAppliancesQty(clicked_HomeAppliances7.get()),Spaces(40-len("Yippee Noodles"))])
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_HomeAppliances7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_HomeAppliances7.get()+") is not added to the cart.")
    def AddG8():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Mixed Fruit Jam",HomeAppliancesPrice(clicked_HomeAppliances8.get()),HomeAppliancesQty(clicked_HomeAppliances8.get()),Spaces(40-len("Mixed Fruit Jam"))])
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_HomeAppliances8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_HomeAppliances8.get()+") is not added to the cart.")
    def AddG9():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Mango Pickle",HomeAppliancesPrice(clicked_HomeAppliances9.get()),HomeAppliancesQty(clicked_HomeAppliances9.get()),Spaces(40-len("Mango Pickle"))])
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_HomeAppliances9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_HomeAppliances9.get()+") is not added to the cart.")
    def AddG10():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Parle's Wafers",HomeAppliancesPrice(clicked_HomeAppliances10.get()),HomeAppliancesQty(clicked_HomeAppliances10.get()),Spaces(40-len("Parle's Wafers"))])
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_HomeAppliances10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_HomeAppliances10.get()+") is not added to the cart.")
    add_HomeAppliances1=Button(lf_HomeAppliances1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=60,y=245)
    add_HomeAppliances2=Button(lf_HomeAppliances2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=60,y=245)
    add_HomeAppliances3=Button(lf_HomeAppliances3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=60,y=245)
    add_HomeAppliances4=Button(lf_HomeAppliances4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=60,y=245)
    add_HomeAppliances5=Button(lf_HomeAppliances5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=60,y=245)
    add_HomeAppliances6=Button(lf_HomeAppliances6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=60,y=245)
    add_HomeAppliances7=Button(lf_HomeAppliances7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=60,y=245)
    add_HomeAppliances8=Button(lf_HomeAppliances8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=60,y=245)
    add_HomeAppliances9=Button(lf_HomeAppliances9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=60,y=245)
    add_HomeAppliances10=Button(lf_HomeAppliances10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=60,y=245)
def TelevisionsCall():
    HideAllFrames()
    Televisions_Label=Label(Products_frame,text="Televisions",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_Televisions1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions1.place(x=5,y=35,width=200,height=280)
    lf_Televisions2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions2.place(x=210,y=35,width=200,height=280)
    lf_Televisions3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions3.place(x=415,y=35,width=200,height=280)
    lf_Televisions4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions4.place(x=620,y=35,width=200,height=280)
    lf_Televisions5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions5.place(x=825,y=35,width=200,height=280)
    lf_Televisions6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions6.place(x=5,y=310,width=200,height=280)
    lf_Televisions7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions7.place(x=210,y=310,width=200,height=280)
    lf_Televisions8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions8.place(x=415,y=310,width=200,height=280)
    lf_Televisions9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions9.place(x=620,y=310,width=200,height=280)
    lf_Televisions10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions10.place(x=825,y=310,width=200,height=280)
    label_Televisions_1=Label(lf_Televisions1,image=Televisions1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_2=Label(lf_Televisions2,image=Televisions2_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_3=Label(lf_Televisions3,image=Televisions3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_4=Label(lf_Televisions4,image=Televisions4_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_5=Label(lf_Televisions5,image=Televisions5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_6=Label(lf_Televisions6,image=Televisions6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_7=Label(lf_Televisions7,image=Televisions7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Televisions_8=Label(lf_Televisions8,image=Televisions8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Televisions_9=Label(lf_Televisions9,image=Televisions9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_10=Label(lf_Televisions10,image=Televisions10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    name_Televisions1=Label(lf_Televisions1,text="Redmi Note 9 Pro(Storage:64GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Televisions2=Label(lf_Televisions2,text="OnePlus 8T 5G(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_Televisions3=Label(lf_Televisions3,text="boAt Bassheads Wired Earphones",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions4=Label(lf_Televisions4,text="JBL T460BT On-Ear Headphones",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Televisions5=Label(lf_Televisions5,text="Logitech M221 Wireless Mouse",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_Televisions6=Label(lf_Televisions6,text="HP Pavilion 15.6-inch",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions6=Label(lf_Televisions6,text="FHD Gaming Laptop",font="arial 9",justify="center").grid(row=2,column=0)
    name_Televisions6=Label(lf_Televisions6,text="Storage:1TB HDD + 256GB SSD",font="arial 9",justify="center").grid(row=3,column=0,padx=6)
    price_Televisions6=Label(lf_Televisions6,text="Price: Rs.67,900",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_Televisions7=Label(lf_Televisions7,text="Acer Aspire 5 15.6 inch Laptop",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions7=Label(lf_Televisions7,text="Intel Core i5 11th Generation",font="arial 9",justify="center").grid(row=2,column=0)
    name_Televisions7=Label(lf_Televisions7,text="Storage: 512GB SSD",font="arial 9",justify="center").grid(row=3,column=0)
    price_Televisions7=Label(lf_Televisions7,text="Price: Rs.49,990",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_Televisions8=Label(lf_Televisions8,text="OnePlus Y Series Full HD",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions8=Label(lf_Televisions8,text="LED Smart Android TV 43Y1",font="arial 9",justify="center").grid(row=2,column=0)
    price_Televisions8=Label(lf_Televisions8,text="Price: Rs.15,499  Inches: 32",font="arial 9 bold",justify="center").grid(row=3,column=0)
    name_Televisions9=Label(lf_Televisions9,text="Noise Colorfit Pro 2 Smartwatch",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_Televisions10=Label(lf_Televisions10,text="EPSON L3115 Color A4",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions10=Label(lf_Televisions10,text="All in ONE Printer",font="arial 9",justify="center").grid(row=2,column=0)
    price_Televisions10=Label(lf_Televisions10,text="Price: Rs.12,250",font="arial 9 bold",justify="center").grid(row=3,column=0)
    label_clr_Televisions1=Label(lf_Televisions1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions2=Label(lf_Televisions2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions3=Label(lf_Televisions3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions4=Label(lf_Televisions4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions5=Label(lf_Televisions5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions6=Label(lf_Televisions6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions7=Label(lf_Televisions7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions8=Label(lf_Televisions8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions9=Label(lf_Televisions9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions10=Label(lf_Televisions10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_Televisions1=["Aurora Blue","Interstellar Black","Glacier White","Champagne Gold"]
    options_Televisions2=["Aquamarine Green","Lunar Silver"]
    options_Televisions3=["Black","Forest Green","Molten Orange","Neon Lime"]
    options_Televisions4=["Black","Blue","White"]
    options_Televisions5=["Charcoal Grey","Red","Blue"]
    options_Televisions6=["Shadow Black","Fiery Red"]
    options_Televisions7=["Black"]
    options_Televisions8=["Black"]
    options_Televisions9=["Jet Black","Cherry Red","Mist Grey","Royal Blue"]
    options_Televisions10=["Blue & White"]
    global clicked_Televisions1,clicked_Televisions2,clicked_Televisions3,clicked_Televisions4,clicked_Televisions5,Televisions_list
    global clicked_Televisions6,clicked_Televisions7,clicked_Televisions8,clicked_Televisions9,clicked_Televisions10
    drop_Televisions1=OptionMenu(lf_Televisions1,clicked_Televisions1,*options_Televisions1).place(x=48,y=212)
    drop_Televisions2=OptionMenu(lf_Televisions2,clicked_Televisions2,*options_Televisions2).place(x=48,y=212)
    drop_Televisions3=OptionMenu(lf_Televisions3,clicked_Televisions3,*options_Televisions3).place(x=48,y=212)
    drop_Televisions4=OptionMenu(lf_Televisions4,clicked_Televisions4,*options_Televisions4).place(x=48,y=212)
    drop_Televisions5=OptionMenu(lf_Televisions5,clicked_Televisions5,*options_Televisions5).place(x=48,y=212)
    drop_Televisions6=OptionMenu(lf_Televisions6,clicked_Televisions6,*options_Televisions6).place(x=48,y=212)
    drop_Televisions7=OptionMenu(lf_Televisions7,clicked_Televisions7,*options_Televisions7).place(x=48,y=212)
    drop_Televisions8=OptionMenu(lf_Televisions8,clicked_Televisions8,*options_Televisions8).place(x=48,y=212)
    drop_Televisions9=OptionMenu(lf_Televisions9,clicked_Televisions9,*options_Televisions9).place(x=48,y=212)
    drop_Televisions10=OptionMenu(lf_Televisions10,clicked_Televisions10,*options_Televisions10).place(x=48,y=212)
    def AddE1():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Redmi Note 9 Pro",13650,"13,650",clicked_Televisions1.get(),Spaces(40-len("Redmi Note 9 Pro"))])
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_Televisions1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_Televisions1.get()+") is not added to the cart.")
    def AddE2():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["OnePlus 8T 5G",42999,"42,999",clicked_Televisions2.get(),Spaces(40-len("OnePlus 8T 5G"))])
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_Televisions2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_Televisions2.get()+") is not added to the cart.")
    def AddE3():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["boAt Earphones",499,"499",clicked_Televisions3.get(),Spaces(40-len("boAt Earphones"))])
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_Televisions3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_Televisions3.get()+") is not added to the cart.")
    def AddE4():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["JBL Headphones",2799,"2,799",clicked_Televisions4.get(),Spaces(40-len("JBL Headphones"))])
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_Televisions4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_Televisions4.get()+") is not added to the cart.")
    def AddE5():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Logitech Mouse",699,"699",clicked_Televisions5.get(),Spaces(40-len("Logitech Mouse"))])
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_Televisions5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_Televisions5.get()+") is not added to the cart.")
    def AddE6():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["HP Pavilion Laptop",67900,"67,900",clicked_Televisions6.get(),Spaces(40-len("HP Pavilion Laptop"))])
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_Televisions6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_Televisions6.get()+") is not added to the cart.")
    def AddE7():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Acer Aspire 5 Laptop",49990,"49,990",clicked_Televisions7.get(),Spaces(40-len("Acer Aspire 5 Laptop"))])
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_Televisions7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_Televisions7.get()+") is not added to the cart.")
    def AddE8():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["OnePlus Android TV",15499,"15,499",clicked_Televisions8.get(),Spaces(40-len("OnePlus Android TV"))])
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_Televisions8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_Televisions8.get()+") is not added to the cart.")
    def AddE9():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Noise Colorfit Smartwatch",2999,"2,999",clicked_Televisions9.get(),Spaces(40-len("Noise Colorfit Smartwatch"))])
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_Televisions9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_Televisions9.get()+") is not added to the cart.")
    def AddE10():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["EPSON Color Printer",12250,"12,250",clicked_Televisions10.get(),Spaces(40-len("EPSON Color Printer"))])
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_Televisions10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_Televisions10.get()+") is not added to the cart.")
    price_Televisions1=Label(lf_Televisions1,text="Price: Rs.13,650",font="arial 9 bold").place(x=5,y=245)
    price_Televisions2=Label(lf_Televisions2,text="Price: Rs.42,999",font="arial 9 bold").place(x=5,y=245)
    price_Televisions3=Label(lf_Televisions3,text="Price: Rs.499",font="arial 9 bold").place(x=5,y=245)
    price_Televisions4=Label(lf_Televisions4,text="Price: Rs.2,799",font="arial 9 bold").place(x=5,y=245)
    price_Televisions5=Label(lf_Televisions5,text="Price: Rs.699",font="arial 9 bold").place(x=5,y=245)
    price_Televisions9=Label(lf_Televisions9,text="Price: Rs.2,999",font="arial 9 bold").place(x=5,y=245)
    add_Televisions1=Button(lf_Televisions1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE1).place(x=120,y=245)
    add_Televisions2=Button(lf_Televisions2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE2).place(x=120,y=245)
    add_Televisions3=Button(lf_Televisions3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE3).place(x=120,y=245)
    add_Televisions4=Button(lf_Televisions4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE4).place(x=120,y=245)
    add_Televisions5=Button(lf_Televisions5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE5).place(x=120,y=245)
    add_Televisions6=Button(lf_Televisions6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE6).place(x=60,y=245)
    add_Televisions7=Button(lf_Televisions7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE7).place(x=60,y=245)
    add_Televisions8=Button(lf_Televisions8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE8).place(x=60,y=245)
    add_Televisions9=Button(lf_Televisions9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE9).place(x=120,y=245)
    add_Televisions10=Button(lf_Televisions10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE10).place(x=60,y=245)
def CameraandaccessoriesCall():
    HideAllFrames()
    Cameraandaccessories_Label=Label(Products_frame,text="Camera and Accessories",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_Cameraandaccessories1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories1.place(x=5,y=35,width=200,height=280)
    lf_Cameraandaccessories2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories2.place(x=210,y=35,width=200,height=280)
    lf_Cameraandaccessories3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories3.place(x=415,y=35,width=200,height=280)
    lf_Cameraandaccessories4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories4.place(x=620,y=35,width=200,height=280)
    lf_Cameraandaccessories5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories5.place(x=825,y=35,width=200,height=280)
    lf_Cameraandaccessories6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories6.place(x=5,y=310,width=200,height=280)
    lf_Cameraandaccessories7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories7.place(x=210,y=310,width=200,height=280)
    lf_Cameraandaccessories8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories8.place(x=415,y=310,width=200,height=280)
    lf_Cameraandaccessories9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories9.place(x=620,y=310,width=200,height=280)
    lf_Cameraandaccessories10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories10.place(x=825,y=310,width=200,height=280)
    label_Cameraandaccessories_1=Label(lf_Cameraandaccessories1,image=Cameraandaccessories1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_2=Label(lf_Cameraandaccessories2,image=Cameraandaccessories2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Cameraandaccessories_3=Label(lf_Cameraandaccessories3,image=Cameraandaccessories3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_4=Label(lf_Cameraandaccessories4,image=Cameraandaccessories4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_5=Label(lf_Cameraandaccessories5,image=Cameraandaccessories5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_6=Label(lf_Cameraandaccessories6,image=Cameraandaccessories6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_7=Label(lf_Cameraandaccessories7,image=Cameraandaccessories7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_8=Label(lf_Cameraandaccessories8,image=Cameraandaccessories8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_9=Label(lf_Cameraandaccessories9,image=Cameraandaccessories9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_10=Label(lf_Cameraandaccessories10,image=Cameraandaccessories10_image,bd=2,justify="center").grid(row=0,column=0)
    name_Cameraandaccessories1=Label(lf_Cameraandaccessories1,text="GM Purist KW 202 Cricket Bat",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_Cameraandaccessories2=Label(lf_Cameraandaccessories2,text="GTS Dezir Cricket Leather Ball",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories3=Label(lf_Cameraandaccessories3,text="Yonex GR 303 Badminton Racquet",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories4=Label(lf_Cameraandaccessories4,text="Strauss Maxis Pro Shuttlecock",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories5=Label(lf_Cameraandaccessories5,text="Stag 4 Star Table Tennis Kit",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_Cameraandaccessories6=Label(lf_Cameraandaccessories6,text="Cockatoo CTM14A 2.5HP",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories6=Label(lf_Cameraandaccessories6,text="Treadmill with Auto-Incline",font="arial 9",justify="center").grid(row=2,column=0)
    name_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="Aurion HEX Rubber Coated Cast",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="Iron Hexagonal Dumbbells for",font="arial 9",justify="center").grid(row=2,column=0)
    name_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="Professional Exercise",font="arial 9",justify="center").grid(row=3,column=0)
    name_Cameraandaccessories8=Label(lf_Cameraandaccessories8,text="SPORTAL Foldable Multi Bench",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories8=Label(lf_Cameraandaccessories8,text="Press Workout Machine",font="arial 9",justify="center").grid(row=2,column=0)
    name_Cameraandaccessories9=Label(lf_Cameraandaccessories9,text="Reach Air Bike Exercise Cycle",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_Cameraandaccessories10=Label(lf_Cameraandaccessories10,text="RMOUR Filled Heavy Punch Bag",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    price_Cameraandaccessories1=Label(lf_Cameraandaccessories1,text="Price: Rs.1,970",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories2=Label(lf_Cameraandaccessories2,text="Price: Rs.160",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories3=Label(lf_Cameraandaccessories3,text="Price: Rs.550",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories4=Label(lf_Cameraandaccessories4,text="Price: Rs.350",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories5=Label(lf_Cameraandaccessories5,text="Price: Rs.980",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories6=Label(lf_Cameraandaccessories6,text="Price: Rs.28,990",font="arial 9 bold").grid(row=3,column=0)
    price_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="Price: Rs.949",font="arial 9 bold").grid(row=4,column=0)
    price_Cameraandaccessories8=Label(lf_Cameraandaccessories8,text="Price: Rs.6,799",font="arial 9 bold").grid(row=3,column=0)
    price_Cameraandaccessories9=Label(lf_Cameraandaccessories9,text="Price: Rs.6,999",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories10=Label(lf_Cameraandaccessories10,text="Price: Rs.2,999",font="arial 9 bold").grid(row=2,column=0)
    def AddS1():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["GM Cricket Bat",1970,"1,970",Spaces(40-len("GM Cricket Bat"))])
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is not added to the cart.")
    def AddS2():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["GTS Leather Ball",160,"160",Spaces(40-len("GTS Leather Ball"))])
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is not added to the cart.")
    def AddS3():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Yonex Badminton Racquet",550,"550",Spaces(40-len("Yonex Badminton Racquet"))])
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is not added to the cart.")
    def AddS4():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Strauss Shuttlecock",350,"350",Spaces(40-len("Strauss Shuttlecock"))])
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is not added to the cart.")
    def AddS5():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Table Tennis Kit",980,"980",Spaces(40-len("Table Tennis Kit"))])
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is not added to the cart.")
    def AddS6():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Cockatoo Treadmill",28990,"28,990",Spaces(40-len("Cockatoo Treadmill"))])
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is not added to the cart.")
    def AddS7():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Aurion Dumbbells",949,"949",Spaces(40-len("Aurion Dumbbells"))])
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is not added to the cart.")
    def AddS8():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Bench Press Machine",6799,"6,799",Spaces(40-len("Bench Press Machine"))])
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is not added to the cart.")
    def AddS9():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Reach Exercise Cycle",6999,"6,999",Spaces(40-len("Reach Exercise Cycle"))])
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is not added to the cart.")
    def AddS10():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["RMOUR Punch Bag",2999,"2,999",Spaces(40-len("RMOUR Punch Bag"))])
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is not added to the cart.")
    add_Cameraandaccessories1=Button(lf_Cameraandaccessories1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS1).place(x=68,y=245)
    add_Cameraandaccessories2=Button(lf_Cameraandaccessories2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS2).place(x=68,y=245)
    add_Cameraandaccessories3=Button(lf_Cameraandaccessories3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS3).place(x=68,y=245)
    add_Cameraandaccessories4=Button(lf_Cameraandaccessories4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS4).place(x=68,y=245)
    add_Cameraandaccessories5=Button(lf_Cameraandaccessories5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS5).place(x=68,y=245)
    add_Cameraandaccessories6=Button(lf_Cameraandaccessories6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS6).place(x=68,y=245)
    add_Cameraandaccessories7=Button(lf_Cameraandaccessories7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS7).place(x=68,y=245)
    add_Cameraandaccessories8=Button(lf_Cameraandaccessories8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS8).place(x=68,y=245)
    add_Cameraandaccessories9=Button(lf_Cameraandaccessories9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS9).place(x=68,y=245)
    add_Cameraandaccessories10=Button(lf_Cameraandaccessories10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS10).place(x=68,y=245)
def ComputerandtabletsCall():
    HideAllFrames()
    Computerandtablets_Label=Label(Products_frame,text="Computerandtablets",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_Computerandtablets1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets1.place(x=5,y=35,width=200,height=280)
    lf_Computerandtablets2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets2.place(x=210,y=35,width=200,height=280)
    lf_Computerandtablets3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets3.place(x=415,y=35,width=200,height=280)
    lf_Computerandtablets4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets4.place(x=620,y=35,width=200,height=280)
    lf_Computerandtablets5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets5.place(x=825,y=35,width=200,height=280)
    lf_Computerandtablets6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets6.place(x=5,y=310,width=200,height=280)
    lf_Computerandtablets7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets7.place(x=210,y=310,width=200,height=280)
    lf_Computerandtablets8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets8.place(x=415,y=310,width=200,height=280)
    lf_Computerandtablets9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets9.place(x=620,y=310,width=200,height=280)
    lf_Computerandtablets10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets10.place(x=825,y=310,width=200,height=280)
    label_Computerandtablets_1=Label(lf_Computerandtablets1,image=Computerandtablets1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_2=Label(lf_Computerandtablets2,image=Computerandtablets2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_3=Label(lf_Computerandtablets3,image=Computerandtablets3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_4=Label(lf_Computerandtablets4,image=Computerandtablets4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_5=Label(lf_Computerandtablets5,image=Computerandtablets5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_6=Label(lf_Computerandtablets6,image=Computerandtablets6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_7=Label(lf_Computerandtablets7,image=Computerandtablets7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_8=Label(lf_Computerandtablets8,image=Computerandtablets8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_9=Label(lf_Computerandtablets9,image=Computerandtablets9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_10=Label(lf_Computerandtablets10,image=Computerandtablets10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    name_Computerandtablets1=Label(lf_Computerandtablets1,text="Julian Wood 2 Door Wardrobe",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_Computerandtablets2=Label(lf_Computerandtablets2,text="Zuari Niko Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets2=Label(lf_Computerandtablets2,text="3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets3=Label(lf_Computerandtablets3,text="TADesign Vinicio Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets3=Label(lf_Computerandtablets3,text="Wood 3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets4=Label(lf_Computerandtablets4,text="Flipkart Perfect Homes Opus",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets4=Label(lf_Computerandtablets4,text="Engineered Wood",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets4=Label(lf_Computerandtablets4,text="Queen Box Bed",font="arial 9",justify="center").grid(row=3,column=0)
    name_Computerandtablets5=Label(lf_Computerandtablets5,text="Forzza Jasper Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets5=Label(lf_Computerandtablets5,text="Wood King Box Bed",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets6=Label(lf_Computerandtablets6,text="Zuari Wood TV Entertainment Unit",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_Computerandtablets7=Label(lf_Computerandtablets7,text="Forzza Belfast Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    name_Computerandtablets7=Label(lf_Computerandtablets7,text="TV Entertainment Unit",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets8=Label(lf_Computerandtablets8,text="Kurlon Crescent Leatherette",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets8=Label(lf_Computerandtablets8,text="3 + 1 + 1 Black Sofa Set",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets9=Label(lf_Computerandtablets9,text="Suncrown Computerandtablets Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets9=Label(lf_Computerandtablets9,text="Fabric 6 Seater Sofa",font="arial 9",justify="center").grid(row=2,column=0)
    name_Computerandtablets9=Label(lf_Computerandtablets9,text="3 + 2 + 1 Vanilla Cream Sofa Set",font="arial 9",justify="center").grid(row=3,column=0)
    name_Computerandtablets10=Label(lf_Computerandtablets10,text="Allie Wood Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets10=Label(lf_Computerandtablets10,text="6 Seater Dining Set",font="arial 9",justify="center").grid(row=2,column=0)
    price_Computerandtablets1=Label(lf_Computerandtablets1,text="Price: Rs.6,990",font="arial 9 bold").grid(row=2,column=0)
    price_Computerandtablets2=Label(lf_Computerandtablets2,text="Price: Rs.17,390",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets3=Label(lf_Computerandtablets3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets4=Label(lf_Computerandtablets4,text="Price: Rs.12,290",font="arial 9 bold").grid(row=4,column=0)
    price_Computerandtablets5=Label(lf_Computerandtablets5,text="Price: Rs.13,640",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets6=Label(lf_Computerandtablets6,text="Price: Rs.6,590",font="arial 9 bold").grid(row=2,column=0)
    price_Computerandtablets7=Label(lf_Computerandtablets7,text="Price: Rs.14,999",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets8=Label(lf_Computerandtablets8,text="Price: Rs.24,490",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets9=Label(lf_Computerandtablets9,text="Price: Rs.36,854",font="arial 9 bold").grid(row=4,column=0)
    price_Computerandtablets10=Label(lf_Computerandtablets10,text="Price: Rs.26,999",font="arial 9 bold").grid(row=3,column=0)
    def AddF1():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Julian 2 Door Wardrobe",6990,"6,990",Spaces(40-len("Julian 2 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is not added to the cart.")
    def AddF2():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Zuari 3 Door Wardrobe",17390,"17,390",Spaces(40-len("Zuari 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF3():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["TADesign 3 Door Wardrobe",34999,"34,999",Spaces(40-len("TADesign 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF4():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Opus Queen Box Bed",12290,"12,290",Spaces(40-len("Opus Queen Box Bed"))])
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is not added to the cart.")
    def AddF5():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Jasper King Box Bed",13640,"13,640",Spaces(40-len("Jasper King Box Bed"))])
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is not added to the cart.")
    def AddF6():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Zuari TV Unit",6590,"6,590",Spaces(40-len("Zuari TV Unit"))])
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is not added to the cart.")
    def AddF7():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Forzza TV Unit",14999,"14,999",Spaces(40-len("Forzza TV Unit"))])
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is not added to the cart.")
    def AddF8():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Kurlon Black Sofa Set",24490,"24,490",Spaces(40-len("Kurlon Black Sofa Set"))])
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is not added to the cart.")
    def AddF9():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Suncrown Cream Sofa Set",36854,"36,854",Spaces(40-len("Suncrown Cream Sofa Set"))])
            messagebox.showinfo("Product Status","Suncrown Computerandtablets Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Suncrown Computerandtablets Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is not added to the cart.")
    def AddF10():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Allie 6 Seater Dining Set",26999,"26,999",Spaces(40-len("Allie 6 Seater Dining Set"))])
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is not added to the cart.")
    add_Computerandtablets1=Button(lf_Computerandtablets1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF1).place(x=68,y=245)
    add_Computerandtablets2=Button(lf_Computerandtablets2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF2).place(x=68,y=245)
    add_Computerandtablets3=Button(lf_Computerandtablets3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF3).place(x=68,y=245)
    add_Computerandtablets4=Button(lf_Computerandtablets4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF4).place(x=68,y=245)
    add_Computerandtablets5=Button(lf_Computerandtablets5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF5).place(x=68,y=245)
    add_Computerandtablets6=Button(lf_Computerandtablets6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF6).place(x=68,y=245)
    add_Computerandtablets7=Button(lf_Computerandtablets7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF7).place(x=68,y=245)
    add_Computerandtablets8=Button(lf_Computerandtablets8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF8).place(x=68,y=245)
    add_Computerandtablets9=Button(lf_Computerandtablets9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF9).place(x=68,y=245)
    add_Computerandtablets10=Button(lf_Computerandtablets10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF10).place(x=68,y=245)
def AudioCall():
    HideAllFrames()
    audio_Label=Label(Products_frame,text="Audio",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_audio1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio1.place(x=5,y=35,width=200,height=280)
    lf_audio2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio2.place(x=210,y=35,width=200,height=280)
    lf_audio3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio3.place(x=415,y=35,width=200,height=280)
    lf_audio4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio4.place(x=620,y=35,width=200,height=280)
    lf_audio5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio5.place(x=825,y=35,width=200,height=280)
    lf_audio6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio6.place(x=5,y=310,width=200,height=280)
    lf_audio7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio7.place(x=210,y=310,width=200,height=280)
    lf_audio8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio8.place(x=415,y=310,width=200,height=280)
    lf_audio9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio9.place(x=620,y=310,width=200,height=280)
    lf_audio10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_audio10.place(x=825,y=310,width=200,height=280)
    label_audio_1=Label(lf_audio1,image=audio1_image,bd=2,justify="center").grid(row=0,column=0)
    label_audio_2=Label(lf_audio2,image=audio2_image,bd=2,justify="center").grid(row=0,column=0)
    label_audio_3=Label(lf_audio3,image=audio3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_audio_4=Label(lf_audio4,image=audio4_image,bd=2,justify="center").grid(row=0,column=0)
    label_audio_5=Label(lf_audio5,image=audio5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_audio_6=Label(lf_audio6,image=audio6_image,bd=2,justify="center").grid(row=0,column=0)
    label_audio_7=Label(lf_audio7,image=audio7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_audio_8=Label(lf_audio8,image=audio8_image,bd=2,justify="center").grid(row=0,column=0)
    label_audio_9=Label(lf_audio9,image=audio9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_audio_10=Label(lf_audio10,image=audio10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_audio1=Label(lf_audio1,text="Whirlpool 7kg Automatic Top Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio2=Label(lf_audio2,text="IFB 6kg Fully Automatic Front Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio3=Label(lf_audio3,text="Samsung 1.5 Ton 5 Star",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio3=Label(lf_audio3,text="Split Inverter AC",font="arial 9",justify="center").grid(row=2,column=0)
    name_audio4=Label(lf_audio4,text="LG 260L Double Door Refrigerator",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio5=Label(lf_audio5,text="IFB 20 L Convection",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio5=Label(lf_audio5,text="Microwave Oven 20SC2",font="arial 9",justify="center").grid(row=2,column=0)
    name_audio6=Label(lf_audio6,text="Bajaj GX1 500W Mixer Grinder",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_audio7=Label(lf_audio7,text="Balzano OX218 Electric Kettle",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio8=Label(lf_audio8,text="Elica WDFL 606 HAC MS NERO",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio8=Label(lf_audio8,text="Auto Clean Wall Mounted Chimney",font="arial 9",justify="center").grid(row=2,column=0)
    name_audio9=Label(lf_audio9,text="Kent Ace 8 L Water Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio10=Label(lf_audio10,text="Eureka Forbes Quick Clean DX",font="arial 9",justify="center").grid(row=1,column=0)
    name_audio10=Label(lf_audio10,text="Dry Vacuum Cleaner",font="arial 9",justify="center").grid(row=2,column=0)
    price_audio1=Label(lf_audio1,text="Price: Rs.14,990",font="arial 9 bold").grid(row=2,column=0)
    price_audio2=Label(lf_audio2,text="Price: Rs.23,790",font="arial 9 bold").grid(row=2,column=0)
    price_audio3=Label(lf_audio3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_audio4=Label(lf_audio4,text="Price: Rs.25,290",font="arial 9 bold").grid(row=2,column=0)
    price_audio5=Label(lf_audio5,text="Price: Rs.9,690",font="arial 9 bold").grid(row=3,column=0)
    price_audio6=Label(lf_audio6,text="Price: Rs.1,999",font="arial 9 bold").grid(row=2,column=0)
    price_audio7=Label(lf_audio7,text="Price: Rs.879",font="arial 9 bold").grid(row=2,column=0)
    price_audio8=Label(lf_audio8,text="Price: Rs.11,999",font="arial 9 bold").grid(row=3,column=0)
    price_audio9=Label(lf_audio9,text="Price: Rs.12,499",font="arial 9 bold").grid(row=2,column=0)
    price_audio10=Label(lf_audio10,text="Price: Rs.3,249",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Whirlpool Top Load",14990,"14,990",Spaces(40-len("Whirlpool Top Load"))])
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is not added to the cart.")
    def AddA2():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["IFB Front Load",23790,"23,790",Spaces(40-len("IFB Front Load"))])
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is not added to the cart.")
    def AddA3():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Samsung Inverter AC",34999,"34,999",Spaces(40-len("Samsung Inverter AC"))])
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is not added to the cart.")
    def AddA4():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["LG 260L Refrigerator",25290,"25,290",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is not added to the cart.")
    def AddA5():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["IFB Microwave Oven",9690,"9,690",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is not added to the cart.")
    def AddA6():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Bajaj Mixer Grinder",1999,"1,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is not added to the cart.")
    def AddA7():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Balzano Electric Kettle",879,"879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is not added to the cart.")
    def AddA8():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Elica Wall Mounted Chimney",11999,"11,999",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is not added to the cart.")
    def AddA9():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Kent Ace Water Purifier",12499,"12,499",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is not added to the cart.")
    def AddA10():
        global audio_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            audio_list.append(["Eureka Dry Vacuum Cleaner",3249,"3,249",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is not added to the cart.")
    add_audio1=Button(lf_audio1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA1).place(x=68,y=245)
    add_audio2=Button(lf_audio2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA2).place(x=68,y=245)
    add_audio3=Button(lf_audio3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA3).place(x=68,y=245)
    add_audio4=Button(lf_audio4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA4).place(x=68,y=245)
    add_audio5=Button(lf_audio5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA5).place(x=68,y=245)
    add_audio6=Button(lf_audio6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA6).place(x=68,y=245)
    add_audio7=Button(lf_audio7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA7).place(x=68,y=245)
    add_audio8=Button(lf_audio8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA8).place(x=68,y=245)
    add_audio9=Button(lf_audio9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA9).place(x=68,y=245)
    add_audio10=Button(lf_audio10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA10).place(x=68,y=245)
HomeAppliances_button=Button(Button_frame,text="HomeAppliances",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=HomeAppliancesCall)
HomeAppliances_button.grid(row=0,column=0,padx=5,pady=5)
Televisions_button=Button(Button_frame,text="Televisions",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=TelevisionsCall)
Televisions_button.grid(row=1,column=0,padx=5,pady=5)
Cameraandaccessories_button=Button(Button_frame,text="Camera and accessories",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=CameraandaccessoriesCall)
Cameraandaccessories_button.grid(row=2,column=0,padx=5,pady=5)
Computerandtablets_button=Button(Button_frame,text="Computerandtablets",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=ComputerandtabletsCall)
Computerandtablets_button.grid(row=3,column=0,padx=5,pady=5)
audio_button=Button(Button_frame,text="Audio",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=AudioCall)
audio_button.grid(row=4,column=0,padx=5,pady=5)
Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="green",font="arial 16 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.750)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        HomeAppliances_price=0
        Televisions_price=0
        Cameraandaccessories_price=0
        Computerandtablets_price=0
        appliances_price=0
        for i in range(len(HomeAppliances_list)):
            HomeAppliances_price+=HomeAppliances_list[i][1]
        for i in range(len(Televisions_list)):
            Televisions_price+=Televisions_list[i][1]
        for i in range(len(Cameraandaccessories_list)):
            Cameraandaccessories_price+=Cameraandaccessories_list[i][1]
        for i in range(len(Computerandtablets_list)):
            Computerandtablets_price+=Computerandtablets_list[i][1]
        for i in range(len(audio_list)):
            audio_price+=audio_list[i][1]
        total_price=HomeAppliances_price+Televisions_price+Cameraandaccessories_price+Computerandtablets_price+audio_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"The Emporium\n"+Spaces(90,'*')+"\n")
            if len(HomeAppliances_list)>0:
                bill_txt_area.insert(END,"HomeAppliances Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in HomeAppliances_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal HomeAppliances Price : Rs."+str(HomeAppliances_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Televisions_list)>0:
                bill_txt_area.insert(END,"Televisions Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in Televisions_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Televisions Price : Rs."+str(Televisions_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Cameraandaccessories_list)>0:
                bill_txt_area.insert(END,"Camera and accessories(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Cameraandaccessories_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Camera and accessories Price : Rs."+str(Cameraandaccessories_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Computerandtablets_list)>0:
                bill_txt_area.insert(END,"Computerandtablets Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Computerandtablets_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Computerandtablets Price : Rs."+str(Computerandtablets_price)+"\n"+Spaces(90,'*')+"\n")
            if len(audio_list)>0:
                bill_txt_area.insert(END,"Audio(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in audio_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Audio Price : Rs."+str(audio_price)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.grid(row=0,column=3)
root.mainloop()
