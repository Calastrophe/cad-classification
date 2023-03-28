### This is the file for parsing and extracting nodes from the parsed file
from helpers import LOGGER, level_contents
from digraph import Node
from pathlib import Path

class STPFile:
    def __init__(self, file: Path):
        self.file_path = file
        self.data: list[str] = []
        self.headers: list[str] = []
        self.parse()
        self.construct_nodes()

    def parse(self):
        with open(self.file_path, "r") as fd:
            file_str = fd.read()
            ## This is a nice four line way to splice off the header and data sections without the extra junk.
            split_file = file_str.split("DATA;")
            header, data = split_file[0].split('HEADER;')[1], split_file[1]
            header, data = header.split('ENDSEC;')[0], data.split('ENDSEC;')[0]
            self.headers, self.data = header.split('\n')[1:-1], data.split('\n')[1:-1]
            # The list comprehension [1:-1] is to remove leftover "" from splitting at \n.

    def construct_nodes(self):
        for object in self.data:
            # Level the contents of the string based on parathenses
            leveled_contents = level_contents(object)
            id_and_type: list[str] = "".join(leveled_contents[0]).split('=')
            node_id = id_and_type[0].strip()
            node_type = id_and_type[1].strip()
            node_parameters = []
            for i, parameter in leveled_contents.items():
                if i != 0: # Skip the ID and type level
                    if parameter: # Gets rid of [''] things in lists
                        node_parameters.append(parameter)
            print(node_parameters)


        
    # Prints out the contents of the data section of the file.
    # Something like #118 = PLANE(#117) ... so on
    def __repr__(self):
        output_string = ""
        for object in self.data:
            output_string += object + "\n"
        return output_string


if __name__ == "__main__":
    some_stp = STPFile("data/example.stp")
