import pathlib

work_dir = pathlib.Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "documents"
destination = pathlib.Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "images"

for file in work_dir.rglob("image?.*"):
     source = pathlib.Path(file)
     source.replace(destination / file.name)
