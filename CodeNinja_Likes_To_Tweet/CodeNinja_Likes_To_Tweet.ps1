$num_first_bloods = 0;
$num_twitter_web_clients = 0;
$num_twitter_for_iphones = 0;

Get-ChildItem $args[0] -Filter *.json | 
    Foreach-Object {
        $name = (ConvertFrom-Json -InputObject (Get-Content $_.FullName | Out-String)).source

        if ($name.IndexOf("First-Blood-Bot") -gt -1) {
            $num_first_bloods += 1;
        } elseif($name.IndexOf("Twitter Web Client") -gt -1) {
            $num_twitter_web_clients += 1;
        } elseif ($name.IndexOf("Twitter for iPhone") -gt -1) {
            $num_twitter_for_iphones += 1;
        }
    }

$output = "First-Blood-Bot:" + $num_first_bloods + "`n" +
    "Twitter Web Client:" + $num_twitter_web_clients + "`n" +
    "Twitter for iPhone:" + $num_twitter_for_iphones;

Write-Host($output)