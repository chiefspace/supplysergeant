# < Supply Sergeant >

# Pre-work - *supply sergeant proof of concept*

**Supply Sergeant** is a computer inventory and user request tracker.

Submitted by: **Ben Altieri**

Time spent: **75** hours spent in total

## App Endpoints

* [x] GET /items &nbsp;&nbsp;&nbsp;&nbsp; Returns a list of all items in the database
* [x] GET /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Returns a specific item by name
* [x] POST /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Inserts an item into the database by item name with assignee and date assigned
* [x] PUT /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Updates an item by item name and new assignee name keeping previous assignee record
* [x] DEL /item/< name > &nbsp;&nbsp;&nbsp;&nbsp; Deletes an item by name
* [x] GET, POST /upload &nbsp;&nbsp;&nbsp;&nbsp; Upload a file
* [x] GET /uploads &nbsp;&nbsp;&nbsp;&nbsp; Get a list of uploaded files
* [x] GET /logins &nbsp;&nbsp;&nbsp;&nbsp; Loads the login page
* [x] GET, POST /logout &nbsp;&nbsp;&nbsp;&nbsp; Log the user out of the app


## User Stories

The following **required** functionality is yet to be completed:

* [x] Design / Define App resource methods



The following **additional** features are **to be** implemented:

* [ ] Purchase request approval workflow [ i.e someone requests a new computer, that will trigger an email to the CAPEX committee]

## Mockup on Balsamiq:

<img src='https://autodidactica.mybalsamiq.com/mockups/5883960.png?key=0944258a85141fb06484b669a7cf3b95451f585e' title='Supply Sergeant Mockup' width='' alt='Supply Sergeant Mockup' />

## Video Walkthrough 

Here's a walkthrough of implemented user stories:

<img src='https://www.google.com' title='Video Walkthrough' width='' alt='Video Walkthrough' />

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## Notes

Describe any challenges encountered while building the app.
* [1] Getting the original text to populate over to the edit Activity
* [2] Updating the item and positioning of the ArrayList when a particular item has been updated
* [3] Refactoring code and seeing what overlaps may be

## License

    Copyright [2017] [Ben Altieri]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
