from androidblobsorganizer.utils.section import Section, register_section

class FastbootSection(Section):
	name = "Fastboot"
	interfaces = [
		"android.hardware.fastboot",
	]

register_section(FastbootSection)
