class DisplayConfig:
    def __init__(
        self, res_x, res_y, refresh_rate=60, pos_x=0, pos_y=0, name=None, id=None
    ):
        self.res_x = res_x
        self.res_y = res_y
        self.refresh_rate = refresh_rate
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.id = id

    def __str__(self):
        string = f"Display Configuration for {self.name}"
        string += f"\nID:{self.id}"
        string += f"\nResolution: {self.res_x}x{self.res_y}"
        string += f"\nRefresh Rate: {self.refresh_rate}"
        string += f"\nPosition: X: {self.pos_x} Y:{self.pos_y}"
        return string
