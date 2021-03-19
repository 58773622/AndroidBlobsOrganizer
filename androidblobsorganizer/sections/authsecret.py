from androidblobsorganizer.utils.section import Section, register_section

class AuthsecretSection(Section):
	name = "Authsecret"
	interfaces = [
		"android.hardware.authsecret",
	]

register_section(AuthsecretSection)
