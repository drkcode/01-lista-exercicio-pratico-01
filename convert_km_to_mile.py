def convert_kilometer_to_mile(distance):
    MILE = 1.61
    if distance < 0:
        raise Exception("distance can't be a negative value")

    distance_in_miles = round(distance / MILE, 3)
    return distance_in_miles
