import tkinter as tk
from tkinter import messagebox, ttk

class AddressBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")
        self.root.geometry("800x500")

        # Data storage (in-memory)
        self.contacts = []

        # UI Layout
        self.setup_ui()

    def setup_ui(self):
        # Frame for form inputs
        form_frame = tk.Frame(self.root, padx=10, pady=10)
        form_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(form_frame, text="Name:", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Phone:", width=10, anchor="w").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(form_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:", width=10, anchor="w").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:", width=10, anchor="w").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(form_frame, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Action Buttons
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Contact", command=self.add_contact).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Contact", command=self.update_contact).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Search Bar
        search_frame = tk.Frame(self.root, padx=10, pady=10)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(search_frame, text="Search:", width=10, anchor="w").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_contact).pack(side=tk.LEFT, padx=5)

        # Contact List
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=100)
        self.tree.column("Email", width=200)
        self.tree.column("Address", width=200)
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.tree.bind("<Double-1>", self.load_selected_contact)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required fields!")
            return

        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        self.update_treeview()
        self.clear_fields()

    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No contact selected for update!")
            return

        index = self.tree.index(selected_item[0])
        self.contacts[index] = {
            "Name": self.name_entry.get().strip(),
            "Phone": self.phone_entry.get().strip(),
            "Email": self.email_entry.get().strip(),
            "Address": self.address_entry.get().strip()
        }
        self.update_treeview()
        self.clear_fields()

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No contact selected for deletion!")
            return

        index = self.tree.index(selected_item[0])
        del self.contacts[index]
        self.update_treeview()
        self.clear_fields()

    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        for contact in self.contacts:
            if query in contact["Name"].lower() or query in contact["Phone"] or query in contact["Email"].lower() or query in contact["Address"].lower():
                self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for contact in self.contacts:
            self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def load_selected_contact(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        index = self.tree.index(selected_item[0])
        contact = self.contacts[index]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact["Name"])

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact["Phone"])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact["Email"])

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, contact["Address"])


if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBook(root)
    root.mainloop()
