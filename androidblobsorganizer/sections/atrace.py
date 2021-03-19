from androidblobsorganizer.utils.section import Section, register_section

class AtraceSection(Section):
	name = "Atrace"
	interfaces = [
		"android.hardware.atrace",
	]

register_section(AtraceSection)
