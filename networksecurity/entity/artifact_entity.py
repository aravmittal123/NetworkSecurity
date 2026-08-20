from dataclasses import dataclass


@dataclass
class DataIngestionArtfact:
    trained_file_path:str
    test_file_path:str