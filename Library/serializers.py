from rest_framework import serializers
from .models import Books,User,BookIssue

class BooksSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    category = serializers.CharField()
    author = serializers.CharField()
    available_copies = serializers.IntegerField()

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = [
            'email'
            'username',
            'password']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '_all_'
        read_only_fields = ('created_at',)