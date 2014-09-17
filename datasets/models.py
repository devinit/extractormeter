from sqlalchemy import Column, Integer, String, Sequence

from database import Base

"""
Register application that wants to use API! Approve or rejection
will happen with the permission of admin on a platform such as OpenDev data's
(tokens being sent to email address)

** Application model
- User's email
- approved
- confirmation code (to be sent out by email)
- oauth_token

**
"""
