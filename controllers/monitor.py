import win32api
from contextlib import suppress
import pywintypes
import win32con
import json
import ctypes


class DisplayHelper:
    def __init__(self):
        pass
        # self.displays = self.list_displays()
        # user32 = ctypes.windll.user32
        # user32.SetProcessDPIAware()

    def get_config(self):
        display_infos = {}
        for rdrc_id, display_enum in enumerate(win32api.EnumDisplayMonitors()):
            pyhandle = display_enum[0]
            logical_info = win32api.GetMonitorInfo(pyhandle)
            config = win32api.EnumDisplaySettingsEx(
                logical_info["Device"], win32con.ENUM_CURRENT_SETTINGS
            )
            # device = win32api.EnumDisplayDevices(display_info["Device"])
            logical_width = logical_info["Monitor"][2] - logical_info["Monitor"][0]
            original_width = config.PelsWidth
            scale = original_width / logical_width
            display_device = win32api.EnumDisplayDevices(logical_info["Device"])

            logical_width = logical_info["Monitor"][2] - logical_info["Monitor"][0]
            logical_height = logical_info["Monitor"][3] - logical_info["Monitor"][1]
            display_infos[rdrc_id] = {
                "rdrc_id": rdrc_id,
                "logical_name": logical_info["Device"],
                "hardware_id": display_device.DeviceID,
                "logical_width": logical_width,
                "logical_height": logical_height,
                "actual_width": logical_width * scale,
                "actual_heigth": logical_height * scale,
                "refresh_rate": config.DisplayFrequency,
                "x": logical_info["Monitor"][0],
                "y": logical_info["Monitor"][1],
                "scale": scale,
            }

        return display_infos

    def get_hardware_config(self, rdrc_id):
        configs = self.get_config()
        config = configs.get(rdrc_id)
        print(config)
        print(rdrc_id)
        print(config)
        if config:
            return config
        return False

    def disable_monitor(self, device_name):
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = 0
        devmode.PelsHeight = 0
        devmode.Position_x = 0
        devmode.Position_y = 0

        devmode.Fields = (
            win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT | win32con.DM_POSITION
        )
        win32api.ChangeDisplaySettingsEx(
            device_name, devmode, win32con.CDS_UPDATEREGISTRY
        )
        # win32api.ChangeDisplaySettingsEx(device_name, devmode, (win32con.CDS_NORESET | win32con.CDS_UPDATEREGISTRY))
        # win32api.ChangeDisplaySettingsEx(device_name, None, win32con.CDS_UPDATEREGISTRY)

    def set_display_config(
        self,
        device_name,
        width,
        height,
        refresh_rate,
        position_x=None,
        position_y=None,
        active=False,
    ):
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = width
        devmode.PelsHeight = height
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        if position_x:
            devmode.Position_x = int(position_x)
            devmode.Position_y = int(position_y)
            devmode.Fields |= win32con.DM_POSITION
        if refresh_rate:
            devmode.DisplayFrequency = refresh_rate
            devmode.Fields |= win32con.DM_DISPLAYFREQUENCY

        if active:
            win32api.ChangeDisplaySettingsEx(
                device_name, devmode, win32con.CDS_RESET | win32con.CDS_UPDATEREGISTRY
            )
        else:
            win32api.ChangeDisplaySettingsEx(
                device_name,
                devmode,
                (win32con.CDS_NORESET | win32con.CDS_UPDATEREGISTRY),
            )
            win32api.ChangeDisplaySettingsEx(
                device_name, None, win32con.CDS_UPDATEREGISTRY
            )
