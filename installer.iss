#define MyAppName "CrystalRET"
#define MyAppVersion "0.9-alpha"
#define MyAppPublisher "Lupix111"
#define MyAppExeName "CrystalRET.exe"
#define MyAppSourceDir "dist\CrystalRET"

[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer_output
OutputBaseFilename=CrystalRET_0.9_alpha_setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
; richiede privilegi admin per installare in Program Files
PrivilegesRequired=admin

[Languages]
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[CustomMessages]
italian.PrerequisitesTitle=Requisiti necessari
italian.PrerequisitesText=Prima di avviare CrystalRET assicurati di:%n%n1. Installare Ollama da ollama.com/download%n%n2. Aprire il terminale e scaricare almeno un modello:%n   ollama pull mistral%n%n3. Al primo avvio CrystalRET scaricherà automaticamente%n   il modello Whisper scelto — serve la connessione internet.%n%nPremi Avanti per continuare l'installazione.
english.PrerequisitesTitle=Requirements
english.PrerequisitesText=Before running CrystalRET make sure to:%n%n1. Install Ollama from ollama.com/download%n%n2. Open a terminal and download at least one model:%n   ollama pull mistral%n%n3. On first launch CrystalRET will automatically download%n   the Whisper model you choose — internet connection required.%n%nClick Next to continue the installation.

[Tasks]
Name: "desktopicon"; Description: "Crea icona sul Desktop"; GroupDescription: "Icone aggiuntive:"; Flags: unchecked

[Files]
; copia tutto il contenuto della cartella dist/CrystalRET
Source: "{#MyAppSourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; shortcut nel menu Start
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
; shortcut sul desktop (opzionale, dipende dalla task)
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
; voce per disinstallare nel menu Start
Name: "{group}\Disinstalla {#MyAppName}"; Filename: "{uninstallexe}"

[Run]
; avvia il programma dopo l'installazione (opzionale)
Filename: "{app}\{#MyAppExeName}"; Description: "Avvia {#MyAppName}"; Flags: nowait postinstall skipifsilent

[Code]
// Controlla se Ollama è installato cercando ollama.exe nel PATH
function OllamaInstallato: Boolean;
var
  ResultCode: Integer;
begin
  Exec('cmd.exe', '/C where ollama > nul 2>&1', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  Result := (ResultCode = 0);
end;

// Viene eseguito prima di mostrare il wizard
function InitializeSetup: Boolean;
var
  ResultCode: Integer;
  
begin
  Result := True;
  if not OllamaInstallato then
  begin
    if MsgBox(
      'Ollama non è installato sul tuo sistema.' + #13#10 + #13#10 +
      'CrystalRET richiede Ollama per funzionare.' + #13#10 +
      'Vuoi aprire la pagina di download di Ollama?' + #13#10 + #13#10 +
      'Puoi installare Ollama ora e poi riprendere questo installer.',
      mbConfirmation,
      MB_YESNO
    ) = IDYES then
    begin
      ShellExec('open', 'https://ollama.com/download', '', '', SW_SHOWNORMAL, ewNoWait, ResultCode);
    end;
    // non blocca l'installazione — l'utente può continuare lo stesso
  end;
end;
