from androidblobsorganizer.utils.section import Section, register_section

class BootSection(Section):
	name = "Boot"
	interfaces = [
		"android.hardware.boot",
	]

register_section(BootSection)
