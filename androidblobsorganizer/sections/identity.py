from androidblobsorganizer.utils.section import Section, register_section

class IdentitySection(Section):
	name = "Identity"
	interfaces = [
		"android.hardware.identity",
	]

register_section(IdentitySection)
