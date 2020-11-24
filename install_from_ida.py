# -*- encoding: utf8 -*-
# 这个脚本的原理是，用pip install下载好资源以后，把plugin.py的主文件丢到用户的plugins下
# 这个还没有完全改好


import idaapi
import os
import sys
from contextlib import contextmanager
import tempfile
import subprocess
import fileinput
import pkg_resources
import shutil

if not "ckxtraceviewer_PACKAGE_LOCATION" in dir():
    ckxtraceviewer_PACKAGE_LOCATION = "ckxtraceviewer"


# Fix the sys.exectuable path. It's misleading in two cases:
#  - On Windows, it's set to 'idaq.exe'.
#  - If a virtualenv is activated with activate_this.py, sys.prefix is changed
#    but sys.executable is still set to the original process. pip and packages
#    will not install in the virtualenv if we don't set it right.
if not hasattr(sys, 'real_executable'):
    sys.real_executable = sys.executable
    if sys.platform == 'win32':
        sys.executable = os.path.join(sys.prefix, 'Python.exe')
    else:
        sys.executable = os.path.join(sys.prefix, 'bin', 'python')
        if sys.version_info.major >= 3:
            # Ready for Python 4?
            sys.executable += str(sys.version_info.major)

# IDA Python sets sys.stdout to a file-like object IDAPythonStdOut. It doesn't
# have things like fileno, close, etc. This helper uses a file and redirect the
# content back to IDA's stdout.
@contextmanager
def temp_file_as_stdout():
    ida_stdout = sys.stdout
    try:
        with tempfile.TemporaryFile() as f:
            sys.stdout = f
            yield
            f.seek(0)
            ida_stdout.write(f.read())
    finally:
        sys.stdout = ida_stdout

try:
    import pip
    print("[+] Using already installed pip (version {:s})".format(pip.__version__))
except ImportError:
    print("[+] Installing pip")
    # pip is built-in Python 3 since 3.4, so we assume Python 2 here
    # We won't support Python >= 3.0 and < 3.4 unless there's a high demand
    import urllib2

    if sys.hexversion < 0x02070900:
        # There are SSL problems with Python version < 2.7.9
        print("[-] ckxtraceviewer installer requires Python 2.7.9 or newer")
        raise Exception("Python >= 2.7.9 required")

    get_pip = urllib2.urlopen("https://bootstrap.pypa.io/get-pip.py").read()
    with temp_file_as_stdout():
        p = subprocess.Popen(
            sys.executable,
            stdin=subprocess.PIPE,
            stdout=sys.stdout,
            stderr=sys.stdout
        )
        p.communicate(get_pip)
    try:
        import pip
    except:
        print("[-] Could not install pip.")
        raise

def pip_install(package, extra_args=[]):
    pip_install_cmd = [ sys.executable, "-m", "pip", "install", "--upgrade" ]
    with temp_file_as_stdout():
        p = subprocess.Popen(
            pip_install_cmd + extra_args + [ package ],
            stdin=subprocess.PIPE,
            stdout=sys.stdout,
            stderr=sys.stdout
        )
        ret = p.wait()
    return ret

if pip_install(ckxtraceviewer_PACKAGE_LOCATION) != 0:
    print("[.] ckxtraceviewer system-wide package installation failed, trying user install")
    if pip_install(ckxtraceviewer_PACKAGE_LOCATION, [ "--user" ]) != 0:
        raise Exception("ckxtraceviewer package installation failed")
    else:
        # If no packages were installed in user site-packages, the path may
        # not be in sys.path in current Python process. Importing ckxtraceviewer will
        # fail until Python (or IDA) is restarted. We can "refresh" sys.path
        # using site.main().
        import site
        if site.getusersitepackages() not in sys.path:
            site.main()

if not os.path.exists(idaapi.get_user_idadir()):
    os.makedirs(idaapi.get_user_idadir(), 0o755)

ida_python_rc_path = os.path.join(idaapi.get_user_idadir(), "idapythonrc.py")
rc_file_content = ""

if os.path.exists(ida_python_rc_path):
    with open(ida_python_rc_path, "r") as rc:
        rc_file_content = rc.read()

if "# BEGIN ckxtraceviewer loading" in rc_file_content:
    print("[.] Old ckxtraceviewer loading script present in idapythonrc.py. Removing.")
    in_ckxtraceviewer_block = False
    for line in fileinput.input(ida_python_rc_path, inplace=1, backup='.ckxtraceviewer_old'):
        if line.startswith("# BEGIN ckxtraceviewer loading code"):
            in_ckxtraceviewer_block = True
        elif line.startswith("# END ckxtraceviewer loading code"):
            in_ckxtraceviewer_block = False
        elif not in_ckxtraceviewer_block:
            sys.stdout.write(line)

ckxtraceviewer_stub_target_path = os.path.join(idaapi.get_user_idadir(), "plugins", "ckxtraceviewer.py")
if not os.path.exists(os.path.dirname(ckxtraceviewer_stub_target_path)):
    os.makedirs(os.path.dirname(ckxtraceviewer_stub_target_path), 0o755)

# Make sure ckxtraceviewer module is not the ckxtraceviewer.py in the plugins folder, otherwise
# pkg_resources will try to get file from there. This happends when package is
# uninstalled, but ckxtraceviewer.py is still in the plugin folder.
if 'ckxtraceviewer' in sys.modules:
    del sys.modules['ckxtraceviewer']

shutil.copyfile(
    pkg_resources.resource_filename("ckxtraceviewer", "ckxtraceviewer_plugin_stub.py"),
    ckxtraceviewer_stub_target_path
)
print("[+] ckxtraceviewer.py added to user plugins")

idaapi.load_plugin(ckxtraceviewer_stub_target_path)

_ida_version = pkg_resources.parse_version(idaapi.get_kernel_version())

if os.name == 'nt' and _ida_version < pkg_resources.parse_version("7.4"):
    # No party for Windows with old IDA
    print("[+] ckxtraceviewer Installation successful. Use <Ctrl-Alt-I> to open the console.")
else:
    print("[🍺] ckxtraceviewer Installation successful. Use <Ctrl-Alt-I> to open the console.")