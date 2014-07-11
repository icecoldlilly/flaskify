from marshmallow import Serializer, fields
#This works with together with Marshmallow, define you serializers here following the Marshmallow API
class UserSerializer(Serializer):
    #You could define a field using a function. The local function could call a global function from another class
    example=fields.Method("thisExample")
    class Meta:
        fields = ('uid', 'username', 'email','followers' ,'points')
    #This is the local example function being called
    def thisExample(self,obj):
        data="Example"
        return data
#Change or delete the Item serializer to fit your needs
class ItemSerializer(Serializer):
    class Meta:
        fields = ('item_id','user_id','description', 'date')
