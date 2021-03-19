from androidblobsorganizer.utils.section import Section, register_section

class ConsumerIrSection(Section):
	name = "ConsumerIr"
	interfaces = [
		"android.hardware.ir",
	]
	hardware_modules = [
		"consumerir",
	]

register_section(ConsumerIrSection)
