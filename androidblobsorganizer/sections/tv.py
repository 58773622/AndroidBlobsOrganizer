from androidblobsorganizer.utils.section import Section, register_section

class TvSection(Section):
	name = "TV"
	interfaces = [
		"android.hardware.tv.cec",
		"android.hardware.tv.input",
		"android.hardware.tv.tuner",
	]
	hardware_modules = [
		"tv_input",
	]

register_section(TvSection)
