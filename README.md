# petsciirender
A web-based PETSCII Art Renderer.

Features:
- Rendering in Standard (High-Res) Character Mode or Extended Background Color Mode.
- Select your choice of C64 character sets for rendering including support for custom character sets.
- Load/Save project file to preserve image rendering configuration.
- Save file formats that can be imported into external PETSCII editors.
- Adjust image contrast and image brightness for optimal image rendering.
- Substitute colors in save file output (to save time postprocessing in PETSCII editors).

Loading source images and character set images requires support for cross origin file loading. To do this:
- On Windows: Start Chrome from the command prompt using "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files file:///D:/petsciirender/petscii_converter.html
- On Mac OSX: Start Safari, in menu select Safari / Settings / Advanced and click to select 'Show features for web developers', then change to the Developers tab and click to select 'Security: Disable local file restrictions'.
- Any OS: Start Firefox, type about:config in the browsers address bar, then enter security.fileuri.strict_origin_policy as the Search preference name, finally toggle the setting to false.

The image does not need to be 320x200, it will be automatically scaled and resized to fit the 320x200 canvas. 

Save file formats are provided to support editing in C64 Studio and Marq's PETSCII editor. You can also save the file if you want to load it up on a real C64, or in an emulator. The .D64 file contains several prerendered and saved files. It also contains the BASIC program I wrote to render the .pet files to the C64's screen.

Enjoy.
