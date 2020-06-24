from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

def mensaje():
    answer = messagebox.askyesno("Salir", "¿Desesa salir del sistema?, Confirme...")
    if(answer):
    	ventana.destroy()

class Student:
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title("Sistema Administrador de Estudiantes")
		self.ventana.geometry("1370x700+00+0")
		self.ventana.resizable(False,False)

		title=Label(self.ventana,text="Sistema Administrador de Estudiantes", bd=10,relief=RAISED, font=("Arial", 40,"bold"),bg="green", fg="white")
		title.pack(side=TOP)

		Exit_btn=Button(ventana,text="Salir", width=7, bg="orange", font=("Arial",17,"bold"),command=mensaje)
		Exit_btn.place(x=1200, y=40)

		#====Variables=====
		self.matricula_var=StringVar()
		self.nombre_var=StringVar()
		self.email_var=StringVar()
		self.genero_var=StringVar()
		self.telefono_var=StringVar()
		self.fdn_var=StringVar()

		self.buscar_por=StringVar()
		self.buscar_txt=StringVar()

		Manage_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="green")
		Manage_Frame.place(x=20,y=100,width=520,height=580)

		m_title=Label(Manage_Frame,text="Control de Estudiantes", bg="yellow", fg="red", font=("Arial",30,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_roll=Label(Manage_Frame,text="Matricula:", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		txt_Roll=Entry(Manage_Frame, textvariable=self.matricula_var , font=("Arial",15,"bold"), bd=5, relief=GROOVE)
		txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

		lbl_name=Label(Manage_Frame,text="Nombre:", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		txt_name=Entry(Manage_Frame, textvariable=self.nombre_var, font=("Arial",15,"bold"), bd=5, relief=GROOVE)
		txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

		lbl_email=Label(Manage_Frame,text="Correo E.", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		txt_email=Entry(Manage_Frame, textvariable=self.email_var, font=("Arial",15,"bold"), bd=5, relief=GROOVE)
		txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

		lbl_gender=Label(Manage_Frame,text="Genero", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		combo_genero=ttk.Combobox(Manage_Frame,textvariable=self.genero_var , width=9, font=("Arial",15,"bold"),state='readonly')
		combo_genero['values']=("Masculino","Femenino","Otro")
		combo_genero.grid(row=4, column=1,padx=20,pady=10)

		lbl_telefono=Label(Manage_Frame,text="Telefono:", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_telefono.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		txt_telefono=Entry(Manage_Frame,textvariable=self.telefono_var, font=("Arial",15,"bold"), bd=5, relief=GROOVE)
		txt_telefono.grid(row=5,column=1,pady=10,padx=20,sticky="w")

		lbl_fdn=Label(Manage_Frame,text="F.D.N.", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_fdn.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		txt_fdn=Entry(Manage_Frame,textvariable=self.fdn_var, font=("Arial",15,"bold"), bd=5, relief=GROOVE)
		txt_fdn.grid(row=6,column=1,pady=10,padx=20,sticky="w")

		lbl_direccion=Label(Manage_Frame,text="Domicilio:", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_direccion.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		self.txt_direccion=Text(Manage_Frame,width=30,height=4, font=("Arial",10,"bold"))
		self.txt_direccion.grid(row=7,column=1,pady=10,padx=20,sticky="w")

		btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE, bg="blue")
		btn_Frame.place(x=15,y=500,width=420)

		Add_btn=Button(btn_Frame,text="Agregar", width=7, command=self.agregar_estudiantes)
		Add_btn.grid(row=0, column=0, padx=10, pady=10)

		Update_btn=Button(btn_Frame, command=self.update_data, text="Actualizar", width=7)
		Update_btn.grid(row=0, column=1, padx=10, pady=10)

		Delete_btn=Button(btn_Frame,text="Eliminar", width=7, command=self.delete_data)
		Delete_btn.grid(row=0, column=2, padx=10, pady=10)

		Clear_btn=Button(btn_Frame,text="Limpiar", width=7, command=self.clear)
		Clear_btn.grid(row=0, column=3, padx=10, pady=10)

		Detail_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="green")
		Detail_Frame.place(x=550,y=100,width=810,height=580)

		lbl_search=Label(Detail_Frame,text="Buscar por:", bg="yellow", fg="red", font=("Arial",20,"bold"))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		combo_search=ttk.Combobox(Detail_Frame,textvariable=self.buscar_por, width=10, font=("Arial",15,"bold"),state='readonly')
		combo_search['values']=("Matricula","Nombre","Telefono")
		combo_search.grid(row=0, column=2,padx=20,pady=10)

		txt_search=Entry(Detail_Frame,textvariable=self.buscar_txt, width=20, font=("Arial",11,"bold"), bd=5, relief=GROOVE)
		txt_search.grid(row=0,column=3,pady=10,padx=20,sticky="w")

		search_btn=Button(Detail_Frame,text="Buscar", width=7,command=self.buscar_data)
		search_btn.grid(row=0, column=4, padx=10, pady=10)

		showall_btn=Button(Detail_Frame, text="Mostrar Todo", font=("Arial", 9) ,width=7,command=self.fetch_data)
		showall_btn.grid(row=0, column=5, padx=10, pady=10)

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="crimson")
		Table_Frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

		self.Student_table=ttk.Treeview(Table_Frame,columns=("matricula","nombre", "email", "genero", "telefono", "fdn", "domicilio"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("matricula", text="Matricula")
		self.Student_table.heading("nombre", text="Nombre")
		self.Student_table.heading("email", text="Correo E")
		self.Student_table.heading("genero", text="Genero")
		self.Student_table.heading("telefono", text="Telefono")
		self.Student_table.heading("fdn", text="F.D.N.")
		self.Student_table.heading("domicilio", text="Domicilio")
		self.Student_table['show']= 'headings'
		self.Student_table.column("matricula", width=100)
		self.Student_table.column("nombre", width=100)
		self.Student_table.column("email", width=100)
		self.Student_table.column("genero", width=90)
		self.Student_table.column("telefono", width=100)
		self.Student_table.column("fdn", width=100)
		self.Student_table.column("domicilio", width=160)

		self.Student_table.pack(fill=BOTH,expand=1)

		self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

		self.fetch_data()

	def agregar_estudiantes(self):

		if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.fdn_var.get()=="":
			messagebox.showerror("Error", "Todos los campos son requeridos!!!")
		else:

			con=pymysql.connect(host="localhost", user="root",password="",database="stm")
			cur=con.cursor()
			cur.execute("insert into estudiantes values(%s,%s,%s,%s,%s,%s,%s)",(
				self.matricula_var.get(),
				self.nombre_var.get(),
				self.email_var.get(),
				self.genero_var.get(),
				self.telefono_var.get(),
				self.fdn_var.get(),
				self.txt_direccion.get('1.0', END)
				))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Adelante...", "Se agregó correctamente el registro")

	def fetch_data(self):
		con=pymysql.connect(host="localhost", user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from estudiantes")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()

	def clear(self):
		self.matricula_var.set("")
		self.nombre_var.set("")
		self.email_var.set("")
		self.genero_var.set("")
		self.telefono_var.set("")
		self.fdn_var.set("")
		self.txt_direccion.delete("1.0",END)

	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents['values']
		self.matricula_var.set(row[0])
		self.nombre_var.set(row[1])
		self.email_var.set(row[2])
		self.genero_var.set(row[3])
		self.telefono_var.set(row[4])
		self.fdn_var.set(row[5])
		self.txt_direccion.delete("1.0",END)
		self.txt_direccion.insert(END,row[6])

	def update_data(self):
		if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.fdn_var.get()=="":
			messagebox.showerror("Error", "Seleccione el registro a actualizar")
		else:

			con=pymysql.connect(host="localhost", user="root",password="",database="stm")
			cur=con.cursor()
			cur.execute("update estudiantes set nombre=%s,email=%s,genero=%s,telefono=%s,fdn=%s,domicilio=%s where matricula=%s",(
				self.nombre_var.get(),
				self.email_var.get(),
				self.genero_var.get(),
				self.telefono_var.get(),
				self.fdn_var.get(),
				self.txt_direccion.get('1.0', END),
				self.matricula_var.get()
				))
			con.commit()
			self.fetch_data()
			self.clear()
			messagebox.showinfo("Actualizando", "Se actualizó correctamente el registro")
			con.close()

	def delete_data(self):
		if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.fdn_var.get()=="":
			messagebox.showerror("Error", "Seleccione el registro a eliminar")
		else:
			con=pymysql.connect(host="localhost", user="root",password="",database="stm")
			cur=con.cursor()
			cur.execute("delete from estudiantes where matricula=%s",self.matricula_var.get())
			con.commit()
			self.fetch_data()
			self.clear()
			messagebox.showinfo("Eliminar", "Se eliminó correctamente el registro")
			con.close()

	def buscar_data(self):
		con=pymysql.connect(host="localhost", user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from estudiantes where "+str(self.buscar_por.get())+" LIKE '%"+str(self.buscar_txt.get())+"%'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()	

ventana = Tk()
ob=Student(ventana)
ventana.mainloop()