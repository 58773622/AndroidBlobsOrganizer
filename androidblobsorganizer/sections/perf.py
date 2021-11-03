from androidblobsorganizer.utils.section import Section, register_section

class PerfSection(Section):
	name = "Perf"
	interfaces = [
		"vendor.qti.hardware.perf",
	]
	libraries = [
		"libqti-perfd-client",
	]
	filenames = [
		"powerhint.xml",
	]
	folders = [
		"etc/perf",
	]

class PerfIopSection(Section):
	name = "Perf IOP"
	interfaces = [
		"vendor.qti.hardware.iop",
	]
	libraries = [
		"libqti-iopd-client",
	]

register_section(PerfSection)
register_section(PerfIopSection)
