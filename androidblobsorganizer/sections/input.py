from androidblobsorganizer.utils.section import Section, register_section

class InputSection(Section):
	name = "Input"
	interfaces = [
		"android.hardware.input",
	]

register_section(InputSection)
