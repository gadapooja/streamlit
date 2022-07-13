try{
    Connect-ExchangeOnline
    $FFile = "C:\Users\pooja.gada\floatspec_code\streamlit\streamlit\all_employyes.csv"
    $userscsv1=import-csv -path $FFile
    $userscsv1|ForEach-Object -Begin $null -Process {Add-DistributionGroupMember -Identity $_.identity -Member $_.members},{"Successfully Added $_"} -End $null
}
catch{
    write-output "Ran into an error: $($PSItem.Exception.Message)"
}

Get-PSSession | Remove-PSSession