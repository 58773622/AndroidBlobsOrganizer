from androidblobsorganizer.utils.section import Section, register_section

class OemLockSection(Section):
	name = "OEM lock"
	interfaces = [
		"android.hardware.oemlock",
	]

register_section(OemLockSection)
