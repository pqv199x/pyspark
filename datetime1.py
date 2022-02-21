from datetime import datetime
 
timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1645002455)
  
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))
print("now:", datetime.now())
diff = (datetime.now() - dt_obj).total_seconds() / 60
print("diff:", diff)