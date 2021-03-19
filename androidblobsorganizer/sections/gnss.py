from androidblobsorganizer.utils.section import Section, register_section

class GnssSection(Section):
	name = "GNSS"
	interfaces = [
		"android.hardware.gnss",
		"vendor.qti.gnss",
	]
	binaries = [
		"loc_launcher",
		"lowi-server",
		"slim_daemon",
		"xtra-daemon",
		"xtwifi-client",
		"xtwifi-inet-agent",
	]

register_section(GnssSection)
