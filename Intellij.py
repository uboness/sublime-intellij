import sublime, sublime_plugin
import functools
import os
import shutil

class IntellijCopyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        selection = v.sel();
        if len(selection) == 0:
            v.run_command('expand_selection', { "to": "line" })
        v.run_command('copy')


class IntellijCutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        selection = v.sel();
        if len(selection) == 0:
            v.run_command('expand_selection', { "to": "line" })
        v.run_command('cut')

class IntellijRenameFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        window = self.window
        view = window.active_view()
        filename = view.file_name()
        if filename == None:
            return

        branch, leaf = os.path.split(filename)
        v = window.show_input_panel("New Name:", leaf, functools.partial(self.on_done, filename, branch, view), None, None)
        name, ext = os.path.splitext(leaf)

        v.sel().clear()
        v.sel().add(sublime.Region(0, len(name)))

    def on_done(self, old, branch, view, leaf):
        new = os.path.join(branch, leaf)

        try:
            os.rename(old, new)

            print 'finding open file [' + old + ']'
            # v = self.window.find_open_file(old)
            if view != None:
                view.retarget(new)
        except:
            sublime.status_message("Unable to rename")

class IntellijCopyFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        window = self.window
        view = window.active_view()
        filename = view.file_name()
        if filename == None:
            return

        branch, leaf = os.path.split(filename)
        v = window.show_input_panel("New File Name:", filename, functools.partial(self.on_done, filename), None, None)
        name, ext = os.path.splitext(leaf)

        v.sel().clear()
        start_index = len(filename) - len(leaf)
        v.sel().add(sublime.Region(start_index, start_index + len(name)))

    def on_done(self, src_path, dest_path):

        try:
            shutil.copyfile(src_path, dest_path)
            self.window.open_file(dest_path)
            if view != None:
                view.retarget(new)
        except:
            sublime.status_message("Unable to rename")
