import urllib
import json
import sys
import io
import zipfile
from contextlib import closing
import requests
from ntpath import basename
import os
import subprocess
import win32com.client


try:
    if not os.path.exists("../new.bat"):
        with open("../new.bat", "w") as file:
            file.write("@echo off\ncookiecutter gh:L0laapk3/cookiecutter-rimworld-mod-development\nif %errorlevel% NEQ 0 pause")
except:
    pass
              
if '{{cookiecutter.include_harmony}}'[0].lower() == 'y':
    
    print "Fetching latest Harmony release info.."
    try:
        url = "https://api.github.com/repos/pardeike/Harmony/releases/latest"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        for asset in data['assets']:
            if "release" not in asset['name'].lower():
                continue
            print "Downloading latest Harmony.."
            r = requests.get(asset['browser_download_url'], stream=True)
            hasLicense = False
            with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:
                for member in archive.infolist():
                    if "license" in member.filename.lower():
                        member.filename = "HARMONY.LICENSE"
                        archive.extract(member, "../{{cookiecutter.package_name}}/Source/Assemblies")
                        hasLicense = True
                    if (".dll" in member.filename.lower()):
                        member.filename = basename(member.filename)
                        archive.extract(member, "../{{cookiecutter.package_name}}/Source/About/Licenses")
            if not hasLicense:
                urllib.URLopener().retrieve("https://raw.githubusercontent.com/pardeike/Harmony/master/LICENSE", "../{{cookiecutter.package_name}}/Source/About/Licenses/HARMONY.LICENSE")
            break
        
    except:
        print "Couldn't fetch Harmony:", sys.exc_info()[0]
        sys.exit(1)

    os.remove("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name}}.cs")
    os.rename("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name}}.harmony.cs",
              "../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name}}.cs")
else:
    os.remove("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name}}.harmony.cs")



if '{{cookiecutter.init_git}}'[0].lower() == 'y':
    print "Initiating git.."
    try:
        original = os.getcwd()
        os.chdir("../{{cookiecutter.package_name}}")
        os.system("git init")
        os.chdir(original)
    except:
        print "Could not initiate git. Maybe the 'git' command is not installed?\n", sys.exc_info()[0]
else:
    os.remove("../{{cookiecutter.package_name}}/.gitignore")
    os.remove("../{{cookiecutter.package_name}}/README.md")
    


objShell = win32com.client.Dispatch("WScript.Shell")
vs = objShell.SpecialFolders("StartMenu") + "\\Visual Studio 2017.lnk"
if not os.path.exists(vs):
    vs = objShell.SpecialFolders("AllUsersPrograms") + "\\Visual Studio 2017.lnk"
if not os.path.exists(vs):
    print "Everything done! You can open the solution with visual studio now."
else:
    try:
        vs = objShell.CreateShortCut(vs).Targetpath
        subprocess.Popen([vs,
                          os.path.abspath("../{{cookiecutter.package_name}}/{{cookiecutter.package_name}}.sln"),
                          os.path.abspath("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name}}.cs")])
        print "Everything done! Starting Visual Studio.."
    except:
        print "Everything done! You can open the solution with visual studio now."




