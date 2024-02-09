### **Activate the Virtual Environment**

Before installing dependencies and running the project, you need to activate the virtual environment.
```
source bin/activate
```
You should now see the name of the virtual environment in parentheses before your terminal prompt, indicating the virtual environment is active.


### **Install Dependencies**

With the virtual environment activated, install the project dependencies.

```
pip install -r requirements.txt
```


### **ffmpeg and ffprobe**
The pydub library uses ffmpeg or ffprobe behind the scenes to handle audio file operations. These tools need to be installed separately from the Python environment because they are not Python packages but standalone applications. Making them available in your system's PATH allows Python libraries like pydub to call them as need


WUsing Homebrew
If you don't already have Homebrew installed on your macOS, you can install it by pasting the following command in a macOS Terminal prompt:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

Then, you can install ffmpeg (which includes ffprobe) using Homebrew by running:

```
brew install ffmpeg
```

Verifying the Installation
After installation, you can verify that ffmpeg and ffprobe are correctly installed and accessible in your PATH by running:

```
ffmpeg -version
ffprobe -version
```

These commands should display the version information for ffmpeg and ffprobe, indicating that they are correctly installed.

Making ffmpeg and ffprobe Available to Your Script
Once ffmpeg and ffprobe are installed, your pydub script should be able to locate and use them without the FileNotFoundError. If you're still encountering issues, ensure that the Terminal session where you run your script is restarted or that you've opened a new Terminal window after installing ffmpeg to refresh the PATH.