@echo off
rem .\ex start A04 ^| .\ex check ^| .\ex run ^| .\ex next ^| .\ex list
dotnet run --project "%~dp0tools\ex" -v q -- %*
