import pymel.core as pmc

def main():
    counter = 0
    while(counter>=3):
        cubexform, cubeshape = pmc.polyCube()
        cubexform.translateY.set(1.5+counter)
        counter += 1

class SceneFile(object):
    """Class used to to represent a DCC software scene file

    The class will be a convenient object that we can use to manipulate our 
    scene files. Examples features include the ability to predefine our naming 
    conventions and automatically increment our versions.

    Attributes:
        dir (Path, optional): Directory to the scene file. Defaults to ''.
        descriptor (str, optional): Short descriptor of the scene file. 
            Defaults to "main".
        version (int, optional): Version number. Defaults to 1.
        ext (str, optional): Extension. Defaults to "ma"

    """

    def __init__(self, dir=None, descriptor="main", version=1, ext="ma"):
        self.dir = dir
        self.descriptor = descriptor
        self.version = version
        self.ext = ext

    def basename(self):
        """Return a scene file name.

        e.g. ship_001.ma, car_011.hip

        Returns:
            str: The name of the scene file.

        """
        name_pattern = "{descriptor}_{version:03d}.{ext}"
        name = name_pattern.format(descriptor=self.descriptor,
                                   version=self.version,
                                   ext=self.ext)
        return name

    def path(self):
        """The function returns a path to scene file.

        This includes the drive letter, any directory path and the file name.

        Returns:
            Path: The path to the scene file.

        """
        pass

    def save(self):
        """Saves the scene file.

        Returns:
            Path: The path to the scene file if successful, None, otherwise.

        """
        scenepath = "D:\\C:\\Users\\blake\\OneDrive\\Documents\\toolsdev\\toolsdev_assignment02\\assignment2_save\\"
        pmc.system.saveAS(scenepath+self.basename())

    def increment_and_save(self):
        """Increments the version and saves the scene file.

        If existing versions of a file already exist, it should increment 
        from the largest number available in the folder.

        Returns:
            Path: The path to the scene file if successful, None, otherwise.
        """
        pass