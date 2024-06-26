# Wokelo

This project takes up a list of websites and outputs a screenshot of the websites removing any ads, cookies, popups, notifications on the website

## Code Overview

Click on the below image to go to youtube

[![Code Overview](https://img.youtube.com/vi/pWI-E21ceBM/0.jpg)](https://www.youtube.com/watch?v=pWI-E21ceBM&ab_channel=DivyanshJain)

## Setup

1. Setup python 3.12 
2. Create a new virtual environment
   
    ```
   # Create env
   python -m venv /path/to/new/virtual/environment
   
   # Activate env
   /path/to/new/virtual/environment activate
   ```

3. Install requirements 
    
    ```
   pip install -r requirements.txt
   ```
   
4. Check your Chrome version
   ![about_brave.png](readme_images/about_brave.png)
   ![brave_version.png](readme_images/brave_version.png)

5. Download ChromeDriver (as per your version)

    ```
   # For old versions
   https://chromedriver.chromium.org/downloads
   
   # For newer versions of Brave
   https://googlechromelabs.github.io/chrome-for-testing/
   ```
   
6. Setup your environment variables (See .env.example file)
   ```
   DRIVER_PATH="C:\Users\divya\PycharmProjects\wokelo\chromedriver.exe"
   BRAVE_PATH="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
   ```

7. Update profiles in profiles.json
   ```
   Syntax -> "Profile_name": "Directory"
   {
    "Default": "C:\\Users\\divya\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data",
    "Profile1": "C:\\Users\\divya\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data New"
   }
   ```

8. Update websites list in websites.json
   ```
   Syntax -> "Website url": "Screenshot file name"
   {
    "https://momi.baby/": "momibaby.png",
    "https://birdeye.com/": "birdeye.png"
   }
   ```

9. Run `main.py` file 

10. You can see the output images in `images` folder

11. Sample outputs (more sample outputs in the folder)
   ![birdeye.png](images/birdeye.png)
   ![alphasense.png](images/alphasense.png)
   ![momibaby.png](images/momibaby.png)


## How Brave does it?

Brave comes inbuilt with 2 main features

1. Filter Lists
   ![brave_filter_lists.png](readme_images/brave_filter_lists.png)
2. Shields
   ![brave_shields.png](readme_images/brave_shields.png)

## Scaling this solution - Multiple threads at a time

1. Use threads and multiple windows in selenium - Not possible
   1. Multiple selenium drivers with same profile - drivers cannot share the same profile, it gets locked
      ```
      Exception occurred for url https://www.alpha-sense.com/ : Message: unknown error: failed to write prefs file
      ```
   2. Multiple windows with same profile - The window needs to be in focus for which ss is being taken, therefore not possible
2. Use multiple drivers with different profiles and use an array of servers to scale - Possible
   1. No of profiles = No of cores on the machine
   2. The profile contains the filter lists configuration, copy and share it in the setup
      ![brave_multi_profiles.png](readme_images/brave_multi_profiles.png)
      The above screenshot shows two profiles running in parallel via selenium

## Future Work - How to further scale this?

1. Use Selenium Grid
   1. With selenium grid, it's easier to scale the number of instances of the browser
   2. Selenium grid only supports Edge, Chrome and Firefox out of the box
   3. Possible ways:
      1. Brave is also based on Chromium, so with some work it should be possible to use brave with Selenium Grid
      2. Use AdBlock Plus with Chrome, it has the features of using custom filter lists
         ![momibaby.png](readme_images/adblock_filter_lists.png)
      3. Community lists can be found at https://filterlists.com/
         ![img.png](readme_images/filterlist_website.png)
      4. Repos for all open source filter lists: https://github.com/collinbarrett/FilterLists/blob/main/services/Directory/data/FilterList.json
