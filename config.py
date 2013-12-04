import random
import string

CSRF_ENABLED = True
SECRET_KEY=''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
REDIRECT_URI='http://amazing-tiger-394.appspot.com/oauth2callback'
#REDIRECT_URI='http://localhost:5000/oauth2callback'
SCOPE='https://www.googleapis.com/auth/analytics.readonly'
CLIENT_ID='475487142216-ldea6frnv53dv0dbaqfjjl5c22rqj0oq.apps.googleusercontent.com'
CLIENT_SECRET='DnsWXVRhYaVW_8RUIYTa2bjM'