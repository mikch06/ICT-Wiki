--- 
date: 2020-06-16 00:00:00
category: checkmk
tags: checkmk, plugins
---
# Checkmk: Show current logins

### Linux
    #!/bin/bash
    # Check who's online
    # mki, 2020.06.16
    
    SERVICE="Current_Logins"
    WHO=$( who |awk {' printf "%s ", $1'} )
    CHECK=$( who |wc -l)
    
    if [ $CHECK == 0 ]
    then
        STATUS="0"
    elif [ ! -z $CHECK ]
    then
        STATUS="1"
    fi
    
    echo "$STATUS $SERVICE count=$CHECK $CHECK Logged in: $WHO "

### Windows
Path on Windows: C:\ProgramData\checkmk\agent\local\current_logins.ps1

    #################################################################
    # mki, 2020.06.30
    # fork of cmk ms-logins plugin 
    # https://exchange.checkmk.com/p/ms-logins
    #################################################################
    
    Function Get-ComputerSessions {
    
    [cmdletbinding(
        DefaultParameterSetName = 'session',
        ConfirmImpact = 'low'
    )]
        Param(
            [Parameter(
                Mandatory = $False,
                Position = 0,
                ValueFromPipeline = $True)]
                [string[]]$Computer
                )
    Begin {
        $report = @()
        }
    Process {
        If ($Computer -eq $null) {
            $Computer = "localhost"
            }
        ForEach($c in $Computer) {
            # Parse 'query session' and store in $sessions:
            $sessions = query session /server:$c
                1..($sessions.count -1) | % {
                    $temp = "" | Select Computer,SessionName, Username, Id, State, Type, Device
                    $temp.Computer = $c
                    $temp.SessionName = $sessions[$_].Substring(1,18).Trim()
                    $temp.Username = $sessions[$_].Substring(19,20).Trim()
                    $temp.Id = $sessions[$_].Substring(39,9).Trim()
                    $temp.State = $sessions[$_].Substring(48,8).Trim()
                    $temp.Type = $sessions[$_].Substring(56,12).Trim()
                    $temp.Device = $sessions[$_].Substring(68).Trim()
                    $report += $temp
                }
            }
        }
    End {
        $report
        }
    }
    
    $User_Sessions = Get-ComputerSessions | select Username, State | Where-Object {$_.username -ne ""}
    $ActiveSessions = 0
    $ActiveUsers =""
    
    ForEach ($User_Session in $User_Sessions) {
    
        If ($User_Session.State -eq "Active") {
            $ActiveSessions++
            $ActiveUsers += $User_Session.Username + " "
            }
        }
    
    If (!$ActiveUsers) {
        "0 Current_Logins count=0 0 Logged in:"
        }
    Else {
        "1 Current_Logins count=$ActiveSessions Logged in: $ActiveUsers"
        }
