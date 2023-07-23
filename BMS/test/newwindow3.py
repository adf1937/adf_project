def OnDoubleClick(self, treeView):
    # First check if a blank space was selected
    entryIndex = treeView.focus()
    if '' == entryIndex:
        return

    # Set up window
    win = Toplevel()
    win.title("Edit Entry")
    win.attributes("-toolwindow", True)

    ####
    # Set up the window's other attributes and geometry
    ####

    # Grab the entry's values
    for child in treeView.get_children():
        if child == entryIndex:
            values = treeView.item(child)["values"]
            break

    col1Lbl = Label(win, text="Value 1: ")
    col1Ent = Entry(win)
    col1Ent.insert(0, values[0])  # Default is column 1's current value
    col1Lbl.grid(row=0, column=0)
    col1Ent.grid(row=0, column=1)

    col2Lbl = Label(win, text="Value 2: ")
    col2Ent = Entry(win)
    col2Ent.insert(0, values[1])  # Default is column 2's current value
    col2Lbl.grid(row=0, column=2)
    col2Ent.grid(row=0, column=3)

    col3Lbl = Label(win, text="Value 3: ")
    col3Ent = Entry(win)
    col3Ent.insert(0, values[2])  # Default is column 3's current value
    col3Lbl.grid(row=0, column=4)
    col3Ent.grid(row=0, column=5)

    def UpdateThenDestroy():
        if ConfirmEntry(treeView, col1Ent.get(), col2Ent.get(), col3Ent.get()):
            win.destroy()

    okButt = Button(win, text="Ok")
    okButt.bind("<Button-1>", lambda e: UpdateThenDestroy())
    okButt.grid(row=1, column=4)

    canButt = Button(win, text="Cancel")
    canButt.bind("<Button-1>", lambda c: win.destroy())
    canButt.grid(row=1, column=5)


def ConfirmEntry(self, treeView, entry1, entry2, entry3):
    ####
    # Whatever validation you need
    ####

    # Grab the current index in the tree
    currInd = treeView.index(treeView.focus())

    # Remove it from the tree
    DeleteCurrentEntry(treeView)

    # Put it back in with the upated values
    treeView.insert('', currInd, values=(entry1, entry2, entry3))

    return True


def DeleteCurrentEntry(self, treeView):
    curr = treeView.focus()

    if '' == curr:
        return

    treeView.delete(curr)
