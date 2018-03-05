# cookiecutter-rimworld-mod-development
My version of [n-fisher's cookiecutter](https://github.com/n-fisher/cookiecutter-rimworld-mod-development).  
Builds the basic Rimworld mod development file structure and sets up a sane build environment.

### Improvements
- Harmony Integration
- Git Integration
- Option to debug in borderless window
- Refactored solution for clarity (especially with About.xml)
- Some other small QOL tweaks


# Install/Setup
### Windows Command Prompt
##### Required Programs
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- `pip install cookiecutter` (or [cookiecutter download link](https://github.com/audreyr/cookiecutter))

##### Usage (inside Rimworld/Mods folder)
1. `cookiecutter gh:L0laapk3/cookiecutter-rimworld-mod-development`
2. `[Answer the prompts]` (If you don't know what something is, leave it empty)
3. Open the folder you just created and double-click the `ModName.sln` file
4. To test, compile as `Debug`. To Release, compile as `Release`
    
### Microsoft Visual Studio Integration (This part is optional)
##### Required Programs

- [Visual Studio Community 2017](https://www.visualstudio.com/downloads/)

##### Install (if no `File -> New -> From Cookiecutter...` option is available)
1. Open up VS Installer (In Visual Studio -> Tools -> Gets Tools and Features)
2. Click Modify
3. Click Individual Components
4. Scroll to Development activities
5. Click the Cookiecutter template support checkbox
6. Click Modify

##### Usage
(Due to a bug in VS, you'll have to make the specific mod's folder in `[...]/Rimworld/Mods/ModName` beforehand)
1. Open Visual Studio
2. `File -> New -> From Cookiecutter...`
3. Search for `rimworld`
4. Double-click `L0laapk3/cookiecutter-rimworld-mod-development`
5. Change the Template Options:
   - `Create To` => `[...]/Rimworld/Mods/mod_name`
   - `Mod name`
   - `Author` (Use your Steam username for automatic linking of mod to profile) (can change later in About-Release.xml)
   - `Mod Description` (not required, can change later in About-Release.xml)
   - `Create blank XML files` (yes/no)
6. `Create and Open Folder`
7. In the Solution Explorer pane that comes up on the right, double click your `ModName.sln` file
8. In the new Solution Explorer view that comes up, right click `RimWorldWin` and click `Set as Startup Project`
9. Due to a bug in VS, you'll have to delete the folder `[...]/Rimworld/Mods/ModName - Release` after you create the project. Otherwise, you will receive an error message whenever you start the game before the first time that you build VS in Release mode.


# Basic Features

### VS Setup Automation
- Links Rimworld and UnityEngine .dlls for importing in code
- Sets build events to automate file management of About-$Version.xml for tagging development versions.
- Clears the default set debugging and trace constants
- Creates a VS solution with correctly defined paths
- Clicking `Start ▶️` will preform the designated build sequence and start Rimworld.exe tied to a Visual Studio resource monitor.

# Advanced Features
### Debug/Release Versioning
blabla
  
### Optional Debug Save Profile
<Temporarily removed>
