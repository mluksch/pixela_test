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
