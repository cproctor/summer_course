Reference
=========

I'll keep things here that you may need to refer to from time to time.


Using Git
---------

### Making Commits

Commits are a way of saving changes to your work. It's good to commit 
frequently. There are two main ways to use git: using the GitHub program,
or using git directly from Terminal.

From the GitHub program:

1. Work on your files using TextWrangler.
2. When you're ready to commit, open GitHub. It will detect the changes you've 
  made since the last commit. You can choose which to include in the commit. 
3. Add a commit message explaining the changes you made. 
4. Press "Commit"
5. Press the Sync button to upload your changes to GitHub. Now everyone can 
   see them. 

From Terminal:

1. `cd` into the directory holding your work.
2. type `git status` to see which files have been changed. 
3. (optional) type `git diff` to see all the changes that have been made to files.
4. type `git add ________` to add a file to the commit you're about to make. If you 
   type `git status` again, you'll see this file is now staged for the commit.
5. Once you're ready to commit, type `git commit -m "A message explaining what's new..."`
6. type `git push` to upload your changes to GitHub. Now everyone can see them.

### Updating your fork

The easiest way to update your fork with changes I made is to use the GitHub website, as 
described [here](http://www.hpique.com/2013/09/updating-a-fork-directly-from-github/).

If you want to use Terminal, there are two steps:

1. [Add an upstream remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/), pointing to 
   my original repository
2. [Sync your fork](https://help.github.com/articles/syncing-a-fork/) with the original repo.






