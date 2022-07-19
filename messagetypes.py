'''
MESSAGE_TYPE supported by rtlamr
scm: Standard Consumption Message. Simple packet that reports total consumption.
scm+: Similar to SCM, allows greater precision and longer meter ID's.
idm: Interval Data Message. Provides differential consumption data for previous 47 intervals at 5 minutes per interval.
netidm: Similar to IDM, except net meters (type 8) have different internal packet structure, number of intervals and precision. Also reports total power production.
r900: Message type used by Neptune R900 transmitters, provides total consumption and leak flags.
r900bcd: Some Neptune R900 meters report consumption as a binary-coded digits.

These values define the field location for each reading,
when rtlamr is in CSV output.
'''

IDM_FIELDS = 66
IDM_METER_ID = 9
IDM_CURRENT_READING = 15
IDM_CURRENT_INTERVAL = 10
IDM_MOST_RECENT_INTERVAL_USAGE = 16

SCM_FIELDS = 9
SCM_METER_ID = 3
SCM_CURRENT_READING = 7
