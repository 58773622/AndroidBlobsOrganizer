from androidblobsorganizer.utils.section import Section, register_section

class PowerSection(Section):
	name = "Power"
	interfaces = [
		"android.hardware.power",
	]
	hardware_modules = [
		"power",
	]

register_section(PowerSection)
