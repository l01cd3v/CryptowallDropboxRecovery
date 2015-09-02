#!/usr/bin/env python

from CryptowallDropboxRestoreLib.utils import *
import sys

#
# Restore previous version of deleted files whose name match a .aaa file
#
def restore_folder(api_client, path):
    sys.stdout.write('Listing files in %s\n' % path)
    try:
        resp = api_client.metadata(path = path, include_deleted = True)
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
                        file_revisions = api_client.revisions(original_file)
                        version_number = 0
                        revision = None
                        for r in file_revisions:
                            if not 'is_deleted' in r or r['is_deleted'] != True:
                                if version_number < r['revision']:
                                    version_number = r['revision']
                                    revision = r['rev']
                        if revision:
                            api_client.restore(original_file, revision)
                            sys.stdout.write('Restored revions %s of %s\n' % (revision, original_file))
                    except Exception, e:
                        sys.stdout.write('Error occured when trying to restore file matching %s (%s)\n' % (filename, e))
            else:
                restore_folder(api_client, fileinfo['path'])
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
##### Restore original files
################################################################################
restore_folder(api_client, '/')

