import gtk

class ReferenceListWindow(gtk.Dialog):

    def __init__(self, parent):

        super(ReferenceListWindow, self).__init__(parent=parent)
        self.set_title("Reference List [Reference List Name]")
        self.set_size_request(470,100)

        #Table
        table = gtk.Table(5, 6)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        refListNameLbl = gtk.Label("Reference List Name")
        table.attach(refListNameLbl, 0, 1, 0, 1)

        refListNameTxt = gtk.TextView()
        refListNameTxt.set_size_request(300,20)
        table.attach(refListNameTxt, 1, 5, 0, 1)

        valueLbl = gtk.Label("Value")
        table.attach(valueLbl, 0, 1, 1, 2)

        textDescLbl = gtk.Label("Text Description")
        table.attach(textDescLbl, 1, 5, 1, 2)

        valueTxt = gtk.TextView()
        valueTxt.set_size_request(150,20)
        table.attach(valueTxt, 0, 1, 2, 3)

        textDescTxt = gtk.TextView()
        textDescTxt.set_size_request(150,20)
        table.attach(textDescTxt, 1, 5, 2, 3)

        fixed = gtk.Fixed()
        fixed.put(table, 5, 10)
        fixed.show_all()

        self.vbox.add(fixed)
        self.run()
        self.destroy()
