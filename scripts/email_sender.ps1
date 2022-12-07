$SmtpServer = 'smtp.mail.yahoo.com'
$SmtpUser = 
$SmtpPassword = 
$SmtpPort = 587
$MailTo = 
$MailFrom = 
$MailSubject = "Subject"
$MailBody = "Body text."
$AttachmentName = ".\file_name.txt"
$Credentials = New-Object System.Management.Automation.PSCredential -ArgumentList $SmtpUser, $($SmtpPassword | ConvertTo-SecureString -AsPlainText -Force) 
Send-MailMessage -To $MailTo -from $MailFrom -Subject $MailSubject -Body $MailBody -Attachments $AttachmentName -SmtpServer $SmtpServer -Credential $Credentials -UseSsl -Port $SmtpPort
