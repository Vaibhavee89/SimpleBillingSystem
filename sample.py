from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root= root
        self.root.geometry()
        self.root.title('Billing Software')

        #variables
        self.product= StringVar()
        self.prices=IntVar()
        self.qty= IntVar()
        self.sub_total=StringVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        #Product Categories list
        self.Category=['Select Option', 'Rice and Flours','Pulses','Spice','Oils','Nuts','Other Ingredients','Dairy']

        #Subcategory rice and flours 

        self.Riceflours=["Turmeric","Sugar","Jaggery","Basmati rice" ,"wheat flour"]
        self.price_turmeric=256
        self.price_sugar=31
        self.price_jaggery=100
        self.price_rice=180
        self.price_wheat=67
        

        #Subcategory pulses

        self.Pulses=["Tur dal","urad","moong", "Chana","Rajma"]
        self.price_tur=94
        self.price_urad=120
        self.price_moong=250
        self.price_chana=70
        self.price_rajma=200

        #Subcategory Spice

        self.Spice= ["Powder salt","Red chilli", "Dhania powder","Garam masala", "Chat masala"]
        self.price_salt=30
        self.price_chilli=185
        self.price_dhania=140
        self.price_garam=80
        self.price_chat=420
        

        #Subcategory oils

        self.oils=["Sesame oil","Cooking oil","Coconut oil","Ghee","butter","Olive oil"]
        self.price_sesame=150
        self.price_cooking=170
        self.price_coconut=260
        self.price_ghee=700
        self.price_butter=417
        self.price_olive=500

        #Subcategory nuts

        self.nuts=["Cashew nuts", "Dry raisins", "Almonds", "Peanuts"]
        self.price_cashew=490
        self.price_raisins=150
        self.price_almonds=610
        self.price_peanuts=90

        #subcategory other

        self.other=["Papad","Noodles","Pasta","Tomato Ketchup","Jam"]
        self.price_papad=1400
        self.price_noodles=20
        self.price_pasta=37
        self.price_ketchup=140
        self.price_Jam=300
        
        #Subcategory dairy

        self.dairy=["Butter","Curd","Fresh cream","Fresh Milk","Paneer"]
        
        self.price_butter=55
        self.price_curd=40
        self.price_cream=280
        self.price_milk=60
        self.price_paneer=378
        
        
        
        
        
        #Product Category list
        lbl_title= Label(self.root, text="BILLING SOFTWARE", font= ('times new roman',35,'bold'), bg= 'white', fg= 'black')
        lbl_title.place(x= 0, y=130, width= 1530, height= 45)
        Main_Frame= Frame(self.root, bd=5,relief= GROOVE, bg= 'white')
        Main_Frame.place(x=0,y=175, width= 1530, height= 620)
        
        #product frame
        Prod_Frame= LabelFrame(Main_Frame, text= 'Products', font= ('times new roman',12,'bold'),bg= 'white',fg= 'black')
        Prod_Frame.place(x=10, y=5, width=600, height=200)

        #Category
        self.lblCategory= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Select Categories', bd=4)
        self.lblCategory.grid(row=0, column=0, sticky= W, padx=5, pady=2)

        self.Combo_Category= ttk.Combobox(Prod_Frame, values=self.Category, font= ('arial', 12, 'bold'),width= 24, state= 'readonly')
        
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky= W, padx=5, pady= 2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
            
        #subcategory
        self.lblSubCategory= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'SubCategory', bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky= W, padx=5, pady=2)
        self.ComboSubCategory= ttk.Combobox(Prod_Frame,state="readonly", font= ('arial', 10, 'bold'),textvariable=self.product,width= 24)
        self.ComboSubCategory.grid(row=1, column=1, sticky= W, padx=5, pady= 2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Categories)
        print(self.Combo_Category.get())
        
            
        #price
        self.lblPrice= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Price', bd=4)
        self.lblPrice.grid(row=2, column=0, sticky= W, padx=5, pady=2)
        self.ComboPrice= ttk.Combobox(Prod_Frame, font= ('arial', 12, 'bold'),width= 24, state= 'readonly',textvariable=self.prices)
        self.ComboPrice.grid(row=2, column=1, sticky= W, padx=5, pady= 2)

        #Qty
        self.lblCategory= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Quantity', bd=4)
        self.lblCategory.grid(row=3, column=0, sticky= W, padx=5, pady=2)
        self.Combo_Category= ttk.Entry(Prod_Frame, font= ('arial', 12, 'bold'),width= 24, state= 'readonly',textvariable=self.qty)
        self.Combo_Category.grid(row=3, column=1, sticky= W, padx=5, pady= 2)


        #RightFrame Bill area
        RightLabelFrame= LabelFrame(Main_Frame, text="Bill", font= ('times new roman',12,'bold'),bg= 'white',fg= 'black')
        RightLabelFrame.place(x=1000, y=45, width= 480, height=440)

        scroll_y= Scrollbar(RightLabelFrame, orient= VERTICAL)
        self.textarea= Text(RightLabelFrame, yscrollcommand= scroll_y.set, bg= "white", fg= 'black',font= ('times new roman',12,'bold'))
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_y.config(command= self.textarea.yview)
        self.textarea.pack(fill= BOTH,expand=1)


        #LabelFrame
        Bottom_Frame= LabelFrame(Main_Frame, text= 'Bill Counter', font= ('times new roman',12,'bold'),bg= 'white',fg= 'black')
        Bottom_Frame.place(x=0, y=485, width=1520, height=125)
        
        self.lblSubTotal= Label(Bottom_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Sub Total', bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky= W, padx=5, pady=2)
        
        self.EntrySubTotal= ttk.Entry(Bottom_Frame, font= ('arial', 10, 'bold'),width= 24)
        self.EntrySubTotal.grid(row=0, column=1, sticky= W, padx=5, pady= 2)
        
        self.lbl_tax= Label(Bottom_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Tax', bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky= W, padx=5, pady=2)
        
        self.txt_tax= ttk.Entry(Bottom_Frame, font= ('arial', 10, 'bold'),width= 24)
        self.txt_tax.grid(row=1, column=1, sticky= W, padx=5, pady= 2)
        
        self.lblAmountTotal= Label(Bottom_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Total', bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky= W, padx=5, pady=2)
        
        self.txtAmountTotal= ttk.Entry(Bottom_Frame, font= ('arial', 10, 'bold'),width= 24)
        self.txtAmountTotal.grid(row=2, column=1, sticky= W, padx=5, pady= 2)

        #Button Frame

        Btn_Frame= Frame(Bottom_Frame, bd=2, bg= "white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart= Button(Btn_Frame,command=self.AddItem,height= 2,text="Add To Cart",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor='hand2')
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill= Button(Btn_Frame,command=self.gen_bill,height= 2,text="Generate Bill",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor= 'hand2')
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnClear= Button(Btn_Frame,height= 2,text="Clear",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor='hand2')
        self.BtnClear.grid(row=0, column=3)

        self.BtnExit= Button(Btn_Frame,height= 2,text="Exit",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor= 'hand2')
        self.BtnAddToCart.grid(row=0, column=4)
        self.welcome()

        self.l=[]
#Add to Cart
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.ComboSubCategory.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.ComboSubCategory.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            
            self.textarea.insert(END,"\n==================================================")

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome")

        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n==================================================")


    def Categories(self,event):
        var = event.widget.get()
        print(var)
        

        if var=="Rice and Flours":
            self.ComboSubCategory.config(value=self.Riceflours)
        if var=="Jaggery":
            self.ComboPrice.config(value=self.price_jaggery)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Sugar":
            self.ComboPrice.config(value=self.price_sugar)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Turmeric":
            self.ComboPrice.config(value=self.price_turmeric)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Basmati rice":
            self.ComboPrice.config(value=self.price_rice)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="wheat flour":
            self.ComboPrice.config(value=self.price_wheat)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Pulses":
            self.ComboSubCategory.config(value=self.Pulses)
            
        if var=="Tur dal":
            self.ComboPrice.config(value=self.price_tur)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="urad":
            self.ComboPrice.config(value=self.price_urad)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="moong":
            self.ComboPrice.config(value=self.price_moong)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Chana":
            self.ComboPrice.config(value=self.price_chana)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Rajma":
            self.ComboPrice.config(value=self.price_rajma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if var=="Spice":
            self.ComboSubCategory.config(value=self.Spice)
            self.ComboSubCategory.current(0)
        if var=="Powder salt":
            self.ComboPrice.config(value=self.price_salt)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Red chilli":
            self.ComboPrice.config(value=self.price_chilli)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if var=="Dhania powder":
            self.ComboPrice.config(value=self.price_dhania)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Garam masala":
            self.ComboPrice.config(value=self.price_garam)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Chat masala":    
            self.ComboPrice.config(value=self.price_chat)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Nuts":
            self.ComboSubCategory.config(value=self.nuts)
            self.ComboSubCategory.current(0)
        if var=="Cashew nuts":
            self.ComboPrice.config(value=self.price_cashew)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Dry raisins":
            self.ComboPrice.config(value=self.price_raisins)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var== "Almonds":
            self.ComboPrice.config(value=self.price_almonds)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var== "Peanuts":
            self.ComboPrice.config(value=self.price_peanuts)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if var=="Oils":
            self.ComboSubCategory.config(value=self.oils)
            self.ComboSubCategory.current(0)
        if var=="Sesame oil":
            self.ComboPrice.config(value=self.price_sesame)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Cooking oil":
            self.ComboPrice.config(value=self.price_cooking)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Coconut oil":
            self.ComboPrice.config(value=self.price_coconut)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Ghee":
            self.ComboPrice.config(value=self.price_ghee)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="butter":
            self.ComboPrice.config(value=self.price_butter)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Olive oil":
            self.ComboPrice.config(value=self.price_olive)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if var=="Other Ingredients":
            self.ComboSubCategory.config(value=self.other)
            self.ComboSubCategory.current(0)
        if var=="Papad":
            self.ComboPrice.config(value=self.price_papad)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Noodles":
            self.ComboPrice.config(value=self.price_noodles)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Pasta":
            self.ComboPrice.config(value=self.price_pasta)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Tomato Ketchup":
            self.ComboPrice.config(value=self.price_ketchup)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Jam":
            self.ComboPrice.config(value=self.price_Jam)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if var=="Dairy":
            self.ComboSubCategory.config(value=self.dairy)
            self.ComboSubCategory.current(0)
        if var=="Butter":
            self.ComboPrice.config(value=self.price_butter)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Curd":
            self.ComboPrice.config(value=self.price_curd)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Fresh cream":
            self.ComboPrice.config(value=self.price_cream)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Fresh Milk":
            self.ComboPrice.config(value=self.price_milk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if var=="Paneer":
            self.ComboPrice.config(value=self.price_paneer)
            self.ComboPrice.current(0)
            self.qty.set(1)

            



if __name__=="__main__":
    root= Tk()
    obj= Bill_App(root)
    root.mainloop()