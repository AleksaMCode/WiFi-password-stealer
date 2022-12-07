$Profiles=@()
$Profiles +=(netsh wlan show profiles) | Select-String "\:(.+)$" | Foreach{$_.Matches.Groups[1].Value.Trim()}
$res = $Profiles | Foreach{$SSID = $_ ; (netsh wlan show profile name="$_" key=clear)} |
            Select-String "Key Content\W+\:(.+)$" |
                Foreach{$pass=$_.Matches.Groups[1].Value.Trim(); $_} |
                    Foreach{[PSCustomObject]@{Wireless_Network_Name=$SSID;Password=$pass}}
                        Format-Table -AutoSize
			
Out-File -FilePath .\wifi_pass.txt -InputObject $res -Encoding ASCII -Width 50