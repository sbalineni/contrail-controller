#
# Copyright (c) 2017 Juniper Networks, Inc. All rights reserved.
#

"""
This file contains utility method for importing all plugin imeplementations for 
self registration. All plugins must be imported before DeviceConf invokes plugin
registrations. Please add an entry here if there is a new plugin
"""
def import_plugins():
    from juniper_conf import JuniperConf
    from mx_conf import MxConf
    from qfx_conf import QfxConf
# end import_plugins
