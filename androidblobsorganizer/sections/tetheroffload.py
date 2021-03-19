from androidblobsorganizer.utils.section import Section, register_section

class TetherOffloadSection(Section):
	name = "Tether offload"
	interfaces = [
		"android.hardware.tetheroffload.config",
		"android.hardware.tetheroffload.control",
	]

register_section(TetherOffloadSection)
