import _const as const
from _util import get_sensor
import wmi

def get_cpu():
    import pythoncom
    sensors = []

    pythoncom.CoInitialize()
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")

    sensors_infos = w.Sensor()
    for sensor in sensors_infos:
        if sensor.SensorType == "Temperature":
            sensor_name = const.SENSOR_NAME_TEMPERATURE_NAME.format(sensor.Name)
            sensor_value = {
                const.SENSOR_NAME_TEMPERATURE_CURRENT: sensor.Value,
                const.SENSOR_NAME_TEMPERATURE_MAX: sensor.Max
            }
            sensors.append(get_sensor(sensor_name, sensor_value))

        elif sensor.Name == "CPU Total":
            sensor_name = const.SENSOR_NAME_CPU_USAGE_NAME.format(sensor.Name)
            sensor_value = {
                const.SENSOR_NAME_CPU_USAGE_CURRENT : sensor.Value,
                const.SENSOR_NAME_CPU_USAGE_MAX :  sensor.Max
            }
            sensors.append(get_sensor(sensor_name, sensor_value))

        elif sensor.SensorType == "Power":
            sensor_name = const.SENSOR_NAME_CPU_USAGE_POWER.format(sensor.Name)
            sensor_value = {
                const.SENSOR_NAME_CPU_USAGE_POWER_CURRENT : sensor.Value,
                const.SENSOR_NAME_CPU_USAGE_POWER_MAX :  sensor.Max
            }
            sensors.append(get_sensor(sensor_name, sensor_value))

        elif sensor.SensorType == "Clock":
            sensor_name = const.SENSOR_NAME_CPU_CLOCK.format(sensor.Name)
            sensor_value = {
                const.SENSOR_NAME_CPU_CLOCK_CURRENT : sensor.Value,
                const.SENSOR_NAME_CPU_CLOCK_MAX :  sensor.Max
            }
            sensors.append(get_sensor(sensor_name, sensor_value))

    return sensors
