# petsciirender
A web-based PETSCII Art Renderer

Loading source images and character set images requires support for cross origin file loading. To do this start chrome on the command line with the --allow-file-access-from-files option. e.g. "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files file:///D:/petsciirender/petscii_converter.html

The image does not need to be 320x200, it will be automatically scaled and resized to fit the 320x200 canvas. 

Safari 10 does not seem to want to save the file. However, the Safari Technology Preview does. You only need to save the file if you want to load it up on a real C64, or in an emulator. The .D64 file contains several prerendered and saved files. It also contains the BASIC program I wrote to render the .pet files to the C64's screen.

Enjoy.
