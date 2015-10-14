# pytestor is a refactoring tool to replace assertions for use with pytest
# Copyright (C) 2015  Gert Pellin <pellingert@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from termcolor import colored

from refactor.directory import process_directory, iterate_files, command_parser

args = command_parser()
root_dir = process_directory(args.directory)
test_files = iterate_files(root_dir)

imports = []

for file in test_files:
    print(file.get_full_name())
    print('-' * len(file.get_full_name()))
    for line in file.lines:
        if line.assertion is not None:
            print(colored(str(line.line_nr) + ' - ' + line.get_refactor(), 'green'))
        else:
            if 'self.assert' in line.line:
                print(colored(str(line.line_nr) + ' - ' + line.get_refactor(), 'red'))
    print()
    if file.import_pytest:
        imports.append(file)
    file.replace_file()
