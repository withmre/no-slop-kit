param(
    [Parameter(Mandatory = $false)]
    [string]$Root = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
$rootPath = (Resolve-Path -LiteralPath $Root).Path

function Report([string]$Name, [scriptblock]$Action) {
    try {
        $result = & $Action
        [pscustomobject]@{ check = $Name; status = 'ok'; evidence = ($result -join '; ') }
    } catch {
        [pscustomobject]@{ check = $Name; status = 'unverified'; evidence = $_.Exception.Message }
    }
}

$checks = @(
    Report 'env-ignore' {
        $ignore = Join-Path $rootPath '.gitignore'
        if (-not (Test-Path -LiteralPath $ignore)) { throw '.gitignore missing' }
        if (-not (Select-String -LiteralPath $ignore -Pattern '^\.env\*' -Quiet)) { throw '.env* is not ignored' }
        'present'
    }
    Report 'docker-compose' {
        $compose = Get-ChildItem -LiteralPath $rootPath -File | Where-Object { $_.Name -match '^(compose|docker-compose).*\.ya?ml$' } | Select-Object -First 1
        if (-not $compose) { 'not-applicable'; return }
        if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { throw 'docker unavailable' }
        & docker compose -f $compose.FullName config --quiet
        'valid'
    }
    Report 'git-secrets' {
        if (-not (Test-Path -LiteralPath (Join-Path $rootPath '.git'))) { 'not-a-git-repository'; return }
        $tracked = & git -C $rootPath ls-files
        if ($tracked | Select-String -Pattern '(^|/)\.env($|\.)') { throw 'tracked environment file found' }
        'no tracked .env file'
    }
)

$checks | ConvertTo-Json -Depth 3
