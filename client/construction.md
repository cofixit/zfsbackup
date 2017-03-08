# Structure of the Client application

### Notification object
- Manages any notifications displayed for the human
- Every notification has an ID
- Notifications are opened in threads, and have a callback function that is initiated later. 

### Request object
- The central object started by main
- Initiates Flask

### Validation object
- Takes care of "validating" servers, i.e. lets the user decide which server he wants to use. 
