from androidblobsorganizer.utils.section import Section, register_section

class GatekeeperSection(Section):
	name = "Gatekeeper"
	interfaces = [
		"android.hardware.gatekeeper",
	]
	hardware_modules = [
		"gatekeeper",
	]

register_section(GatekeeperSection)
