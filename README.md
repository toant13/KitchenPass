Kitchen Pass APP
=======
SUMMARY: Application that sends a notification from one significant other to another for permission to hangout with friends/co-workers/etc (canned questions that users of the app can add).  The spouse can then give or deny permission.  The asking spouse will get a notification and their calendar will be updated appropriately.  

Phone app with a Django Restful Framework Backend connected to Android client that gets push notification with Google Cloud Messaging Services (GCM).



++++++++TODO+++++
- Make device registration dynamic
- fix client code for registration handling
- Possibly use db rather than sharedpreferences to persist the reg_id
- Update model in web app so admin url can update/add reg id and device number
- Add device handling (ie request sends request to device 2, response go to device 1)

