from androidblobsorganizer.utils.section import Section, register_section

class NeuralNetworksSection(Section):
	name = "Neural networks"
	interfaces = [
		"android.hardware.neuralnetworks",
	]

register_section(NeuralNetworksSection)
