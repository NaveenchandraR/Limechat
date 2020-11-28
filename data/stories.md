<!-- Booking -->
## Story path 1
*greet
    - utter_greet
*booking
    - utter_enquiry_room_no
*room_no
    - utter_enquiry_room_type
*simple
    - utter_confirmation_simple
*goodbye
    - utter_goodbye

## Story path 2
*greet
    - utter_greet
*booking
    - utter_enquiry_room_no
*room_no
    - utter_enquiry_room_type
*deluxe
    - utter_confirmation_deluxe
*goodbye
    - utter_goodbye

## Story path 3
*greet
    - utter_greet
*book+room_no
    - utter_enquiry_room_type
*simple
    - utter_confirmation_simple
*goodbye
    - utter_goodbye

## Story path 4
*greet
    - utter_greet
*book+room_no
    - utter_enquiry_room_type
*deluxe
    - utter_confirmation_deluxe
*goodbye
    - utter_goodbye

<!-- Cleaning -->
## Story path 5
*greet
    - utter_greet
*cleaning
    - utter_ask_time
*clean+time
    - action_relative

## Story path 6
*greet
    - utter_greet
*cleaning
    - utter_ask_time
*immediate
    - utter_cleaning_confirm

<!-- FAQ -->
## Story path 7
*checkin
    - utter_checkin

## Story path 8
*checkout
    - utter_checkout

## Story path 9
*cancel_reservation
    - utter_cancel_reservation

## Story path 10
*cancellation_policy
    - utter_cancellation_policy

## Story path 11
*restaurant
    - utter_restaurant

## Story path 12
*breakfast
    - utter_breakfast

## Story path 13
*breakfast_timings
    - utter_breakfast_timings

## Story path 14
*restaurant_timings
    - utter_restaurant_timings

## Story path 15
*goodbye
    - utter_goodbye

## Story path 16
*greet
    - utter_greet
*cleaning
    - utter_ask_time
*timing
    - action_relative