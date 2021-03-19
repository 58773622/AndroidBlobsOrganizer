from androidblobsorganizer.utils.section import Section, register_section

class ThermalSection(Section):
	name = "Thermal"
	interfaces = [
		"android.hardware.thermal",
	]
	hardware_modules = [
		"thermal",
	]

class ThermalXiaomiSection(Section):
	name = "Thermal (Xiaomi)"
	binaries = [
		"mi_thermald",
	]

register_section(ThermalSection)
register_section(ThermalXiaomiSection)
