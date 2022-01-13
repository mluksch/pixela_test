import datetime

import pixela_service

username = "mluk"
graphname = "test-graph"

try:
    pixela_service.create_user(username)
except Exception as e:
    print(f"error: {e}")

try:
    pixela_service.create_new_graph(username=username, graphname=graphname, unit="count")
except Exception as e:
    print(f"error: {e}")

try:
    pixela_service.create_pixel(username=username, graphname=graphname, quantity="26",
                                date=(datetime.datetime.now() - datetime.timedelta(days=2)))
except Exception as e:
    print(f"error: {e}")

try:
    svg = pixela_service.get_graph_svg_url(username=username, graphname=graphname)
    print(svg)
except Exception as e:
    print(f"error: {e}")

try:
    html = pixela_service.get_graph_html_url(username=username, graphname=graphname)
    print(html)
except Exception as e:
    print(f"error: {e}")

try:
    pixel_info = pixela_service.get_pixel(username=username, graphname=graphname, date=datetime.datetime.now())
    print(pixel_info)
except Exception as e:
    print(f"error: {e}")
