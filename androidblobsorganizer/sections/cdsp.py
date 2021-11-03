from androidblobsorganizer.utils.section import Section, register_section

class CdspSection(Section):
	name = "CDSP"
	interfaces = [
		"vendor.qti.cdsprpc",
	]
	binaries = [
		"cdsprpcd",
	]
	libraries = [
		"libcdsprpc",
		"libcdsp_default_listener",
		"libfastcvdsp_stub",
		"libfastcvopt",
	]

register_section(CdspSection)
