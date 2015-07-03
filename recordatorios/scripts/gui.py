#!/usr/bin/python3
import manejar
from gi.repository import Gtk
from time import localtime


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Recordatorios")
        Gtk.Window.maximize(self)
        #Gtk.Window.set_default_icon_from_file("icono.svg")

        # caja principal vertical
        vbox_ = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self.add(vbox_)

        # caja horizontal; barra de herramientas
        toolbar = Gtk.Toolbar()
        vbox_.pack_start(toolbar, False, True, 0)

        recargar_tbutton = Gtk.ToolButton(Gtk.STOCK_REFRESH, label="Recargar")
        anadir_tbutton = Gtk.ToolButton(Gtk.STOCK_ADD)
        eliminar_tbutton = Gtk.ToolButton(Gtk.STOCK_REMOVE)
        recordar_caja = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                spacing=0)
        switch = Gtk.Switch()
        switch.set_state(True)
        recordar_caja.pack_start(Gtk.Label("Recordar: "), False, True, 0)
        recordar_caja.pack_start(switch, False, True, 0)
        recordar_titem = Gtk.ToolItem()
        recordar_titem.add(recordar_caja)

        recargar_tbutton.connect("clicked", self.actualizar)
        eliminar_tbutton.connect("clicked", self.eliminar)
        anadir_tbutton.connect("clicked", self.anadir)

        toolbar.insert(recordar_titem, 0)
        toolbar.insert(recargar_tbutton, 0)
        toolbar.insert(eliminar_tbutton, 0)
        toolbar.insert(anadir_tbutton, 0)

        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=3)
        vbox_.pack_start(hbox2, False, True, 0)

        # lista de recordatorios
        self.store = Gtk.ListStore(str, int, int, int, int, int)

        self.filas = []

        self.coger_recordatorios()
        for i in range(0, len(self.recordatorios)):
            self.filas.append(self.store.append(self.recordatorios[i][:6]))

        treeview = Gtk.TreeView(self.store)

        renderer = Gtk.CellRendererText()

        nombre = Gtk.TreeViewColumn("Nombre", renderer, text=0)
        anio = Gtk.TreeViewColumn(u"A\u00f1o", renderer, text=1)
        mes = Gtk.TreeViewColumn("Mes", renderer, text=2)
        mdia = Gtk.TreeViewColumn(u"D\u00eda", renderer, text=3)
        hora = Gtk.TreeViewColumn("Hora", renderer, text=4)
        minu = Gtk.TreeViewColumn("Minuto", renderer, text=5)

        treeview.append_column(nombre)
        treeview.append_column(hora)
        treeview.append_column(minu)
        treeview.append_column(mdia)
        treeview.append_column(mes)
        treeview.append_column(anio)

        # caja con todos los recordatorios
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_hexpand(False)
        scrolled.set_vexpand(True)
        scrolled.add(treeview)
        hbox2.pack_start(scrolled, True, True, 0)

        self.select = treeview.get_selection()
        self.select.connect("changed", self.selected)

        # caja de edicion
        ## arriba
        vbox_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        hbox2.pack_start(vbox_1, True, True, 0)

        self.nombre_entry = Gtk.Entry()
        nombre_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        nombre_box.pack_start(Gtk.Label("Nombre"), False, True, 0)
        nombre_box.pack_start(self.nombre_entry, False, True, 0)
        vbox_1.pack_start(nombre_box, False, True, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        vbox_1.pack_start(hbox, False, True, 0)

        adjustment = Gtk.Adjustment(0, 0, 3000, 1, 10, 0)

        self.anio_spinbutton = Gtk.SpinButton()
        self.anio_spinbutton.set_numeric(True)
        self.anio_spinbutton.set_adjustment(Gtk.Adjustment(0, 0, 2100,
                                                           1, 10, 0))
        anio_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        anio_box.pack_start(Gtk.Label(u"A\u00f1o"), False, True, 0)
        anio_box.pack_start(self.anio_spinbutton, False, True, 0)

        self.mes_spinbutton = Gtk.SpinButton()
        self.mes_spinbutton.set_numeric(True)
        self.mes_spinbutton.set_adjustment(Gtk.Adjustment(0, 0, 12, 1, 3, 0))
        mes_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        mes_box.pack_start(Gtk.Label("Mes"), False, True, 0)
        mes_box.pack_start(self.mes_spinbutton, False, True, 0)

        self.mdia_spinbutton = Gtk.SpinButton()
        self.mdia_spinbutton.set_numeric(True)
        self.mdia_spinbutton.set_adjustment(Gtk.Adjustment(0, 0, 31, 1, 7, 0))
        mdia_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        mdia_box.pack_start(Gtk.Label(u"D\u00eda"), False, True, 0)
        mdia_box.pack_start(self.mdia_spinbutton, False, True, 0)

        self.hora_spinbutton = Gtk.SpinButton()
        self.hora_spinbutton.set_numeric(True)
        self.hora_spinbutton.set_adjustment(Gtk.Adjustment(0, 0, 24, 1, 12, 0))
        hora_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        hora_box.pack_start(Gtk.Label("Hora"), False, True, 0)
        hora_box.pack_start(self.hora_spinbutton, False, True, 0)

        self.minu_spinbutton = Gtk.SpinButton()
        self.minu_spinbutton.set_numeric(True)
        self.minu_spinbutton.set_adjustment(Gtk.Adjustment(0, 0, 60, 1, 15, 0))
        minu_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        minu_box.pack_start(Gtk.Label("Minuto"), False, True, 0)
        minu_box.pack_start(self.minu_spinbutton, False, True, 0)

        hbox.pack_start(hora_box, True, True, 0)
        hbox.pack_start(minu_box, True, True, 0)
        hbox.pack_start(mdia_box, True, True, 0)
        hbox.pack_start(mes_box, True, True, 0)
        hbox.pack_start(anio_box, True, True, 0)

        ## abajo
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        hbox_ = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)

        vbox_1.pack_end(hbox_, False, True, 5)
        vbox_1.pack_end(hbox, False, True, 0)

        self.aceptar_button = Gtk.Button("Guardar")
        cancelar_button = Gtk.Button("Cancelar")

        self.aceptar_button.connect("clicked", self.bot_aceptar)
        cancelar_button.connect("clicked", self.selected)

        hbox.pack_start(cancelar_button, True, True, 80)
        hbox.pack_end(self.aceptar_button, True, True, 80)

    def coger_recordatorios(self):
        self.recordatorios = manejar.lista()

    def actualizar(self, button):
        self.store.clear()
        self.filas = []
        self.coger_recordatorios()
        for i in range(0, len(self.recordatorios)):
            self.filas.append(self.store.append(self.recordatorios[i][:6]))

    def anadir(self, button):
        self.aceptar_button.set_label("Nuevo")
        t = localtime()
        self.nombre_entry.set_text("Nuevo recordatorio")
        self.anio_spinbutton.set_value(t.tm_year)
        self.mes_spinbutton.set_value(t.tm_mon)
        self.mdia_spinbutton.set_value(t.tm_mday)
        self.hora_spinbutton.set_value(t.tm_hour)
        self.minu_spinbutton.set_value(0)

    def eliminar(self, button):
        dialog = Confirmar(self)
        response = dialog.run()
        print(response)
        dialog.destroy()
        if response == 1:
            pos = self.model.get_path(self.treeiter).get_indices()[0]
            manejar.eliminar(pos)
            self.actualizar(False)

    def selected(self, selection):
        self.aceptar_button.set_label("Guardar")
        if type(selection) == Gtk.TreeSelection:
            self.model, self.treeiter = selection.get_selected()
            if self.model[self.treeiter] is not None:
                self.nombre_entry.set_text(self.model[self.treeiter][0])
                self.anio_spinbutton.set_value(self.model[self.treeiter][1])
                self.mes_spinbutton.set_value(self.model[self.treeiter][2])
                self.mdia_spinbutton.set_value(self.model[self.treeiter][3])
                self.hora_spinbutton.set_value(self.model[self.treeiter][4])
                self.minu_spinbutton.set_value(self.model[self.treeiter][5])

        elif type(selection) == Gtk.Button:
            self.model, self.treeiter = self.select.get_selected()

            self.nombre_entry.set_text(self.model[self.treeiter][0])
            self.anio_spinbutton.set_value(self.model[self.treeiter][1])
            self.mes_spinbutton.set_value(self.model[self.treeiter][2])
            self.mdia_spinbutton.set_value(self.model[self.treeiter][3])
            self.hora_spinbutton.set_value(self.model[self.treeiter][4])
            self.minu_spinbutton.set_value(self.model[self.treeiter][5])

    def bot_aceptar(self, botton):
        if self.aceptar_button.get_label() == "Guardar":
            pos = self.model.get_path(self.treeiter).get_indices()[0]

            self.store[self.filas[pos]][0] = self.nombre_entry.get_text()
            self.store[self.filas[pos]][1] = self.anio_spinbutton.get_value()
            self.store[self.filas[pos]][2] = self.mes_spinbutton.get_value()
            self.store[self.filas[pos]][3] = self.mdia_spinbutton.get_value()
            self.store[self.filas[pos]][4] = self.hora_spinbutton.get_value()
            self.store[self.filas[pos]][5] = self.minu_spinbutton.get_value()

            manejar.modificar(pos,
                              self.store[self.filas[pos]][0],
                              self.store[self.filas[pos]][1],
                              self.store[self.filas[pos]][2],
                              self.store[self.filas[pos]][3],
                              self.store[self.filas[pos]][4],
                              self.store[self.filas[pos]][5])

        if self.aceptar_button.get_label() == "Nuevo":
            print(self.nombre_entry.get_text())
            manejar.anadir(self.nombre_entry.get_text(),
                           self.anio_spinbutton.get_value(),
                           self.mes_spinbutton.get_value(),
                           self.mdia_spinbutton.get_value(),
                           self.hora_spinbutton.get_value(),
                           self.minu_spinbutton.get_value())
            self.actualizar(Gtk.Button())


class Confirmar(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Confirmar", parent)
        box = self.get_content_area()
        box.add(Gtk.Label("Esta seguro que desea eliminar el recordatorio?"))
        self.add_button("Si", True)
        self.add_button("No", False)
        self.show_all()

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
