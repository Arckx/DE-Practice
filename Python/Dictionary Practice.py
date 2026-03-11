customer_raw_data = """customer_id,customer_fname,customer_lname,address,city,state,pincode
11599,Mary,Malone,8708 Indian Horse Highway,Hickory,NC,28601
256,David,Rodriguez,7605 Tawny Horse Falls,Chicago,IL,60625
12111,Amber,Franco,8766 Clear Prairie Line,Santa Cruz,CA,95060
8827,Brian,Wilson,8396 High Corners,San Antonio,TX,78240
11318,Mary,Henry,3047 Silent Embers Maze,Caguas,PR,00725"""

customer_header = customer_raw_data.split("\n")[0]
customer_data = customer_raw_data.split("\n")[1:]

print(customer_header)