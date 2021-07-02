import cx_Freeze

executables = [cx_Freeze.Executable("Coherence.pyw")]

cx_Freeze.setup(
	name = "MemoryCoherence" ,
	options = {"build_exe":{"packages":["pygame"],
	"include_files":["Ta Da-SoundBible.com-1884170640.wav",
	"Background.png",
	"Button.png",
	"Gray Arrow.png",
	"Green Arrow.png",
	"Purple Arrow.png",
        "Red Arrow.png",
        "White Arrow.png",
        "Yellow Arrow.png"]}},
	executables = executables
	)
