# Setting up Mu Editor on Ubuntu 16.04

In our workshop, students will be using laptops loaded with Ubuntu 16.04.

Here is a procedure to add the Mu Editor to this environment:

    sudo apt install python3-pip3
    pip3 install mu-editor
    pip3 uninstall ipython
    pip3 install ipython==7.9.0

At this point, Mu Editor should be installed and working.

To test, run: mu-editor

Next, to add an icon to the launcher, do:

    cd ~/.local/share/applications
    wget https://raw.githubusercontent.com/mu-editor/mu/master/conf/mu.codewith.editor.desktop
    mkdir -p ../icons
    cd ../icons
    wget https://raw.githubusercontent.com/mu-editor/mu/master/conf/mu.codewith.editor.png

Select "Search your computer" in the launcher. (That's the top-most Ubuntu icon.)

Search for: mu

Launch it.

The application should launch and the "mu" icon should appear in the launcher.

Right-click the launcher and select "Lock to launcher."

