from androidblobsorganizer.utils.section import Section, register_section

class AcdbSection(Section):
	name = "ACDB"
	folders = [
		"etc/acdbdata",
	]

register_section(AcdbSection)
