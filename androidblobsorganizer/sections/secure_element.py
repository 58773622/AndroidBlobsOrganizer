from androidblobsorganizer.utils.section import Section, register_section

class SecureElementSection(Section):
	name = "Secure element"
	interfaces = [
		"android.hardware.secure_element",
		"vendor.qti.secure_element",
	]

class SecureElementESESection(Section):
	name = "Secure element (ESE)"
	interfaces = [
		"vendor.qti.esepowermanager",
	]

register_section(SecureElementSection)
register_section(SecureElementESESection)
