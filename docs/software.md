---
title: Software
#subtitle: 
#description: 
#icon: 
#status:
#template: 
---

# Software


!!! tip
    CLI (command line interface) software is most easily installed using your [package manager](#system). 
    _Homebrew_ can even install most GUI software for your macOS.

    === "macOS"

        Using Terminal:

        ``` bash
        $ brew search <name>       # look for software 
        $ brew install <name>      # install software 
        $ brew cask install <name> # install GUI software 
        ```
        
        See [`tldr brew`](https://tldr.inbrowser.app/pages/common/brew) for more information.

    === "Windows"

        Using WSL (Ubuntu):

        ``` bash
        $ apt search <name>         # look for software
        $ sudo apt install <name>   # install software
        ```

        See [`tldr apt`](https://tldr.inbrowser.app/pages/linux/apt) for more information.

    === "Linux"

        [pacman/Rosetta](https://wiki.archlinux.org/title/Pacman/Rosetta)

    -----

## System

#### [Homebrew](https://brew.sh/)
The missing package manager for macOS.

#### [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)
Use Linux inside Windows. Works as a package manager for CLI software on Windows. ([MSYS2](https://www.msys2.org/) can also be considered, as an alternative to WSL)

#### [Linux](https://distrochooser.de/)
Linux :simple-linux:


## CAD

#### [FreeCAD](https://www.freecad.org/)
Parametric 3D modeller software. The functionality is expected to increase significantly in the coming years.
{{ resource( "freecad" ) }}

#### [FreeCAD BIM](https://www.freecad.org/)
FreeCAD workbench for digital architecture modelling. 
{{ resource( "freecad_bim" ) }}

#### [Blender](https://www.blender.org/)
Meshing and sculpting 3D-modeller software. 
{{ resource( "blender" ) }}

#### [LibreCAD](https://librecad.org/)
2D design software with DXF support.


## Graphic

#### [Inkscape](https://inkscape.org/)
Vector graphics editor with bitmap tracing, path effects, filters and generator extensions (QR codes, charts, plots, calendars, etc.). 
{{ resource( "inkscape" ) }}

#### [Graphite](https://graphite.rs/)
2D vector & raster editor that melds traditional layers & tools with a modern node-based, non-destructive, procedural workflow. 

#### [Krita](https://krita.org/)
Raster graphics drawing editor with good graphics table support and G'MIC filters.

#### [GIMP](https://www.gimp.org/)
Raster graphics editor for image manipulation and editing, typically photos.

#### [FontForge](https://fontforge.org/)
Font editor software. Can also extract and export fonts from PDF files.

#### [Blender](https://www.blender.org/)
3D scene renderer (photorealism, cartooning, etc.). 
{{ resource( "blender" ) }}

#### [Sozi](https://sozi.baierouge.fr/)
Zooming presentation editor.

#### [Pixelorama](https://orama-interactive.itch.io/pixelorama)
Pixel art multitool.

#### [Scribus](https://www.scribus.net/)
Desktop Publishing software (DTP)

#### [darktable](https://www.darktable.org/)
Photography workflow application and RAW developer.

#### [ImageMagick](https://imagemagick.org/)
CLI image format converter and editor.


## Video

#### [VLC Media Player](https://www.videolan.org/vlc/)
Media player that supports most video and audio formats.

#### [Kdenlive](https://kdenlive.org/)
Video editor software.

#### [Natron](https://natrongithub.github.io/)
Composing software for VFX and motion graphics.

#### [EagleAnimation](https://brickfilms.com/eagle-animation)
Stop motion animation software with several features, using
a wired USB-webcam (or a DSLR camera), typically.

#### [Synfig Studio](https://www.synfig.org/)
Vector based 2D animation software.

#### [Pencil2D](https://www.pencil2d.org/)
2D hand-drawn animation software.

#### [FFmpeg](https://tldr.inbrowser.app/pages/common/ffmpeg)
CLI to convert video and sound formats.

#### [yt-dlp](https://tldr.inbrowser.app/pages/common/yt-dlp)
CLI to download video and audio from internet (YouTube, Vimeo, SoundCloud and _many_ other sites).

#### [vcsi](https://github.com/amietn/vcsi)
CLI with several options to create a grid of thumbnails from video.


## Audio

#### [Audacity](https://www.audacityteam.org/)
Digital audio editor and recorder.

#### [LMMS](https://lmms.io/)
Digital audio workstation.

#### [Mixxx](https://mixxx.org/)
DJ software.


## Web

#### [GitHub Pages](https://pages.github.com/)
A free and easy way to create a homepage using your GitHub account.

#### [Jekyll](https://jekyllrb.com/)
An easy way to create your own website. Works well with GitHub pages.

#### [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
A popular theme with several features for MkDocs. Works well with GitHub pages. 
This site is made using MkDocs and Material.

#### [awesome-selfhosted](https://awesome-selfhosted.net/)
List of self hosting alternatives for web services.


## Office

#### [Pandoc](https://pandoc.org/)
CLI for converting between text document formats. Makes it easy to create PDF files from Markdown with images, reference system, etc. Templates let you define custom visual styles.

#### [LibreOffice](https://www.libreoffice.org/)
Traditional office suite (word processor, spreadsheet, presentation program, database).


## UI

#### [Penpot](https://penpot.app/)
GUI design 


## Data

#### [SankeyMATIC](https://sankeymatic.com/)
Compare amounts through different stages.

#### [Orange](https://orangedatamining.com/)
Interactive, visual data analysis.

#### [sampler](https://sampler.dev/)
CLI configurable data sampler and visualizer.


## Tools

#### [Git](https://git-scm.com/book/)
The de facto version control system. 

#### [GitHub Desktop](https://github.com/apps/desktop)
GUI to simplify Git workflows on GitHub.

## Productivity

#### [uBlock Origin](https://ublockorigin.com/)
Enjoy the internet without ads.

#### [SponsorBlock](https://sponsor.ajay.app/)
Automatically skip the sections with sponsored content in YouTube videos.


*[CLI]: Install using your package manager (typically)
