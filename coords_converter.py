def coords_converter(input_type: str, output_type: str, latitude, longitude):
    """
    possible if :
        NMEA DD
        NMEA DM
        NMEA DMS
        DD DM
        DD DMS
        DM DD
        DM DMS
        DMS DD
        DMS DM

    possible conversion :
        NMEA DD
        DD DM
        DD DMS
        DM DD
        DM DMS
        DMS DD
        DMS DM
    """

    if input_type and output_type:

        # FROM          NMEA        TO       DD
        if input_type == "NMEA" and output_type == "DD":
            return nmea_to_dd(latitude, longitude)

#        # FROM          NMEA        TO       DM
#        elif input_type == "NMEA" and output_type == "DM":
#            print(1)
#
#        # FROM          NMEA        TO       DMS
#        elif input_type == "NMEA" and output_type == "DMS":
#            print(1)
#
#        # FROM          DD        TO       DM
#        elif input_type == "DD" and output_type == "DM":
#            print(1)
#
#        # FROM          DD        TO       DMS
#        elif input_type == "DD" and output_type == "DMS":
#            print(1)
#
#        # FROM          DM        TO       DD
#        elif input_type == "DM" and output_type == "DD":
#            print(1)
#
#        # FROM          DM        TO       DMS
#        elif input_type == "DM" and output_type == "DMS":
#            print(1)
#
#        # FROM          DMS        TO       DD
#        elif input_type == "DMS" and output_type == "DD":
#            print(1)
#
#        # FROM          DMS        TO       DM
#        elif input_type == "DMS" and output_type == "DM":
#            print(1)

        else:
            print("Accepted values for input_type are NMEA, DD, DM, DMS and output_type are DD, DM, DMS")
            exit(1)

    else:
        print("Values can't be null")
        return False

    return str(latitude), str(longitude)


def nmea_to_dd(latitude, longitude):
    """

    :param latitude:
    :param longitude:
    :return: latitude, longitude
    """

    # Decoupage du string en 2 variables
    latitude, cp_lat = str(latitude).split(" ")
    longitude, cp_long = str(longitude).split(" ")

    # Calcul de la latitude | from nmea to dd
    p_lat1 = latitude[0] + latitude[1]
    p_lat2 = latitude[2] + latitude[3]
    p_lat3 = "0." + latitude.split('.')[1]
    latitude = int(p_lat1) + (int(p_lat2) / 60) + ((float(p_lat3) * 60) / 3600)

    # Calcul de la longitude | from nmea to dd
    p_long1 = longitude[0] + longitude[1] + longitude[2]
    p_long2 = longitude[3] + longitude[4]
    p_long3 = "0." + longitude.split('.')[1]
    longitude = int(p_long1) + (int(p_long2) / 60) + ((float(p_long3) * 60) / 3600)

    # Verif points cardinal non null
    if cp_lat and cp_long:
        # Verif points cardinal dans la range de valeur
        if cp_lat in ["N", "S"] and cp_long in ["E", "W"]:
            # Modification de la latitude en fonction du point cardinal
            if cp_lat == "S":
                latitude = "-" + str(latitude)
            # Modification de la longitude en fonction du point cardinal
            if cp_long == "W":
                longitude = "-" + str(longitude)

        else:
            print("Cardinal point format is not correct.")
            return False


    else:
        print("Wrong data ! Latitude or longitude cardinal point needed.")
        return False

    return str(latitude), str(longitude)


"""
def dd_to_dm(latitude, longitude):
def dd_to_dms(latitude, longitude):
def dm_to_dd(latitude, longitude):
def dm_to_dms(latitude, longitude):
def dms_to_dd(latitude, longitude):
def dms_to_dm(latitude, longitude):
"""
