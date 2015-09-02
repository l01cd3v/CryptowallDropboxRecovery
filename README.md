CryptowallDropboxRecovery
=========================

## Installation and configuration

1. Clone this repository

    $ git clone git@github.com:l01cd3v/CryptowallDropboxRecovery.git

1. Install the Dropbox SDK

    $ pip install -r requirements.txt

1. Connect to your dropbox account
1. Create one -- or two -- new Dropbox Core application(s)
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

    $ python CryptowallRestore.py  

## Deletion of _.aaa_ files

    $ python CryptowallCleanup.py

## Author

l01cd3v

## License

GPLv2: See LICENSE.
