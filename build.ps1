# Define the source folders
$sourceFolders = @("src", "package")

# Define the destination archive file name
$destinationArchive = "deploy.zip"

# Check if the archive already exists
if (Test-Path $destinationArchive) {
    # Update the existing archive
    Compress-Archive -Path $sourceFolders -DestinationPath $destinationArchive -Force
} else {
    # Create a new archive
    Compress-Archive -Path $sourceFolders -DestinationPath $destinationArchive
}

# Check if an empty "Lab2" folder was created and remove if so
if (Test-Path "codelabs-emailer" -PathType Container) {
    $isEmpty = !(Get-ChildItem "codelabs-emailer")
    if ($isEmpty) {
        Remove-Item "codelabs-emailer" -Recurse -Force # Remove the empty folder
    }
}
