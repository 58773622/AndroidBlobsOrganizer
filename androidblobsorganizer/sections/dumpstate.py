from androidblobsorganizer.utils.section import Section, register_section

class DumpstateSection(Section):
	name = "Dumpstate"
	interfaces = [
		"android.hardware.dumpstate",
	]

register_section(DumpstateSection)
