import os

# List of the Meter IDs to watch
# Use empty brackets to read all meters - []
# List may contain only one entry - [12345678]
# or multiple entries - [12345678, 98765432, 12340123]
env_meters = os.getenv('WATCHED_METERS')
if env_meters:
    WATCHED_METERS = [int(m.strip()) for m in env_meters.split(',')]
else:
    WATCHED_METERS = []

# MQTT Server settings
# If no authentication, leave MQTT_USER and MQTT_PASS empty
MQTT_HOST = os.getenv('MQTT_HOST', '127.0.0.1')
MQTT_PORT = int(os.getenv('MQTT_PORT', '1883'))
MQTT_USER = os.getenv('MQTT_USER', '')
MQTT_PASSWORD = os.getenv('MQTT_PASS', '')

# RTLAMR settings
RTLAMR = os.getenv('RTLAMR', '/amrscm2mqtt/go/bin/rtlamr')
RTLAMR_MSGTYPE = os.getenv('RTLAMR_MSGTYPE', 'all')

# RTL TCP settings
RTL_TCP = os.getenv('RTL_TCP', '/usr/bin/rtl_tcp')
RTL_TCP_LISTEN_ADDRESS = os.getenv('RTL_TCP_LISTEN_ADDRESS', '0.0.0.0')
