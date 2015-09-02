#!/usr/bin/env python

from CryptowallDropboxRestoreLib.utils import *
import sys

#
# Remove .aaa files whose name matches a restored file
#
def cleanup_folder(api_client, path):
    sys.stdout.write('Listing files in %s\n' % path)
    try:
        resp = api_client.metadata(path = path)
        contents = resp['contents']
        for fileinfo in contents:
            if not fileinfo['is_dir']:
                filename = fileinfo['path']
                if filename.endswith('.aaa'):
                    original_file = filename.replace('.aaa', '')
                    if not has_original_file(contents, original_file):
                        sys.stdout.write('Error: did not find an original file matching %s\n' % filename)
                        continue
                    try:
                        api_client.file_delete(filename)
                        sys.stdout.write('Deleted file %s\n' % filename)
                    except Exception, e:
                        sys.stdout.write('Error: failed to delete file %s\n' % filename)
            else:
                cleanup_folder(api_client, fileinfo['path'])
    except Exception as e:
        sys.stdout.write('Error listing files in folder %s (%s)\n' % (path, e))


################################################################################
##### Initialize the Dropbox client
################################################################################
api_client = initialize_dropbox_client()
if not api_client:
    sys.stdout.write('Error: failed to initialize Dropbox client.\n')
    sys.exit(1)

################################################################################
##### Delete .aaa files
################################################################################
cleanup_folder(api_client, '/')

