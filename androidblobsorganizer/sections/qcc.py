from androidblobsorganizer.utils.section import Section, register_section

class QccSection(Section):
	name = "QCC"
	interfaces = [
		"vendor.qti.hardware.qccsyshal",
		"vendor.qti.hardware.qccvndhal",
	]

register_section(QccSection)
