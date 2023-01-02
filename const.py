LOGIN_URL = "https://www.95598.cn/osgweb/login"
ELECTRIC_USAGE_URL = "https://www.95598.cn/osgweb/electricityCharge"
BALANCE_URL = "https://www.95598.cn/osgweb/userAcc"

SUPERVISOR_URL = "http://supervisor/core"
API_PATH = "/api/states/"

BALANCE_SENSOR_NAME = "sensor.electricity_charge_balance"
DAILY_USAGE_SENSOR_NAME = "sensor.last_electricity_usage"
YEARLY_USAGE_SENSOR_NAME = "sensor.yearly_electricity_usage"
YEARLY_CHARGE_SENESOR_NAME = "sensor.yearly_electricity_charge"
BALANCE_UNIT = "CNY"
USAGE_UNIT = "KWH"
BALANCE_STATE_CLASS = "measurement"
DAILY_USAGE_STATE_CLASS = "measurement"
USAGE_DEVICE_CLASS = "energy"
YEARLY_USAGE_STATE_CLASS = "total_increasing"

BALANCE_SENSOR_FRIENDLY_NAME = "电费余额"
DAILY_USAGE_SENSOR_FRIENDLY_NAME = "近日用电量"
YEARLY_USAGE_SENSOR_FRIENDLY_NAME = "今年用电量"
YEARLY_CHARGE_SENSOR_FRIENDLY_NAME = "今年电费"

JOB_INTERVAL_HOURS = 12  # Please DO NOT make it too frequently.
DRIVER_IMPLICITY_WAIT_TIME = 20
RETRY_TIMES_LIMIT = 5
LOGIN_EXPECTED_TIME = 10
RETRY_WAIT_TIME_OFFSET_UNIT = 10
