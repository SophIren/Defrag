class Attribute:
    def __init__(self, archive: bool, directory: bool, volume_id: bool,
                 system: bool, hidden: bool, read_only: bool):
        self.volume_id = volume_id
        self.read_only = read_only
        self.system = system
        self.hidden = hidden
        self.directory = directory
        self.archive = archive
