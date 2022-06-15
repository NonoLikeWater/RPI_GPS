#!/bin/python3
import serial
from gpxmaker import GPX
from datetime import datetime
from coords_converter import coords_converter
from gpxtemplates import *

# ----- Initialisation liaison série -----
ser = serial.Serial("/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_7_-_GPS_GNSS_Receiver-if00", 9600, parity=serial.PARITY_EVEN)

# ----- Initialisation date pour nom du document -----
date_debut = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# ----- Initialisation des variables pour les compteurs -----
number_of_request_before_save = 60
i = 0

# ----- Initialisation de l'objet GPX -----
gpx_file = GPX()
gpx_file.make_header(gpx_header_template, f"Tracé du {date_debut}")
gpx_file.make_footer(gpx_footer_template)

# ----- Boucle de traitement -----
while True:
    # ------ Lecture de la liaison série -----
    line = ser.readline()
    
    # ----- Traitement des lignes de la liaison série -----
    data = str(line).split(",")
    if data[0] == "b'$GPGGA":
        
        # ----- Vérification de la présence des données -----
        if data[2] != "" and data[3] != "" and data[4] != "" and data[5] != "" and data[9] != "" :

            # ----- Initialisation date pour la coordonée -----
            date_now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

            # ----- Incrémentation du compteur de cycle -----
            i = i + 1

            # ----- Affectation des données au variables -----
            raw_latitude = f"{data[2]} {data[3]}"
            raw_longitude = f"{data[4]} {data[5]}"
            elevation = data[9]
            
            # ----- Converstion des coordonées -----
            parsed_latitude, parsed_longitude = coords_converter("NMEA", "DD", raw_latitude, raw_longitude)

            # ----- Ajout de la data à l'objet GPX -----
            gpx_file.append_body(gpx_body_template, parsed_latitude, parsed_longitude, elevation, date_now)

            # ----- Traitement du fichier gpx -----
            if i == number_of_request_before_save:
                # ----- Declaration du fichier -----
                with open(f"/home/pi/traces/trace_{date_debut}.gpx", "w") as file :

                    # ----- Génération du xml gpx -----
                    gpx_file.make_gpx_file()

                    # ----- Ecriture du xml gpx dans le fichier -----
                    file.write(gpx_file.gpx_file)

                # ----- Réinitialisation du comnpteur -----
                i = 0
