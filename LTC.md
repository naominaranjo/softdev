# notes-and-code
Miscellany for SoftDev. Code snippets, starter kits, templates, etc -- as well as occasional miscellany -- will be posted to this repo.


# Last Class Today
Here shall be the official record of events transpiring in the 2021-2022 season of SoftDev. Each day, a new Devo will update this, in the appropriate period's folder, according to the template below.

## Wednesday 2020-10-06 :: STATIC WEBSITES W FLASK :: by Naomi Naranjo

**Interesting Tech News:** [Twitch confirms massive data breach.](https://www.bbc.com/news/technology-58817658)


### Static Files?
* static files don't change! 
* you can just use a static ```.html``` file, where the same page will be rendered everytime you refresh

### “This thing has no end on it”
* static/foo appe, that means it's just a plaintext file (which can still be read and edited)
* when you run http://localhost:5000/static/foo, without ".html" flask will propmt you to download foo since you are running the txt file and the html file
    - happens for most browsers, you should test your site on multiple to make sure
 
```bash
  $gedit filename # Opens filename in a regular text editor as a plain text file, doesnt render
  $cat foo   # Prints the contents of file to the terminal, shows up as just gibberish if not a plain text file
```


### Helpful
* [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

### Deliverables
In your heading, replace your name with your TNPG and roster.
Save to workshop under 11_flask-static. Structure:
```
path/to/myworkshop/11_flask-static$ tree
.
├── app.py
├── notes.txt
└── static
    ├── foo
    ├── foo.html
    └── fixie.html
```

#### Next LCT
* Roshani Shrestha (rshrestha20@stuy.edu)

#### Stuff
* Blah
* Blah
* Blah

#### Next LCT
* John von Neumann (jvn@stuy.edu)

Note the horizontal line below. Use it effectively.

---
