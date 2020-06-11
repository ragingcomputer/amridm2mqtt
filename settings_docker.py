"""Get our settings from os.environ to facilitate running in Docker.
"""
import os

# Sanity checks
all_keys_found = True
for key in ['WATCHED_METERS']:
    if key not in os.environ:
        all_keys_found = False
        print("Can't find key {0}, did you pass `-e {0}=<value>` to `docker run`?".format(key))

if not all_keys_found:
    print("\nPlease set the environment variables above.")
    exit(1)

# List of the Meter IDs to watch
# Use empty brackets to read all meters - []
# List may contain only one entry - [12345678]
# or multiple entries - [12345678, 98765432, 12340123]
power_meters = os.environ['WATCHED_METERS'].replace(',', ' ').split(' ')
WATCHED_METERS = [int(meter_id) for meter_id in power_meters]

# multiplier to get reading to Watt Hours (Wh)
# examples:
#   for meter providing readings in kWh
#      MULTIPLIER = 1000
#   for meter providing readings in kWh
#   with 2 extra digits of precision
#      MULTIPLIER = 10
# MULTIPLIER needs to be a number
WH_MULTIPLIER = int(os.environ.get('WH_MULTIPLIER', 1000))

# number of IDM intervals per hour reported by the meter
# examples:
#   for meter providing readings every 5 minutes
#   or 12 times every hour
#     READINGS_PER_HOUR = 12
#   for meter providing readings every 15 minutes
#   or 12 times every hour
#     READINGS_PER_HOUR = 4
READINGS_PER_HOUR = int(os.environ.get('READINGS_PER_HOUR', 12))

# MQTT Server settings
# MQTT_HOST needs to be a string
# MQTT_PORT needs to be an int
# MQTT_USER needs to be a string
# MQTT_PASSWORD needs to be a string
# If no authentication, leave MQTT_USER and MQTT_PASSWORD empty
MQTT_HOST = os.environ.get('MQTT_HOST', '127.0.0.1')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
MQTT_USER = os.environ.get('MQTT_USER', '')
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD', '')

# path to rtlamr
RTLAMR = '/root/go/bin/rtlamr'

# path to rtl_tcp
RTL_TCP = '/usr/bin/rtl_tcp'
