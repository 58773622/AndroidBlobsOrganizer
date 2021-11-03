from androidblobsorganizer.utils.section import Section, register_section

class WifiDisplaySection(Section):
	name = "Wi-Fi Display"
	interfaces = [
		"com.qualcomm.qti.wifidisplayhal",
		"vendor.qti.hardware.wifidisplaysession",
	]
	apps = [
		"WfdService",
	]
	binaries = [
		"wfdhdcphalservice",
		"wfdservice",
		"wfdvndservice",
		"wifidisplayhalservice",
	]

register_section(WifiDisplaySection)
