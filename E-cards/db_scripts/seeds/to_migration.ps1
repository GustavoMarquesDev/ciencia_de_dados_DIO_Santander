$scriptDirectory = Split-Path $MyInvocation.MyCommand.Definition -Parent

outputFile = Join-Path $scriptDirectory -ChildPath "migration.sql"

if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name

foreach ($sqlFile in $sqlFiles) {
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile "Go" | Out-File -Append -FilePath $outputFile
}

Write-Host "Todos os arquivos foram combinados em $outputFile"