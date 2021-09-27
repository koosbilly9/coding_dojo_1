from pcs_telegram.km.km_connection import KmConnection

km_connection = KmConnection("TEST")
km_connection.connect()
km_connection.send("Text telegram here", sender_name="koos")

km_connection.disconnect()