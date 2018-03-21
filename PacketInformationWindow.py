import gtk

class PacketInformationWindow(gtk.Dialog):

    def __init__(self, parent):

        super(PacketInformationWindow, self).__init__(parent=parent)
        self.set_title("Packet Information")
        self.set_size_request(460,100)

        #Table
        table = gtk.Table(5, 6)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        valueLbl = gtk.Label("Value")
        table.attach(valueLbl, 0, 1, 0, 1)

        textDescLbl = gtk.Label("Text Description")
        table.attach(textDescLbl, 1, 5, 0, 1)

        valueTxt = gtk.TextView()
        valueTxt.set_size_request(220,20)
        table.attach(valueTxt, 0, 1, 1, 2)

        textDescTxt = gtk.TextView()
        textDescTxt.set_size_request(220,20)
        table.attach(textDescTxt, 1, 5, 1, 2)

        fixed = gtk.Fixed()
        fixed.put(table, 5, 10)
        fixed.show_all()

        self.vbox.add(fixed)
        self.run()
        self.destroy()
