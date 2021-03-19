from androidblobsorganizer import __version__ as version, current_path
from androidblobsorganizer.androiddump import AndroidDump
from argparse import ArgumentParser
from pathlib import Path

def main():
	print(f"Android blobs organizer\n"
		  f"Version {version}\n")

	parser = ArgumentParser(prog='python3 -m androidblobsorganizer')
	parser.add_argument("dump_path", type=Path,
						help="path to an Android dump made with dumpyara")
	parser.add_argument("-o", "--output", type=Path, default=current_path / "proprietary-files.txt",
						help="custom output file")

	args = parser.parse_args()

	dump = AndroidDump(args.dump_path)
	dump.dump_to_file(args.output)
