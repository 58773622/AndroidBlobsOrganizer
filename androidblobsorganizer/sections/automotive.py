from androidblobsorganizer.utils.section import Section, register_section

class AutomotiveSection(Section):
	name = "Automotive"
	interfaces = [
		"android.hardware.automotive.audiocontrol",
		"android.hardware.automotive.can",
		"android.hardware.automotive.evs",
		"android.hardware.automotive.occupant_awareness",
		"android.hardware.automotive.sv",
		"android.hardware.automotive.veichle",
		"vendor.qti.hardware.automotive.vehicle",
	]

register_section(AutomotiveSection)
