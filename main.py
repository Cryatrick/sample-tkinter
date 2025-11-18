from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import session as sess
import mahasiswa as mhs


current_session = sess.Session()

class MainApp :
	def __init__(self, root) :
		self.root = root
		self.login_page()


	def login_process(self) :
		username = self.entry_username.get()
		password = self.entry_password.get()

		if username != "" and password != "" :
			stat_login = current_session.login_user(username,password)

			if stat_login == True :
				messagebox.showinfo("Success", f"Welcome {current_session.user_name}!")
				self.open_main_window()

			else :
				messagebox.showerror("Failed", "Invalid username or password")
		else :
			messagebox.showerror("Failed", "Invalid username or password")

	def login_page(self) :
		self.clear_window()

		self.root.title("Login Page")
		self.root.geometry("300x180")

		ttk.Label(self.root, text="Username:").pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:").pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Login", command=self.login_process).pack(pady=15)

	def open_main_window(self):
		self.clear_window()

		self.root.title("Dashboard")
		self.root.geometry("650x350")

		top_frame = ttk.Frame(self.root)
		top_frame.pack(fill="x", pady=5)

		ttk.Label(top_frame,
		          text=f"Logged in as: {current_session.user_name}",
		          font=("Arial", 12)).pack(side="left", padx=10)

		ttk.Button(top_frame, text="Add New User", command=self.add_user_window).pack(side="right", padx=10)

		ttk.Button(top_frame, text="Logout", command=self.logout).pack(side="right", padx=10)

		self.table = ttk.Treeview(self.root, columns=("No", "Npm", "Nama", "Prodi", "Edit", "Delete"), show="headings")
		self.table.heading("No", text="No")
		self.table.heading("Npm", text="Npm")
		self.table.heading("Nama", text="Nama")
		self.table.heading("Prodi", text="Prodi")
		self.table.heading("Edit", text="Edit")
		self.table.heading("Delete", text="Delete")

		self.table.column("No", width=50)
		self.table.column("Npm", width=100, anchor="center")
		self.table.column("Nama", width=100, anchor="center")
		self.table.column("Prodi", width=100, anchor="center")
		self.table.column("Edit", width=100, anchor="center")
		self.table.column("Delete", width=100, anchor="center")

		self.table.pack(fill="both", expand=True)
		self.table.bind("<ButtonRelease-1>", self.on_table_click)
		self.load_table_data()


	def load_table_data(self):
		for row in self.table.get_children():
			self.table.delete(row)

		all_mahasiswa = mhs.get_all_mahasiswa()
		i = 1
		for mahasiswa in all_mahasiswa:
			self.table.insert("", tk.END, values=(i, mahasiswa.npm_mahasiswa, mahasiswa.nama_mahasiswa, mahasiswa.nama_prodi, "Edit", "Delete"))
			i+= 1


	def add_user_window(self) :
		print("This in ongoing")

	def on_table_click(self, event):
		item = self.table.identify_row(event.y)
		column = self.table.identify_column(event.x)

		if not item:
			return

		_,npm_mahasiswa,_, _, _, _ = self.table.item(item, "values")

		if column == "#5":  
			print(f"Edit {npm_mahasiswa}")
		elif column == "#6":
			print(f"Delete {npm_mahasiswa}")


	def logout(self):
		current_session.logout()
		messagebox.showinfo("Info", "Logged out successfully")
		self.login_page()

	def clear_window(self):
		for widget in self.root.winfo_children():
			widget.destroy()


# ---------- RUN APP ----------
if __name__ == "__main__":
	root = Tk()
	app = MainApp(root)
	root.mainloop()