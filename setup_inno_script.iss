; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Headlines
AppVersion=1.5
WizardStyle=modern
DefaultDirName={autopf}\Headlines
DefaultGroupName=Headlines
UninstallDisplayIcon={app}\MyProg.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output
ChangesEnvironment=yes

[CustomMessages]
AppAddPath=Add application directory to your environmental path (required)
      
[Files]
Source: "headlines.exe"; DestDir: "{app}"
Source: "main.py"; DestDir: "{app}"

Source: "updateNews.py"; DestDir: "{app}"
Source: "news.json"; DestDir: "{app}"
Source: "newstitles.json"; DestDir: "{app}"

Source: "appGui.py"; DestDir: "{app}"

Source: "python-3.9.0-amd64.exe"; DestDir: "{app}"
Source: "vcredist_x86.exe"; DestDir: "{app}"
Source: "PyQt5-5.15.4-cp36.cp37.cp38.cp39-none-win_amd64.whl"; DestDir: "{app}"
Source: "PyQt5-5.15.4-cp36.cp37.cp38.cp39-none-win32.whl"; DestDir: "{app}"
Source: "installpyqt5.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\headlines"; Filename: "{app}\headlines.exe"
                
[Registry]
Root: HKCU; Subkey: "SOFTWARE\Classes\Applications\headlines.exe\shell\open\command"; Flags: uninsdeletekeyifempty
Root: HKCU; Subkey: "SOFTWARE\Classes\Applications\headlines.exe\shell\open\command"; Flags: uninsdeletekey
Root: HKCU; Subkey: "SOFTWARE\Classes\Applications\headlines.exe\shell\open\command"; ValueType: string; ValueName: "Default"; ValueData: "py {app}\headlines.exe"
Root: "HKCU"; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPathHKCU(ExpandConstant('{app}'))



[Tasks]
Name: python; Description: "Install Python 3.9+" 
Name: PyQt5Library; Description: "Install PyQt5" 
Name: VisualC; Description: "Install Microsoft Visual C++ 2010" 

[Code]

procedure InstallVisualC(Path: string);
var
  ErrorCode: Integer;
  Result1: Boolean;
begin
          Result1 := MsgBox('This tool requires Microsoft Visual C++ 2010  to run.  Do you want to install it now ?', mbConfirmation, MB_YESNO) = IDYES;
          if Result1
          then ShellExec('', Path, '', '', SW_SHOW, ewWaitUntilTerminated, ErrorCode)

end;

procedure Python3Install(Path: string);
var
  ErrorCode: Integer;
  Result1: Boolean;
begin
          Result1 := MsgBox('This tool requires python 3.9 Runtime Environment  to run.  Do you want to install it now ?', mbConfirmation, MB_YESNO) = IDYES;
          if Result1
          then ShellExec('', Path, '', '', SW_SHOW, ewWaitUntilTerminated, ErrorCode)

end;

procedure PyQt5LibraryInstall(Path: string);
var
  ErrorCode: Integer;
  Result1: Boolean;
begin
          Result1 := MsgBox('This tool requires PyQt5 library  to run.  Do you want to install it now ?', mbConfirmation, MB_YESNO) = IDYES;
          if Result1
          then if not ShellExec('', Path, '', '', SW_SHOW, ewWaitUntilTerminated, ErrorCode) then
          begin
              Log('ErrorCode: ' + IntToStr(ErrorCode))
          end;

end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
    if (CurStep = ssPostInstall) and IsTaskSelected('python')
    then Python3Install(Expandconstant('{app}\python-3.9.0-amd64.exe'));
    if (CurStep = ssPostInstall) and IsTaskSelected('PyQt5Library')
    then PyQt5LibraryInstall(Expandconstant('{app}\installpyqt5.exe'));
    if (CurStep = ssPostInstall) and IsTaskSelected('VisualC')
    then InstallVisualC(Expandconstant('{app}\vcredist_x86.exe'));
    end;

function NeedsAddPathHKCU(Param: string): boolean;
var
OrigPath: string;
begin
if not RegQueryStringValue(HKEY_CURRENT_USER,
'Environment',
'Path', OrigPath)
then begin
Result := True;
exit;
end;
// look for the path with leading and trailing semicolon
// Pos() returns 0 if not found
Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;