import sublime, sublime_plugin

class MakeCleanCommand(sublime_plugin.WindowCommand):
	def run(self,  **args):
		args["file"] = "Packages/User/make_clean.sublime-build"
		self.window.run_command("set_build_system",args)
		self.window.run_command("build")
		args["file"] = "Packages/User/make.sublime-build"
		self.window.run_command("set_build_system",args)
