from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root= root
        self.root.geometry()
        self.root.title('BIlling Software')

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

        self.Riceflours=["Turmeric","Sugar","Jaggery","Basmati rice" ,"wheat flour", "Maida", "Rice Flour", "Besan", "Poha", "Vermicelli"]
        self.price_turmeric=256
        self.price_sugar=31
        self.price_jaggery=100
        self.price_rice=180
        self.price_wheat=67
        self.price_maida=60
        self.price_rice=49
        self.price_besan=129
        self.price_poha=205
        self.price_vermicelli=100

        #Subcategory pulses

        self.Pulses=["Tur dal","urad","moong", "Chana","Rajma"]
        self.price_tur=94
        self.price_urad=120
        self.price_moong=250
        self.price_chana=70
        self.price_rajma=200

        #Subcategory Spice

        self.Spice= ["Powder salt","Red chilli", "Dhania powder","Garam masala", "Chat masala", "Cumin", "Pepper powder", "Ginger garlic paste", "Tamarind", "Sambhar masala", "Biryani masala", "Mustard seeds", "Methi seeds", "Ajwain", "Hing", "Elaichi","Cloves", "Cinnamon","Tea Powder","Cocoa Powder", "Instant Coffee powder", "Baking soda"]
        self.price_salt=30
        self.price_chilli=185
        self.price_dhania=140
        self.price_garam=80
        self.price_chat=420
        self.price_cumin=335
        self.price_pepper=400
        self.price_ginger=23
        self.price_tamarind=225
        self.price_sambhar=30
        self.price_biryani=30
        self.price_mustard=46
        self.price_methi=60
        self.price_ajwain=277
        self.price_hing=250
        self.price_elaichi=1480
        self.price_cloves=750
        self.price_cinnamon=550

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

        self.other=["Papad","Noodles","Pasta","Tomato Ketchup","Jam","Mayonaisse","Bread"]
        self.price_papad=1400
        self.price_noodles=20
        self.price_pasta=37
        self.price_ketchup=140
        self.price_Jam=300
        self.price_Mayo=200
        self.price_bread=30

        #Subcategory dairy

        self.dairy=["Cheese","Butter","Curd","Fresh cream","Fresh Milk","Paneer"]
        self.price_cheese=780
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

        self.Combo_Category= ttk.Combobox(Prod_Frame, value= self.Category, font= ('arial', 12, 'bold'),width= 24, state= 'readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky= W, padx=5, pady= 2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
            
        #subcategory
        self.lblSubCategory= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'SubCategory', bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky= W, padx=5, pady=2)

        self.ComboSubCategory= ttk.Combobox(Prod_Frame,state= 'readonly', font= ('arial', 10, 'bold'),textvariable=self.product,width= 24)
        self.ComboSubCategory.grid(row=1, column=1, sticky= W, padx=5, pady= 2)
        
       
        
            
        #price
        self.lblPrice= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Price', bd=4)
        self.lblPrice.grid(row=2, column=0, sticky= W, padx=5, pady=2)
        self.ComboPrice= ttk.Combobox(Prod_Frame, font= ('arial', 12, 'bold'),width= 24, state= 'readonly', textvariable=self.prices)
        self.ComboPrice.grid(row=2, column=1, sticky= W, padx=5, pady= 2)


        #Qty
        self.lblCategory= Label(Prod_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Quantity', bd=4)
        self.lblCategory.grid(row=3, column=0, sticky= W, padx=5, pady=2)
        self.Combo_Category= ttk.Entry(Prod_Frame, font= ('arial', 12, 'bold'),width= 24, state= 'readonly', textvariable=self.qty)
        self.Combo_Category.grid(row=3, column=1, sticky= W, padx=5, pady= 2)


        #RightFrame Bill area
        RightLabelFrame= LabelFrame(Main_Frame, text="Bill", font= ('times new roman',12,'bold'),bg= 'white',fg= 'black')
        RightLabelFrame.place(x=1000, y=45, width= 480, height=440)

        scroll_y= Scrollbar(RightLabelFrame, orient= VERTICAL)
        self.textarea= Text(RightLabelFrame, yscrollcommand= scroll_y.set, bg= "white", fg= 'blue',font= ('times new roman',12,'bold'))
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
        
        self.lblAmountTotal= Label(Bottom_Frame, font= ('arial',12,'bold'),bg= 'white',text= 'Sub Total', bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky= W, padx=5, pady=2)
        
        self.txtAmountTotal= ttk.Entry(Bottom_Frame, font= ('arial', 10, 'bold'),width= 24)
        self.txtAmountTotal.grid(row=2, column=1, sticky= W, padx=5, pady= 2)

        #Button Frame

        Btn_Frame= Frame(Bottom_Frame, bd=2, bg= "white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart= Button(Btn_Frame,height= 2,text="Add To Cart",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor='hand2')
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill= Button(Btn_Frame,height= 2,text="Generate Bill",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor= 'hand2')
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnClear= Button(Btn_Frame,height= 2,text="Clear",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor='hand2')
        self.BtnClear.grid(row=0, column=3)

        self.BtnExit= Button(Btn_Frame,height= 2,text="Exit",font= ('arial', 15, 'bold'), bg= 'black', fg= 'white', width= 15, cursor= 'hand2')
        self.BtnAddToCart.grid(row=0, column=4)

        self.list=[]
        #Add items
        def AddItem(self):
            self.n=self.prices.get()
            self.m= self.qty.get()*self.n
            self.l.append(self.m)
            if self.product.get()=="":
                messagebox.showerror('Error','Please Select the Product Name')
            else:
                self.textarea.insert(END,"\n{}self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")



    def Categories(self,event):
        var= event.widget.get()
        print(var)
        if var=="Rice and Flours":
            self.ComboSubCategory.config(value=self.Riceflours)
            self.ComboSubCategory.current(0)

        if var=="Pulses":
            self.ComboSubCategory.config(value=self.Pulses)
            self.ComboSubCategory.current(0)

        if var=="Spice":
            self.ComboSubCategory.config(value=self.Spice)
            self.ComboSubCategory.current(0)

        if var=="Oils":
            self.ComboSubCategory.config(value=self.oils)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Nuts":
            self.ComboSubCategory.config(value=self.nuts)
            self.ComboSubCategory.current(0)

        if var=="Other Ingredients":
            self.ComboSubCategory.config(value=self.other)
            self.ComboSubCategory.current(0)

        if var=="Dairy":
            self.ComboSubCategory.config(value=self.dairy)
            self.ComboSubCategory.current(0)

    def Categories(self,event):
        var = event.widget.get()
        print(var)
        

        if var=="Rice and Flours":
            self.ComboSubCategory.config(value=self.Riceflours)
        if var=="Jaggery":
            self.ComboPrice.config(value=self.price_jaggery)

        if var=="Sugar":
            self.ComboPrice.config(value=self.price_sugar)

        if var=="Pulses":
            self.ComboSubCategory.config(value=self.Pulses)


        if var=="Spice":
            self.ComboSubCategory.config(value=self.Spice)
            self.ComboSubCategory.current(0)

        if var=="Oils":
            self.ComboSubCategory.config(value=self.oils)
            self.ComboSubCategory.current(0)

        if var=="Nuts":
            self.ComboSubCategory.config(value=self.nuts)
            self.ComboSubCategory.current(0)

        if var=="Other Ingredients":
            self.ComboSubCategory.config(value=self.other)
            self.ComboSubCategory.current(0)

        if var=="Dairy":
            self.ComboSubCategory.config(value=self.dairy)
            self.ComboSubCategory.current(0)

            


    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_category.set("")
        self.c_subcategory  
        
       
        

if __name__=="__main__":
    root= Tk()
    obj= Bill_App(root)
    root.mainloop()
    
