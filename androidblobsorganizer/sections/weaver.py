from androidblobsorganizer.utils.section import Section, register_section

class WeaverSection(Section):
	name = "Weaver"
	interfaces = [
		"android.hardware.weaver",
	]

register_section(WeaverSection)
