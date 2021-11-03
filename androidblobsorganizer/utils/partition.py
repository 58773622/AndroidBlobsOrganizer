from androidblobsorganizer.utils.ignore import is_blob_allowed
from pathlib import Path

(
	SYSTEM,
	PRODUCT,
	SYSTEM_EXT,
	VENDOR,
	ODM,
) = range(5)

PARTITION_STRING = {
	SYSTEM: "system",
	SYSTEM_EXT: "system_ext",
	PRODUCT: "product",
	ODM: "odm",
	VENDOR: "vendor",
}

PROPRIETARY_FILES_PARTITION_PREFIX = {
	SYSTEM: "",
	SYSTEM_EXT: "system_ext/",
	PRODUCT: "product/",
	ODM: "odm/",
	VENDOR: "vendor/",
}

(
	SSI,
	TREBLE,
) = range(2)

SSI_PARTITIONS = [
	SYSTEM,
	PRODUCT,
	SYSTEM_EXT,
]

TREBLE_PARTITIONS = [
	VENDOR,
	ODM,
]

def get_dir(path: Path):
	dir = {}
	for i in path.iterdir():
		dir[i.name] = i if i.is_file() else get_dir(i)
	return dir

class AndroidPartition:
	def __init__(self, partition: int, real_path: str, dump_path: Path):
		self.partition = partition
		self.real_path = real_path
		self.dump_path = dump_path

		self.files: list[str] = []
		self.proprietary_files_prefix = PROPRIETARY_FILES_PARTITION_PREFIX[self.partition]
		self.group = SSI if self.partition in SSI_PARTITIONS else TREBLE

	def fill_files(self, files: list[str]):
		path_prefix = f"{self.real_path}/"
		for file in files:
			if not file.startswith(path_prefix):
				continue

			file = file.removeprefix(path_prefix)
			if not is_blob_allowed(file):
				continue

			self.files.append(file)

	def get_formatted_file(self, file: str):
		return f"{self.proprietary_files_prefix}{file}"

	def get_formatted_files(self):
		return [self.get_formatted_file(file) for file in self.files]
