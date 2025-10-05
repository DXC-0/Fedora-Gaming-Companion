#!/usr/bin/env python3

import sys
import gi
import subprocess
import os
import threading
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, GLib

path = os.getcwd()

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        self.set_default_size(650, 800)
        self.set_title("Fedora Gaming Companion")

        buttons = [
            ("Mettre à jour le système", self.update, 60),
            ("Installer les dépôts RPM Fusion", self.rpmfusion, 20),
            ("Détecter le GPU et installer le pilote", self.drivers, 20),
            ("Installer les codecs multimédias", self.codecs, 20),
            ("Installer les outils de gaming (Steam, Lutris, Heroic)", self.gaming, 20),
            ("Composants complémentaires (Gamescope, Gamemode, HDR)", self.gamingplus, 20),
            ("Controle du matériel (LACT)", self.oc, 20),
            ("Installer Proton GE", self.protonge, 20),
            ("Installer Proton-CachyOS", self.protoncachy, 20),
            ("Installer un version manager (ProtonPlus)", self.protonplus, 20),
            ("Installation automatisée", self.auto, 20),
            ("Quitter", self.quit, 20),
        ]

        for label, callback, margin_top in buttons:
            button = Gtk.Button(label=label)
            button.connect('clicked', callback)
            button.set_margin_top(margin_top)
            button.set_margin_start(20)
            button.set_margin_end(20)
            self.box1.append(button)

        image = Gtk.Picture.new_for_filename("/bin/gaming-companion/gc-icon.svg")
        image.set_content_fit(Gtk.ContentFit.SCALE_DOWN)
        image.set_size_request(200, 200)
        image.set_margin_top(20)
        image.set_margin_end(80)
        image.set_margin_start(80)
        self.box1.append(image)

    def run_script(self, title, script):
        self.dialog = Gtk.Dialog(title=title, transient_for=self, modal=True)
        self.dialog.set_default_size(300, 100)

        box = self.dialog.get_content_area()
        progress_bar = Gtk.ProgressBar()
        progress_bar.set_pulse_step(0.1)
        box.append(progress_bar)
        self.dialog.show()

        def pulse():
            progress_bar.pulse()
            return True

        GLib.timeout_add(100, pulse)

        def execute():
            cmd = f"pkexec bash -c 'cd \"{path}\" && {script}'"
            subprocess.run(cmd, shell=True)
            GLib.idle_add(self.dialog.destroy)
            return False

        threading.Thread(target=execute).start()

    def update(self, button):
        self.run_script("Mise à jour", "/bin/gaming-companion/scripts/update.sh")

    def rpmfusion(self, button):
        self.run_script("RPM Fusion", "/bin/gaming-companion/scripts/rpm-fusion.sh")

    def drivers(self, button):
        self.run_script("Installation des pilotes", "/bin/gaming-companion/scripts/drivers.sh")

    def codecs(self, button):
        self.run_script("Codecs Multimédias", "/bin/gaming-companion/scripts/codecs.sh")

    def gaming(self, button):
        self.run_script("Applications Gaming", "/bin/gaming-companion/scripts/gaming.sh")

    def gamingplus(self, button):
        self.run_script("Outils complémentaires...", "/bin/gaming-companion/scripts/gaming-plus.sh")

    def oc(self, button):
        self.run_script("Installation de LACT", "/bin/gaming-companion/scripts/overclocking.sh")

    def protonge(self, button):
        self.run_script("Proton GE", "/bin/gaming-companion/scripts/protonge.sh")

    def protoncachy(self, button):
        self.run_script("Proton CachyOS", "/bin/gaming-companion/scripts/protoncachy.sh")

    def protonplus(self, button):
        self.run_script("Proton Manager", "/bin/gaming-companion/scripts/protonplus.sh")

    def auto(self, button):
        scripts = [
            "update.sh", "rpm-fusion.sh", "drivers.sh", "codecs.sh",
            "gaming.sh", "gaming-plus.sh", "protonge.sh",
            "protoncachy.sh", "protonplus.sh", "overclocking.sh"
        ]
        joined = " && ".join(f"/bin/gaming-companion/scripts/{s}" for s in scripts)
        self.run_script("Installation automatisée", joined)

    def quit(self, button):
        print("Quitter")
        self.get_application().quit()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("style.css")

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="Fedora Gaming Toolkit")
app.run(sys.argv)

