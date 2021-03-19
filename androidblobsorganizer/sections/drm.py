from androidblobsorganizer.utils.section import Section, register_section

class DrmSection(Section):
	name = "DRM"
	interfaces = [
		"android.hardware.drm",
	]
	libraries = [
		"liboemcrypto",
	]
	folders = [
		"lib/mediacas",
		"lib/mediadrm",
		"lib64/mediacas",
		"lib64/mediadrm",
	]

register_section(DrmSection)
