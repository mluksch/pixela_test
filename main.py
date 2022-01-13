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
                                date=(datetime.datetime(year=2022, month=1, day=12)))
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
    pixel_info = pixela_service.get_pixel(username=username, graphname=graphname,
                                          date=datetime.datetime(year=2022, month=1, day=12))
    print(f"get pixel : {pixel_info}")
except Exception as e:
    print(f"error: {e}")

try:
    pixel_info = pixela_service.update_pixel(username=username, graphname=graphname,
                                             date=datetime.datetime(year=2022, month=1, day=12), quantity="99")
    print(f"update pixel : {pixel_info}")
except Exception as e:
    print(f"error: {e}")

try:
    pixel_info = pixela_service.get_pixel(username=username, graphname=graphname,
                                          date=datetime.datetime(year=2022, month=1, day=12))
    print(f"get pixel : {pixel_info}")
except Exception as e:
    print(f"error: {e}")

try:
    pixel_info = pixela_service.delete_pixel(username=username, graphname=graphname,
                                             date=datetime.datetime(year=2022, day=12, month=1))
    print(f"deleted : {pixel_info}")
except Exception as e:
    print(f"error: {e}")

try:
    pixel_info = pixela_service.get_pixel(username=username, graphname=graphname,
                                          date=datetime.datetime(year=2022, day=12, month=1))
    print(f"get pixel : {pixel_info}")
except Exception as e:
    print(f"error: {e}")
