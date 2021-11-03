from androidblobsorganizer.utils.section import Section, register_section

class FmSection(Section):
	name = "FM"
	interfaces = [
		"vendor.qti.hardware.fm",
	]

register_section(FmSection)
