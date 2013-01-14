# Sublime Plugins

## Intellij Plugin

An attempt to mimic the keyboard shortcut behavoir of intellij (mainly on the mac)

## Elasticsearch Plugin

It's actually an enhanced bash plugin which assumes the you're executing curl commands to communicate with Elasticsearch.

Try this:
 * Open a new tab (Command+t)
 * Associate the new tab with the Elasticsearch build system (Command+e)
 * Write a curl command that communicates with an running instance of Elasticsearch (some pre-defined snippets are included, so you can use them... just type 'node-stats' and you'll see a suggestion for the snippets poping up)
 * Once you have your command ready, execute/build it (Command+b)
  - You should see that the window is split to two and a new tab on the right is opened with the json returned from Elasticsearch
 * It is also possible to select some of the text in the tab (on the right side of the split window) and when building it, only the selected text will be executed as a bash script

# Installation

## On the Mac

 * Navigate to the Packages directory of sublime (where it stores all its plugins)
  - `cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/`
 * Copy the Elastisearch and/or Intellij folders into it

