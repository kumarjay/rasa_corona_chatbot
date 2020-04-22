## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - action_link
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## country path
* greet
- utter_greet
* name_entity
- action_form
- form{"name":"action_form"}
- form{"name":null}
- utter_show_name
  
* goodbye
- utter_goodbye

## state path
* district_info_entity
- action_state
- form{"name":"action_state"}
- form{"name":null}

* goodbye
- utter_goodbye


## picture data
- worldwide_corona_spread
- action_link
