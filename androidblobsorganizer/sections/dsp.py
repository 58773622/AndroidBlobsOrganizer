from androidblobsorganizer.utils.section import Section, register_section

class DspSection(Section):
	name = "DSP"
	interfaces = [
		"vendor.qti.hardware.dsp",
	]
	binaries = [
		"dspservice",
	]

register_section(DspSection)
