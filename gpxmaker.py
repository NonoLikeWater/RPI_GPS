class GPX:
    def __init__(self, gpx_type:str=""):
        self.gpx_type = ""
        self.header = ""
        self.footer = ""
        self.body = ""
        self.gpx_file = ""

    def make_header(self, template: str, header_title: str=""):
        self.header = template.format(header_title)

    def append_body(self, template: str, latitude: str = "", longitude: str = "", elevation: str = "", time: str = ""):
        self.body += template.format(lat=latitude, long=longitude, ele=elevation, time=time)

    def make_footer(self,template:str):
        self.footer = template

    def make_gpx_file(self):
        self.gpx_file = f"{self.header}{self.body}{self.footer}"

    def __del__(self):
        del self
