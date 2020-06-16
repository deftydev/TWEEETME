import random
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.utils.http import is_safe_url


ALLOWED_HOSTS=settings.ALLOWED_HOSTS


def home_view(request, *args , **kwargs):
    return render(request, "pages/feed.html")

def tweets_list_view(request, *args , **kwargs):
    return render(request, "tweets/list.html")

def tweets_detail_view(request,id, *args , **kwargs):
    return render(request, "tweets/detail.html", context={"id":id})

# def tweets_profile_view(request,username,*args , **kwargs):
#     return render(request, "tweets/profile.html", context={"profile_username":username})

#@authentication_classes([SessionAuthentication, MyCustomAuth])
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def tweet_create_view(request, *args, **kwargs):
#     serializer= TweetCreateSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         obj=serializer.save(user=request.user)
#         return Response(serializer.data, status=201)
#     return Response({}, status=400)
#
# @api_view(['GET'])
# def tweet_list_view(request, *args, **kwargs):
#     qs=Tweet.objects.all()
#     username= request.GET.get('username')
#     if username != None:
#         qs=qs.filter(user__username__iexact=username)
#     serializer=TweetSerializer(qs, many=True)
#
#     return Response(serializer.data, status=200)
#
# @api_view(['GET'])
# def tweet_detail_view(request,id, *args, **kwargs):
#     qs=Tweet.objects.filter(id=id)
#     if not qs.exists():
#         return Response({}, status=404)
#     obj=qs.first()
#     serializer=TweetSerializer(obj)
#
#     return Response(serializer.data, status=200)
#
#
# @api_view(['GET','DELETE'])
# @permission_classes([IsAuthenticated])
# def tweet_delete_view(request,id, *args, **kwargs):
#     qs=Tweet.objects.filter(id=id)
#     if not qs.exists():
#         return Response({}, status=404)
#         qs=qs.filter(user=request.user)
#     if not qs.exists():
#         return Response({"message":"you cannot delete this tweet"}, status=401)
#     obj=qs.first()
#     obj.delete()
#     return Response({"message":"tweet deleted"}, status=200)
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def tweet_action_view(request, *args, **kwargs):
#     serializer=TweetActionSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         data=serializer.validated_data
#         id=data.get("id")
#         action=data.get("action")
#         content=data.get("content")
#         qs=Tweet.objects.filter(id=id)
#         if not qs.exists():
#             return Response({}, status=404)
#         obj=qs.first()
#
#         if action=="like":
#             obj.likes.add(request.user)
#             serializer=TweetSerializer(obj)
#             return Response(serializer.data, status=200)
#         elif action=="unlike":
#             obj.likes.remove(request.user)
#             serializer=TweetSerializer(obj)
#             return Response(serializer.data, status=200)
#         elif action=="retweet":
#
#             new_tweet=Tweet.objects.create(user=request.user, parent=obj,content=content,)
#             serializer=TweetSerializer(new_tweet)
#             return Response(serializer.data, status=200)
#
#     return Response({}, status=200)
#
#
# def tweet_create_view_pure_django(request, *args, **kwargs):
#     user=request.user
#     if not request.user.is_authenticated:
#         user=None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#     print("ajax", request.is_ajax())
#     form=TweetForm(request.POST or None)
#     next_url=request.POST.get("next") or None
#     if form.is_valid():
#         obj=form.save(commit=False)
#         obj.user=request.user or None
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)
#
#         if next_url!=None and is_safe_url(next_url,ALLOWED_HOSTS):
#             return redirect(next_url)
#         form=TweetForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#     return render(request, "components/form.html",context={"form":form})
#
# def tweet_list_view_pure_django(request, *args, **kwargs):
#     qs=Tweet.objects.all()
#     tweet_list=[x.serialize() for x in qs]
#     data={
#        "isUser": False,
#        "response":tweet_list
#     }
#     return JsonResponse(data)
#
# def tweet_detail_view_pure_django(request,id, *args, **kwargs):
#     data={
#       "id": id,
#     }
#     status=200
#     try:
#         obj=Tweet.objects.get(id=id)
#         data['content']= obj.content
#     except:
#         data['message']="NOT Found"
#         status=404
#     return JsonResponse(data, status=status)
