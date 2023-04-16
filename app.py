# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from apps.common.commons.manager import app

if __name__ == '__main__':
    app.run()