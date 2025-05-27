from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Follow, Group, User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "posts")
        ref_name = "ReadOnlyUsers"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)

    def validate(self, data):
        current_user = self.context['request'].user
        target_user = data.get('following')

        if current_user == target_user:
            raise serializers.ValidationError(
                "Вы не можете подписаться на самого себя!")

        subscription_exists = Follow.objects.filter(
            user=current_user,
            following=target_user
        ).exists()

        if subscription_exists:
            raise serializers.ValidationError(
                "Подписка на этого пользователя уже существует")

        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, required=False)
    post = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    created = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post', 'created')
        model = Comment
