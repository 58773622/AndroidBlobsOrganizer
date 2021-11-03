from androidblobsorganizer.utils.section import Section, register_section

class SensorsSection(Section):
	name = "Sensors"
	interfaces = [
		"android.hardware.sensors",
		"vendor.qti.hardware.sensorscalibrate",
	]
	hardware_modules = [
		"sensors",
	]
	binaries = [
		"init.qcom.sensors.sh",
		"sensors.qti",
		"sscrpcd",
	]
	patterns = [
		"lib(64)?/sensors\..*\.so",
	]

class SensorsConfigsSection(Section):
	name = "Sensors configs"
	folders = [
		"etc/sensors",
	]

register_section(SensorsSection)
register_section(SensorsConfigsSection)
