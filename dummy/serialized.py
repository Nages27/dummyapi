from rest_framework import serializers
from dummy.models import User

class serializeduser(serializers.ModelSerializer):
 class Meta:
  model=User
  fields=["title","description","completed"]