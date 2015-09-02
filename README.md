CryptowallDropboxRecovery
=========================

This repository contains the python code I created and used to recover a friend's file after they were victim of Cryptowall. It addresses a particular case where all of my friend's files were stored in Dropbox. Because Dropbox offers free versioning to all users for a 30-day period and because my friend contacted me within a day of the compromise, I was able to restore all of her files. Note that **I do not recommend the use of Dropbox as a primary backup system or protection against any cryptolocker malware**. Much consideration should be taken when creating one's backup process, which is out of the scope of this project.

## Installation and configuration

1. Clone this repository
<pre>$ git clone git@github.com:l01cd3v/CryptowallDropboxRecovery.git</pre>
1. Install the Dropbox SDK
<pre>$ pip install -r requirements.txt</pre>
1. In your browser, connect to your dropbox account
1. Create a new Dropbox Core application(s)
  1. Browse to the console API at https://www.dropbox.com/developers/apps
  1. Create a new application with the following settings
    * Type of application: "Dropbox Core API"
    * Limited folder: "No My app needs access to files already on Dropbox."
    * Access: "All file types My app needs access to a user's full Dropbox."
    * Name: your application name, _e.g._ CryptowallDropboxRecoveryFor_YourNameHere_
1. Edit the _CryptowallDropboxRecovery/utils.py_ file and replace the following:
  1. _YOUR\_APP\_KEY\_HERE_ with the "App key" copied from the application page
  1. _YOUR\_APP\_SECRET\_HERE_ with the "App secret" copied from the application page

## Recovery of deleted files

In order to restore your deleted files, run the _CryptowallRestore.py_ tool. This tool iterates through all your files and folders and restores the latest, non-deleted version of your files if a corresponding "_.aaa_" file is found. You will be prompted to browse to the application authorization page and copy-paste the authorization code.

    $ python CryptowallRestore.py

## Deletion of _.aaa_ files

After confirming that the restoration of your files was successful, run the _CryptowallCleanup.py_ tool. This tool iterates through all your files and folders and deletes all "_.aaa_" files if a corresponding file exists. You will be prompted to browse to the application authorization page and copy-paste the authorization code.

    $ python CryptowallCleanup.py

## Author

l01cd3v

## License

GPLv2: See LICENSE.
