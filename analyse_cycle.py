import os
import json
import csv
import matplotlib.pyplot as plt
import datetime


def load_station_data(station, date, data_directory=None):
    with open('MY1_station_20090101.json') as file:
        data = json.load(file)

    fulldict = {}

    mydict = {'Station': station, 'date': date}

    IndDict = {}
    with open('MY1_cycleCount_20090101.csv') as c:
        r = csv.DictReader(c)

        for row in r:
            # These Three lines extract the time from the row and loops the other values where each row has the time
            # as a key. i.e matching format of conditions where each row is a dict and the individual time value is
            # the key.

            index = row['TIME']
            row.pop('TIME')
            IndDict[index] = row

    print(IndDict['00:01:35'])
    conditions_read = data['data']  # Take Key Value from Date followed by time, to just Time in loop  through this dict

    conditions = {}

    for key, value in conditions_read.items():
        # Trying to get time in same format as the csv document (Precision is two d.p higher in csv)
        Time = key.replace(" ", "")[-5:] + ":00"
        conditions[Time] = value
    print(Time)

    fulldict['metadata'] = mydict
    fulldict['conditions'] = conditions
    fulldict['IndividualCount'] = IndDict
    print(fulldict['conditions'])
    conditions = data['data']

    return {'metadata': mydict,
            'cyclecount': IndDict,
            'conditions': conditions}


def pollutant_at_origin(value_station, distance):
    # Pollution on the road = [1 + (distance to the station)^2] . (Pollution at the station)

    a = 1 + (distance ** 2)
    b = value_station

    pollutant_origin = 0

    if len(a) == 1:
        pollutant_origin = a * b

    else:
        for a, b in zip(a, b):
            pollutant_origin = pollutant_origin + a * b

    return pollutant_origin


def pollutant_at_distance(pollutant_origin, distance):
    # values of pollution at ANY distance

    vals_pol = pollutant_origin / (1 + (distance ** 2))

    return vals_pol


def bin_times(list_times, interval):

    # bin the data at the same intervals that the station measures for pollutants at the stations
    # different intervals at different stations
    # interval input should be an integer indicating the length of time in minutes, default should be 15 minutes
    # function should return the number of cyclists that pass through the counter in the interval requested,
    # starting from and including midnight
    # output should be a list of tuples
    # each tuple should have 2 elements - the starting date and time
    # times should be represented using datetime objects from Python’s built-in date-time module (imported above)

    x = 0

    return x


def get_observation_rate(observation_times):

    # produce the observation time (interval integer of that specific station)
    observation_rate = 0

    return observation_rate


def plot_cyclist_pollution(input_data, save=...):
    # input_data is the output of load_station_data for the specific function

    fig = plt.plot()

    return fig


def decompose_wind(wind_speed, wind_direction, movement):

    decomposition = wind_speed * wind_direction

    return decomposition


def plot_cyclist_wind(input_data, save=...):
    raise NotImplementedError


def calculate_faster_rider(input_data):
    raise NotImplementedError


def save_rain_cyclists_speed(input_data, output_directory):
    raise NotImplementedError
