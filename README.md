We are cooked

commands to run to create a user that can interact with the database
``` sql
create user 'group_international'@localhost identified by 'EEKPAMSMAW';
grant create, select, insert, update on flight_game.* to group_international@localhost;
```

Trivia api for new and improved trivia game: https://opentdb.com/api_config.php

Api scripts complete: 
<br>small_task.py // contains pickpocketing and dumpster diving 
<br>random_events.py // should work
<br>


## What to check when testing
**if jsons dont want to work with javascript, you can wrap the dictionary in a list so it should work. most API returns should be in a result variable.(After some testing the way it is works but ill leave this here just in case) Example:**
``` python
result_json = [result]
return jsonify(result_json)
```
**Or use Response or another smarter way, im not smart enough**

**When game is done/ready for testing with class remove the comments marked with #!#, these implicate updates to the class witch doesnt work while testing since the player object is created at the beginning of the game**

**try to come up for a easy task for the medium airport since its feeling a bit lonely :(**

**current images are placeholders, might be used in end product but maybe we can generate new ones with AI**

**if using < br > tag in text doesnt work (likely not using innerHTML), try using \n or come up with a different way to break lines into smaller paragraphs**

## Ideas

- if we/i have time and allowed(would manly be javascript), try to add fishing minigame to medium airport.
- api for hangman: https://www.wordgamedb.com/endpoints 

