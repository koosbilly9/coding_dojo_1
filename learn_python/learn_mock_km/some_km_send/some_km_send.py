from pcs_telegram.km.km_connection import KmConnection
import os

def send_to_km_partner(km_partner="test") -> "send some test" :
    snd_telegram = F"TEST TEST"

    km_connection = KmConnection(km_partner)
    km_connection.connect()
    km_connection.send(snd_telegram, "w9_mask1")
    km_connection.disconnect()

    return "Okay"

def call():
    print(f"{os.getcwd()}")