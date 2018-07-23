import gameconnection as gc

conn = gc.GameConnection()
conn.connect()
cmd = {"Type": "Ship", "Subject": "", "Action": "List", "Arguments": []}
responce = conn.run_command(cmd)
print(responce)
ship = responce["ResultObject"][0]
cmd = {"Type": "Ship", "Subject": ship["Name"], "Action": "Observe", "Arguments": []}
responce = conn.run_command(cmd)
print(responce)
dest = responce["ResultObject"]["Hyperlanes"][0]
cmd = {"Type": "Ship", "Subject": ship["Name"], "Action": "Move", "Arguments": [dest]}
responce = conn.run_command(cmd)
print(responce)
