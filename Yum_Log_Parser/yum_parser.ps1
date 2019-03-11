$log = Get-Content $args[0] | Out-String;
$split_log = $log.Split("`n");
For ($i = 0; $i -lt $split_log.Length; $i++) {
    $split_split_log = $split_log[$i].Split(' ');
    Write-Host($split_split_log[]);
}
