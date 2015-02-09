import sys
import gui
import console
import mixins
import colorpicker
import util
from .qtbinding import loadUi, QT_BINDING, QT_BINDING_MODULES, QT_BINDING_VERSION  # @UnusedImport

# register all binding modules as sub modules of this package.
for module_name, module in QT_BINDING_MODULES.items():
    sys.modules[__name__ + '.' + module_name] = module
    setattr(sys.modules[__name__], module_name, module)
    del module_name
    del module
