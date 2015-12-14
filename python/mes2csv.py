#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    sys.exit("no file given")

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    point = None
    points = []

    for line in lines:

        if line[0:4] == '$$ME':
            continue

        if line[0:2] == 'SL':
            session_name = line[2:36].strip()

        if line[0:2] == 'LY':
            point = {}

            point_number = line[2:20].strip()
            point['point_number'] = point_number

            y_coord = line[24:36].strip()
            point['y_coord'] = y_coord

            eliminated = line[36:41].strip()
            point['eliminated'] = eliminated

            point['session_name'] = session_name

            continue

        if line[0:2] == 'LX':
            x_coord = line[24:36].strip()
            point['x_coord'] = x_coord

            # If y_coord is eliminated, we assume that also y_coord is
            # eliminated.

            continue

        # IT ONLY WORKS IF THERE IS A HEIGHT MEASUREMENT!
        if line[0:2] == 'LH':
            h_coord = line[24:36].strip()
            point['h_coord'] = h_coord

            points.append(point)
            continue


    print 'point_numer' + ';' + 'y_coord' + ';' + 'x_coord' + ';' \
        + 'h_coord' + ';' + 'eliminated' + ';' + 'session_name'
    for meas in points:
        print meas['point_number'] + ';' + meas['y_coord'] + ';' \
            + meas['x_coord'] + ';' + meas['h_coord'] + ';' \
            + meas['eliminated'] + ';' + meas['session_name']
