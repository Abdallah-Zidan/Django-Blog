from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import Profile
from django.contrib.auth.models import User
from users.logger import log
from users.util_funcs import *
import os

""" the following functions are to control users or admins 
    providing some functionality to be used in views
    @author AbdAllah Zidan """

def manager_show_normal_users(request):

    """ show all normal users [not admins nor super users]
    @params : request """

    current_user = request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            users = User.objects.filter(is_staff__exact= False)
            return render(request , "manager/users.html",{"users":users})
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")    

def manager_show_admins(request):
    
    """ show all admin users [admins or super users]
    @params : request """

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):  
            admins = User.objects.filter(is_staff__exact= True)
            context = {"admins":admins ,"superuser":current_user.is_superuser}
            return render(request , "manager/admins.html",context)    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")   
        
def manager_lock_user(request,id):

    """ lock a specific user not to be able to login again but his account is still alive
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            user = User.objects.get(pk=id)
            lock_user(user)
            log(current_user.username+" locked " +user.username+".")
            return HttpResponseRedirect("/manager/users")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def manager_delete_user(request , id ):

    """ delete a specific user not to be able to login and his account is deleted
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            user = User.objects.get(pk=id)
            if(user.profile.profile_pic !=None):
                 delete_profile_pic(user.profile.profile_pic)
            user.delete()
            log(current_user.username+" removed " +user.username+".")
            return HttpResponseRedirect("/manager/users")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def manager_show_user(request,id):

    """ show info of specific user all his profile with some additional info only revealed for admins
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            user = User.objects.get(pk=id)
            return render(request , "manager/show_user.html",{"user":user})    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def manager_unlock_user(request,id):

    """ unlock a specific user and becomes able to login again 
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            user = User.objects.get(pk=id)
            unlock_user(user)
            log(current_user.username+" unlocked " +user.username+".")
            return HttpResponseRedirect("/manager/users")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def manager_promote_user(request , id):

    """promote a specific user to become an admin with all determined permissions 
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            user = User.objects.get(pk=id)
            promote_to_staff(user)
            log(current_user.username+" promoted " +user.username+".") 
            return HttpResponseRedirect("/manager/users")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def super_demote_admin(request,id):

    """demote  a specific admin to become a normal user again  
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            if(current_user.is_superuser):
                user = User.objects.get(pk=id)
                demote_user(user)
                log(current_user.username+" demoted " +user.username+".") 
            return HttpResponseRedirect("/manager/admins")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def super_delete_admin(request,id):

    """ delete a specific admin not to be able to login and his account is deleted
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            if(current_user.is_superuser):
                user = User.objects.get(pk=id)
                if(user.profile.profile_pic !=None):
                    delete_profile_pic(user.profile.profile_pic)
                user.delete()
                log(current_user.username+" removed " +user.username+".") 
            return HttpResponseRedirect("/manager/admins")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def super_lock_admin(request,id):

    """lock a specific adminr not to be able to login again but keeping his account and permissions alive 
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            if(current_user.is_superuser):
                user = User.objects.get(pk=id)
                lock_user(user)
                log(current_user.username+" locked " +user.username+".") 
            return HttpResponseRedirect("/manager/admins")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 

def super_unlock_admin(request , id):

    """unlock a specific adminr  to be able to login again 
    @params : request  , id"""

    current_user =request.user
    if(current_user.is_authenticated):
        if(current_user.is_staff):
            if(current_user.is_superuser):
                user = User.objects.get(pk=id)
                unlock_user(user)
                log(current_user.username+" unlocked " +user.username+".") 
            return HttpResponseRedirect("/manager/admins")    
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/") 





