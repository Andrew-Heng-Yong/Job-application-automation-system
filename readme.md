# Job application automation system

## Overview
This project automates majority parts of WaterlooWork job application process. It is designed to help with repetitive application steps and reduce manual clicking. The system also supports cover letter generation and resume selection as part of the workflow

## Setup

 1. Set execution policy if needed:
 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
    
 2. Activate the virtual environment:
 `venv\Scripts\activate`
 
 3. Install required packages:
 `pip  install  -r  requirements.txt`
 
 ## Requirements

This project currently works best on a Windows device with the same general setup used during development.

Requirements:

-   Windows environment
    
-   Python virtual environment
    
-   Required Python packages installed
    
-   Matching reference screenshots for the current device

-   Recommands: display scaling set to 125% or 150%
    

## Important Device-Specific Notes

### Display scaling

On the current device, the automation is expected to run with Windows display scaling set to 125 percent. This helps the program to distinguish symbols easier.

### Reference images

This project depends on screenshot-based image matching for most UI interactions. Because of differences in display scaling, resolution, browser layout, font rendering, and device-specific appearance, capturing new reference images is needed for each new device.

In future developments, we plan to automate the reference images capturing process.

## First-Time Setup on a New Device

1.  Set Windows display scaling to 125 percent.
    
2.  Activate the virtual environment.
    
3.  Install the required packages.
    
4.  Re-capture the reference screenshots needed by the bot.
    
5.  If unsure the computed diffrence between two images, use `conftest.py` to check

6.  Upload Gemini API key by running `$env:GEMINI_API_KEY="your_api_key_here"` in the terminal of your IDE

7.  select model in `gemini_cover_letter.py`.

8. Need to rearrange WaterlooWork such that its Level column is fully shown.

10. When uploading cover letter, make sure the folder `generated_cover_letters/` is open by default.

## Adding new resume:

 - Add new resume to `resume/` folder
 - Upload resume catalogue in `generate_cover_letter.py`
 - Add resume to WaterlooWork and take refrence image

## Project Structure

-   `main.py` contains the main automation flow.
    
-   `gemini_cover_letter.py` contains cover letter generation logic.
    
-   `imgs/` stores reference screenshots used for image matching.
    
-   `resume/` stores resume files used by the application system.

-  `generated_cover_letters/` contains generated cover letters

-  `image_relation_tester/` contains the image relation tester
    

## Known Limitations

-   The automation may break if the website layout changes.
    
-   The automation is sensitive to display scaling, browser layout, and screenshot differences, do not change scaling after refrence images has been taken.
    
-   New devices require retaking reference images.
   