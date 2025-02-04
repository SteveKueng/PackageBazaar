# Install PackageBazaar on macOS (development environment):

## Prerequisites 

* Git
* Python
* munki repo
* munkitools

### Install python:
The easiest way is to install it via Homebrew. (follow this article to install Homebrew: https://docs.brew.sh/Homebrew-and-Python)

    brew install python



## Run PackageBazaar
### clone PackageBazaar

    cd ~
    git clone https://github.com/SteveKueng/PackageBazaar.git
    cd packagebazaar

### Create virtual env and activate it

    python -m venv ./venv
    source venv/bin/activate

### start dev server
check out ./startDevServer.sh and change any environment variable to your needs.
MUNKI_REPO_DIR
MAKECATALOGS_PATH
Do not change DEBUG to 0.

    ./devScripts/startDevServer.sh

### access munkiwebadmin
Check out http://localhost:8000
