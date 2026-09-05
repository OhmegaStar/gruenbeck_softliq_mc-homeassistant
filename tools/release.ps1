param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9]+\.[0-9]+\.[0-9]+$')]
    [string]$Version,

    [switch]$Push
)

$ErrorActionPreference = 'Stop'

if (git status --short) {
    throw 'Working tree is not clean. Commit your changes before creating a release.'
}

if (git tag --list "v$Version") {
    throw "Tag v$Version already exists. Choose a new version."
}

$manifestPath = Join-Path $PSScriptRoot '..\custom_components\gruenbeck_softliq_mc\manifest.json'
$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
$oldVersion = $manifest.version
$manifest.version = $Version
$manifest | ConvertTo-Json -Depth 10 | Set-Content $manifestPath -Encoding utf8

git diff --check
git add $manifestPath
git commit -m "Release v$Version"
git tag "v$Version"

if ($Push) {
    git push origin HEAD
    git push origin "v$Version"
}

Write-Host "Version changed from $oldVersion to $Version."
if ($Push) {
    Write-Host "Pushed v$Version. GitHub Actions will create the release."
} else {
    Write-Host "Review the commit, then push with: git push origin HEAD; git push origin v$Version"
}