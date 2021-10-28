import os
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    else:
        repo = sys.argv[1]
        checkout_dir = sys.argv[2]
        # Make the git directory
        os.system('mkdir %s' % repo)
        os.chdir('%s' % repo)
        # Initialize a new bare repo
        os.system('git init --bare')
        txt = """#!/bin/sh
GIT_WORK_TREE=%s git checkout -f""" % checkout_dir
        # Write the post-receive hook
        hook = open('./hooks/post-receive', 'w')
        hook.write(txt)
        hook.close()
        # Make it executable
        os.system('chmod +x ./hooks/post-receive')
        # Print a command to run next.
        print ("\n\nNow run this command on your local repository\n\n")
        cmd = 'git remote add origin https://github.com/aashumallik/Git-Python.git' + repo
        print (cmd)

if __name__ == "__main__":
    main()