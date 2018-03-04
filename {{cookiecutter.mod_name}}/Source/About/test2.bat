@echo off
setlocal enableextensions disabledelayedexpansion
for /f "delims=" %%i in ('type "D:\NIET illegaal\RimWorld.v0.18.1722\Mods\TEST\Source\About\About.xml" ') do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    set lin=!line:^</name^>= - Dev Build^</name^>!
    >>"D:\NIET illegaal\RimWorld.v0.18.1722\Mods\TEST\Assemblies\..\About\About.xml" echo(!lin:^</description^>=^

^(This is the dev version of TEST. The release version of About.xml is available for editing at About/About-Release.xml. Edits made on this file or on the temporary About/About.xml won't show up on the release version. Use VisualStudio to build a "Release" version of this mod when ready to upload your mod^!^)^</description^>!
    endlocal
)