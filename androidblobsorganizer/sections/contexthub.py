from androidblobsorganizer.utils.section import Section, register_section

class ContextHubSection(Section):
	name = "Context hub"
	interfaces = [
		"android.hardware.contexthub",
	]

register_section(ContextHubSection)
