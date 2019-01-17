# search_pwned_passwords_offline
This Jupyter notebook looks up all your passwords from a LastPass export in the offline database of [Pwned Passwords][1]. and reports any breached passwords.

## Usage
1. Install Python3 and the package 'pandas' using [PiP][2] or [Conda][3].
1. Download the 'Pwned Passwords' database [here][1].
   Note that the 7-Zip packed download is ~10GB, unpacked ~23GB.
1. Get an export of your LastPass passwords.
   1. Go to your Password Vault and in the lower left corner hit 'More Options \ Advanced \ Export'.
   1. Copy the whole text, paste it into a text editor, save the file as **UTF-8** to the same location as where you stored the python script, using the file name `my_password_list.txt`.
1. Make sure that the python script, the unpacked 'Pwned Passwords' file and your LastPass file are in the same location.
1. In a command line window `cd` to the folder containing your files.
1. Execute `python check_pwned_passwords_from_lastpass_export.txt`.
   1. Get ready to change some passwords.
1. **Don't forget to [securely remove][4] the file containing the plain text passwords afterwards!**

[1]: https://haveibeenpwned.com/Passwords
[2]: https://packaging.python.org/tutorials/installing-packages/
[3]: https://conda.io/docs/user-guide/tasks/manage-pkgs.html
[4]: https://www.groovypost.com/howto/7-free-ways-securely-delete-files-windows/
