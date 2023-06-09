# main.py
#
# Copyright 2023 Timofey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        center_box = Gtk.CenterBox()
        center_box.set_center_widget(self.box2)

##добавление кнопки
        self.button = Gtk.Button(label="Установить Wireguard")
        self.button.connect('clicked', self.hello)
##добавление окон ввода текста (логина, ip и пароля)

        self.ip_entry = Gtk.Entry()
        self.ip_entry.set_text("Введите ip-адрес сервера")
        server_ip = self.ip_entry.get_text()
        self.login_entry = Gtk.Entry()
        self.login_entry.set_text("Введите имя пользователя сервера")
        server_login = self.login_entry.get_text()
        self.passwd_entry = Gtk.PasswordEntry()
        self.passwd_entry.set_text("Введите пароль")
        server_passwd = self.passwd_entry.get_text()

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        ##self.box1.append(self.box3)  # And another one, empty for now

        self.box2.append(self.ip_entry)
        self.box2.append(self.login_entry)
        self.box2.append(self.passwd_entry)
        self.box2.append(self.button) # Put button in the first of the two vertial boxes

        self.set_default_size(1200, 500)
        self.set_child(center_box)
        self.set_title("MyApp")
    def hello(self, button):
        print("Hello world") ##нужно будет заменить на вызов WG
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
def main(version):
    """The application's entry point."""
    app = MyApp()
    return app.run(sys.argv)
