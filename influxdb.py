#!/usr/bin/python3
###############################################
# Copyright by IT Stall (www.itstall.de) 2018 #
# Author:   Dennis Eisold                     #
# Created:  05.10.2018                        #
###############################################

import datetime, time, json, subprocess, sys, time, argparse
from influxdb import InfluxDBClient

influx_host = "IP Adresse"
influx_user = "Benutzername"
influx_pass = "Passwort"
influx_db = "Datenbank"
influx_port = 8086

parser = argparse.ArgumentParser(description='Pixelflut to InfluxDB.')
parser.add_argument('--rx', help='RX Bandwith')
parser.add_argument('--tx', help='TX Bandwith')
parser.add_argument('--mp', help='MegaPixel')
parser.add_argument('--ps', help='P/S')
parser.add_argument('--con', help='Connections')
parser.add_argument('--debug', default=False, help='Debug true/false')
args = parser.parse_args()

if(args.debug):
        print("write to influxDB: pixelflut(rx:"+args.rx+" tx:"+args.tx+" mp:"+args.mp+" ps:"+args.ps+" con:"+args.con+")")
json_body = [{
        "measurement": "pixelflut",
        "fields": {
                "rx": float(args.rx),
                "tx": float(args.tx),
                "mp": float(args.mp),
                "ps": float(args.ps),
                "con": float(args.con),
        }
}]
dbclient = InfluxDBClient(influx_host, influx_port, influx_user, influx_pass, influx_db)
dbclient.write_points(json_body)