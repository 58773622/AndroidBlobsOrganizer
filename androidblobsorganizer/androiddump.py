from androidblobsorganizer.utils.reorder import reorder_key
from androidblobsorganizer.utils.section import Section
from androidblobsorganizer.utils.partition import TREBLE_PARTITIONS, AndroidPartition, PARTITION_STRING
from androidblobsorganizer.utils.partition import ODM, PRODUCT, SYSTEM, SYSTEM_EXT, VENDOR
from androidblobsorganizer.utils.section import sections
from pathlib import Path

class AndroidDump:
	def __init__(self, path: Path):
		self.path = path

		self.all_files_txt = self.path / "all_files.txt"
		self.all_files = [file for file in self.all_files_txt.open().read().splitlines()]
		                  #if (self.path / file).is_file()]
		self.all_files = list(dict.fromkeys(self.all_files))
		self.all_files.sort(key=reorder_key)

		# Determine partitions
		self.system = None
		self.product = None
		self.system_ext = None
		self.vendor = None
		self.odm = None

		for system in ["system", "system/system"]:
			if f"{system}/build.prop" in self.all_files:
				self.system = AndroidPartition(SYSTEM, system, self.path)

		if self.system is None:
			raise FileNotFoundError("System not found")

		for vendor in [f"{self.system.real_path}/vendor", "vendor"]:
			if f"{vendor}/build.prop" in self.all_files:
				self.vendor = AndroidPartition(VENDOR, vendor, self.path)

		if self.vendor is None:
			raise FileNotFoundError("Vendor not found")

		self.product = self.search_for_partition(PRODUCT)
		self.system_ext = self.search_for_partition(SYSTEM_EXT)
		self.odm = self.search_for_partition(ODM)

		self.partitions: list[AndroidPartition] = [
			partition for partition in [
				self.system,
				self.product,
				self.system_ext,
				self.vendor,
				self.odm,
			] if partition is not None
		]

		for partition in self.partitions:
			partition.fill_files(self.all_files)

		self.sections: list[Section] = [section() for section in sections]
		for section in self.sections:
			for partition in self.partitions:
				section.add_files(partition)

		misc_section = Section()

		for partition in self.partitions:
			if partition.partition not in TREBLE_PARTITIONS:
				continue

			misc_section.add_files(partition)

		self.sections.append(misc_section)

		self.build_description = None
		for line in (self.path / self.vendor.real_path / "build.prop").open().read().splitlines():
			if line.startswith("ro.vendor.build.fingerprint="):
				self.build_description = line.removeprefix("ro.vendor.build.fingerprint=")

	def dump_to_file(self, file: Path):
		with file.open("w") as f:
			f.write(f"# Unpinned blobs from {self.build_description}\n")
			for section in self.sections:
				if not section.files:
					continue

				f.write(f"\n# {section.name}\n")
				f.writelines([f"{file}\n" for file in section.files])

	def search_for_partition(self, partition: int):
		result = None
		possible_locations = [f"{self.system}/{PARTITION_STRING[partition]}",
							  f"{self.vendor}/{PARTITION_STRING[partition]}",
							  PARTITION_STRING[partition]]

		for location in possible_locations:
			if (f"{location}/build.prop" in self.all_files
				or f"{location}/etc/build.prop" in self.all_files):
				result = AndroidPartition(partition, location, self.path)

		return result

	def search_file_in_partitions(self, file: str):
		files = []
		for file in [f"{partition.real_path}/{file}" for partition in self.partitions]:
			if file in self.all_files:
				files.append(file)
		return files
