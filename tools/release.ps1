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

$lastTag = git tag --sort=-version:refname | Select-Object -First 1
if (-not $lastTag) {
    throw 'No previous release tag found. Create an initial release tag manually first.'
}

$commitMessages = @(git log "$lastTag..HEAD" --format='- %s (%h)')
$fileChanges = @(git diff --stat "$lastTag..HEAD")
if ($commitMessages.Count -eq 0) {
    throw "No commits found since $lastTag. Add and commit changes before creating a release."
}

$date = Get-Date -Format 'yyyy-MM-dd'
$changelogEntry = @(
    "## [$Version] - $date"
    '### Changed'
    $commitMessages
    ''
    '### Files changed'
    '```text'
    $fileChanges
    '```'
    ''
) -join "`n"

$changelogPath = Join-Path $PSScriptRoot '..\CHANGELOG.md'
$changelog = Get-Content $changelogPath -Raw
$unreleasedMarker = '## [Unreleased]'
if (([regex]::Matches($changelog, '(?m)^## \[Unreleased\]')).Count -ne 1) {
    throw 'CHANGELOG.md does not contain an Unreleased section.'
}
$changelog = $changelog.Replace($unreleasedMarker, "$changelogEntry$unreleasedMarker")
Set-Content $changelogPath $changelog -Encoding utf8

$manifestPath = Join-Path $PSScriptRoot '..\custom_components\gruenbeck_softliq_mc\manifest.json'
$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
$oldVersion = $manifest.version
$manifest.version = $Version
$manifest | ConvertTo-Json -Depth 10 | Set-Content $manifestPath -Encoding utf8

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) "gruenbeck_softliq_mc-$Version"
$artifactPath = Join-Path ([System.IO.Path]::GetTempPath()) "gruenbeck_softliq_mc-$Version.zip"

if (Test-Path $tempRoot) {
    Remove-Item $tempRoot -Recurse -Force
}
if (Test-Path $artifactPath) {
    Remove-Item $artifactPath -Force
}

New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
Copy-Item -Path (Join-Path $repoRoot 'custom_components') -Destination (Join-Path $tempRoot 'custom_components') -Recurse -Force
Copy-Item -Path (Join-Path $repoRoot 'hacs.json') -Destination (Join-Path $tempRoot 'hacs.json') -Force
Compress-Archive -Path (Join-Path $tempRoot 'custom_components'), (Join-Path $tempRoot 'hacs.json') -DestinationPath $artifactPath -Force

Write-Host "Release payload archive created at: $artifactPath"
Write-Host "Archive contains only custom_components/ and hacs.json."

git diff --check
git add $manifestPath $changelogPath
git commit -m "Release v$Version"
git tag "v$Version"

if ($Push) {
    git push origin HEAD
    git push origin "v$Version"
}

Write-Host "Version changed from $oldVersion to $Version."
Write-Host "Changelog generated from $lastTag..HEAD."
if ($Push) {
    Write-Host "Pushed v$Version. GitHub Actions will create the release."
} else {
    Write-Host "Review the commit, then push with: git push origin HEAD; git push origin v$Version"
}