@echo off
setlocal enableextensions disabledelayedexpansion
for /f "delims=" %%i in ('type "About.xml" ') do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    set "lin=!line:^</name^>= - Dev Build^</name^>!"
    >>"out.xml" echo(!lin:^</description^>=test%!^)^</description^>!
    endlocal
)