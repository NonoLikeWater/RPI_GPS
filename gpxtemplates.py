gpx_header_template = """<?xml version="1.0" encoding="UTF-8"?>
<gpx  version="1.0" creator="gpxmaker -- https://github.com/NonoLikeWater">
  <metadata>
    <name>{}</name>
  </metadata>
  <trk>
    <trkseg>
"""

gpx_body_template = """      <trkpt lat="{lat}" lon="{long}">
        <ele>{ele}</ele>
        <time>{time}</time>
      </trkpt>
"""

gpx_footer_template = """    </trkseg>
  </trk>
</gpx>"""
