#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import json

from uuid import uuid1
from xdg import BaseDirectory
from xdg.DesktopEntry import DesktopEntry

from lib.utils import desktop_environment


APP_NAME = 'compartir'
APP_PREFERENCES_FILE = 'preferences.json'


class Data(object):
    def __init__(self, data):
        self.__dict__.update(data)


class Preferences(object):
    def __init__(self):
        self._app_path = BaseDirectory.save_config_path(APP_NAME)
        self._file = os.path.join(self._app_path, APP_PREFERENCES_FILE)

        self._desktop = desktop_environment()

        self.compartir = None
        self.profile = None

        self._load()

    def _load(self):
        if not os.path.isfile(self._file):
            data = {
                'profile': {
                    'name': 'Alumno',
                    'description': 'usando Huayra!',
                },
                'compartir': {
                    'user': uuid1().hex,
                    'autostart': True
                }
            }
            with open(self._file, 'w') as fd:
                fd.write(json.dumps(data))

        with open(self._file, 'r') as fd:
            _ = json.loads(fd.read())
            self.compartir = Data(_['compartir'])
            self.profile = Data(_['profile'])

    def save(self):
        data = {
            'compartir': self.compartir.__dict__,
            'profile': self.profile.__dict__
        }

        with open(self._file, 'w') as fd:
            fd.write(json.dumps(data))

        self._update_autostart_flag()

    def _update_autostart_flag(self):
        if self._desktop == 'unknown':
            # No se puede autostartear :(
            return

        desktop_compartir = DesktopEntry(
            os.path.join(BaseDirectory.save_config_path('autostart'),
            'compartir.desktop')
        )

        if self._desktop == 'mate':
            desktop_compartir.set(
                'X-MATE-Autostart-enabled',
                'true' if self.compartir.autostart else 'false'
            )
            desktop_compartir.write()


