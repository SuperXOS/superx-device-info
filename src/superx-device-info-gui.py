#!/usr/bin/python3

# Copyright (C) 2020 Wrishiraj Kaushik <wrix@libresoft.in>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3,
# or (at your option) any later version, as published by the
# Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType


if __name__ == "__main__":

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
 
