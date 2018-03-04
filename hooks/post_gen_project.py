import urllib
import json
import sys
import io
import zipfile
from contextlib import closing
import requests
from ntpath import basename
import os


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
                        archive.extract(member, "../{{cookiecutter.package_name}}/Source/Assemblies")
            if not hasLicense:
                urllib.URLopener().retrieve("https://raw.githubusercontent.com/pardeike/Harmony/master/LICENSE", "../{{cookiecutter.package_name}}/Source/Assemblies/HARMONY.LICENSE")
            break
        
    except:
        print "Couldn't fetch Harmony:", sys.exc_info()[0]
        sys.exit(1)

    os.remove("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name.replace(' ', '_')}}.cs")
    os.rename("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name.replace(' ', '_')}}.harmony.cs",
              "../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name.replace(' ', '_')}}.cs")
else:
    os.remove("../{{cookiecutter.package_name}}/Source/{{cookiecutter.package_name.replace(' ', '_')}}.harmony.cs")



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
    




print "Everything done! You can open the solution with visual studio now."
