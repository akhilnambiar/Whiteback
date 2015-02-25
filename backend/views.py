from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from ast import literal_eval
from backend.models import UsersModel, HandoutModel, InvitesModel
import json
import logging
import urllib2
import simplejson


# NOTE: For the BETA, people will only be adding accounts
# NOTE: After the BETA, we will need to account for school as well
# NOTE: Assumption, that we are only supporting one school right now
# NOTE: We will need to think about data purging (when do we remove
# handouts and invites etc)


def index(request):
    return render(request, 'index.html')


def add(request):
    """
    Logic: What do we need for login?
    We don't want to have the hassel of their passwords
    """
    response = {'errCode': 40}
    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
def login(request):
    """
    Request JSON:
    @user_id: The individuals ID given by the permission ID in google drive

    Logic:
    1) Check to see if they are in db
    2) If not, have them create a profile
    3) Once they create a profile, we will respond with the invite count

    Response JSON:
    @errcode: Boolean for if they are valid or not (0 is false, 1 is true)
    @user_id: Their user_id so they can populate invites
    @invites: A count for the invites so we know how many they have (None, if they have not been authenticated)
    NOTE: The next two will be made obsolete as we iterate onwards (We will use the time to determine the teacher and period, so we will make a seperate method later to avoid db queries)
    @teacher:
    @period:
    """
    try:
        correct_data = get_request_data(request)
        req = correct_data[0]
        inList = correct_data[1]
        if inList:
            username = req['username'][0]
        else:
            username = req.get('username', None)
        username = username
        db_model = UsersModel()
        errcode = db_model.login(username)
        if errcode[1] == 1:
            valid = 1
        else:
            valid = -1
        # for now we will return the userID, later we need to modify and create another query for this
        # we will use the returned userid to query for the invites associated
        # EXPAND HERE
        res = {'errcode': valid, 'user_id': errcode[
            0], 'invites': 0, 'teacher': errcode[2], 'period': errcode[3]}
        return HttpResponse(json.dumps(res), content_type='application/json')
    except Exception, ex:
        logging.exception("Something awful happened!")


@csrf_exempt
def add_user(request):
    """
    Request JSON:
    @username: The individual's username
    @school: The school the individual attends
    @first_name: The first name of the user
    @last_name: The last name of the user
    @teacher: The teacher of the primary user
    @period: The period that the student is attending that class (if applicable)
    @email: The email address


    Logic:
    1) We just need to store this information in the database
    2) Return an error code if these things failed

    NOTE: We will eventually phase out what period you have to enter,we will shift to codes to accept

    Response JSON:
    @errorCode: 1 if success, else -1
    @invites: The number of invites the individual has

    ASSUMPTION: Currently we are assuming that we can't add people that aren't in the system
    """
    correct_data = get_request_data(request)
    req = correct_data[0]
    inList = correct_data[1]
    if inList:        
        username = req['username'][0]
        school = req['school'][0]
        first_name = req['first_name'][0]
        last_name = req['last_name'][0]
        teacher = req['teacher'][0]
        period = req['period'][0]
        email = req['email'][0]
    else:
        username = req.get('username', None)
        school = req.get('school', None)
        first_name = req.get('first_name', None)
        last_name = req.get('last_name', None)
        teacher = req.get('teacher', None)
        period = req.get('period', None)
        email = req.get('email', None)
    db_model = UsersModel()
    # add_user will return a list of two items
    errcode = db_model.add_user(
        username, school, teacher, period, first_name, last_name, email)
    res = {'errcode': errcode[0], 'count': errcode[1]}
    return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
def put_handout(request):
    """
    Request JSON:
    @file_name: The name of the file on google drive that's being added
    ***WARNING: This should eventually be changed to the file ID***
    @teacher: The teacher of the primary user
    @period: The period that the student is attending that class (if applicable)

    Return JSON
    @errcode: 1 if success -1 if failed
    """
    req = dict(request.POST.iterlists())
    file_name = req['file_name'][0]
    teacher = req['teacher'][0]
    period = req['period'][0]
    db_model = HandoutModel()
    # add_user will return a list of two items
    errcode = db_model.put_handout(teacher, period, file_name)
    res = {'errcode': errcode}
    return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
def get_handouts(request):
    """
    Request JSON:
    @username: The individual's username
    @teacher: The teacher of the primary user
    @period: The period that the student is attending that class (if applicable)


    IDEAL SCENARIO: We will have the teacher "push" files to all of the students in their class
    In order to simulate this, the teacher will share the file to all of her students. We will then look at
    the recent handouts based on when the items were shared and then we can pull them one by one
    from the students. That way, they will have the file as well.

    Logic:
    1) We will look at the parameters and see what were the recent handouts
    2) We will then serve up a thumbnail of the response by sending a thumbnail_url (Not necessary for MVP)

    Comments:
    We will not be storing files within Django for now, we will assume the sample user account can have
    We can have default image URLs (they can be stored locally)

    JSON Response:
    @Errorcode: 1 if the operation succeeded, or -1 if it failed. -2 Means that an exception was thrown
    @file_name: A list of up to three titles of handouts
    Note: We won't provide them with URLs, but if the account is a test account, we need to make a call to find handouts
    """
    try:
        correct_data = get_request_data(request)
        req = correct_data[0]
        inList = correct_data[1]
        if inList:
            teacher = req['teacher'][0]
            period = req['period'][0]
        else:
            teacher = req.get('teacher', None)
            period = req.get('period', None)
        res = {'errcode': -2, 'file_name': None}
        req = dict(request.GET.iterlists())
        print(request)
        print(req)
        # add_user will return a list of two items
        db_model = HandoutModel()
        handout = db_model.get_handouts(teacher, period)
        # the first item shouldn't be None, if it is, there is an error
        if handout[0] == None:
            res = {'errcode': -1, 'file_name': None}
        else:
            res = {'errcode': 1, 'file_name': handout}
        return HttpResponse(json.dumps(res), content_type='application/json')
    except Exception, ex:
        logging.exception("Something awful happened!")
        return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
def get_classmates(request):
    """
    Request JSON:
    @username: The individual's username
    @teacher: The teacher of the primary user
    @period: The period that the student is attending that class (if applicable)

    Logic:
    We will just look up the teacher and period and return a list of the classmates

    Return JSON:
    @errcode: 1 if success, -1 if it failed
    @first_name: A list of all of the available classmate's first names,  None, if there are none
    @last_name: A list of all of the available classmate's last names,  None, if there are none
    @user_id: A list of the corresponding user_ids (used to send invites later)
    """
    try:
        correct_data = get_request_data(request)
        req = correct_data[0]
        inList = correct_data[1]
        if inList:
            teacher = req['teacher'][0]
            period = req['period'][0]
        else:
            teacher = req.get('teacher', None)
            period = req.get('period', None)
        db_model = UsersModel()
        # add_user will return a list of three items
        result = db_model.get_classmates(teacher, period)
        if result[2] == -1:
            res = {'errcode': 1, 'first_name': None,
                   'last_name': None, 'user_id': None}
        else:
            res = {'errcode': 1, 'first_name': result[
                0], 'last_name': result[1], 'user_id': result[2]}
        return HttpResponse(json.dumps(res), content_type='application/json')
    except Exception, ex:
        render(logging.exception("Something awful happened!"))


@csrf_exempt
def send_invites(request):
    """
    Request JSON:
    @username: A list of user_id's
    @file_name: The file name of an associated handout if it exists, else the handout will be None

    Logic: go through and for each user_id on the list, add a new invite object

    Response JSON:
    @errcode: 1 if it succeeded, -1 if there was at least one failure, -2 if the handout could not be found

    Comments: For now, we will not add an invite for an existing username
    -In view docs, we should be able to see the recent files we have manipulated so we can access them
    -In the long run, we should promote ACID transactions (either all actions persist or none)

    TODO: Add the invites userflow
    TODO: Add the correct error handling in case query fails
    TODO: We need to make sure for a given handout, the student and the period and stuff line up. It will work for now but we will need to fix it
    """
    try:
        correct_data = get_request_data(request)
        req = correct_data[0]
        inList = correct_data[1]
        if inList:
            u = req['user_id'][0]
            inviter = req['inviter'][0]
            invitee = req['invitee'][0]
            f = req['file_name'][0]
        else:
            u = req.get('user_id', None)
            inviter = req.get('inviter', None)
            invitee = req.get('invitee', None)
            f = req.get('file_name', None) 
        db_model1 = HandoutModel()
        if f != "None":
            h = db_model1.get_handout_from_file_name(f)
            if h == None:
                res = {'errcode': -2}
                return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            h = None
        db_model2 = InvitesModel()
        errorcode = 1
        for x in u:
            error = db_model2.put_invite(x, h, inviter, invitee)
            if error == -1 and errorcode == 1:
                errorcode = - 1
            res = {'errcode': errorcode}
        return HttpResponse(json.dumps(res), content_type='application/json')
    except Exception, ex:
        render(logging.exception("Something awful happened!"))


@csrf_exempt
def get_invites(request):
    """
    Request JSON:
    @username: The individual's username
    @teacher: The teacher of the primary user
    @period: The period that the student is attending that class (if applicable)

    Logic: Just create a model method to go ahead and grab the invites associated to a corresponding person

    Response JSON:
    Note: Each of these items are lists
    @file_name: A list of all of the file names
    @date: A list of all of the date
    """
    try:
        req = dict(request.GET.iterlists())
        correct_data = get_request_data(request)
        req = correct_data[0]
        inList = correct_data[1]
        if inList:
            u = req['user_id'][0]
            f = req['teacher'][0]
            p = req['period'][0]
        else:
            u = req.get('user_id', None)
            f = req.get('teacher', None)
            p = req.get('period', None)
        db_model = InvitesModel()
        errcode = db_model.get_invite(u, f, p)
        if errcode[2] == -1:
            res = {'errcode': errcode[2], 'file_name': None, 'date': None}
        else:
            res = {
                'errcode': errcode[2], 'file_name': errcode[0], 'date': errcode[1]}
        return HttpResponse(json.dumps(res), content_type='application/json')
    except Exception, ex:
        render(logging.exception("Something awful happened!"))

# In the next iteration we will implement this find the next room feature


def findRoom(request):
    """
    Request JSON:
    @username: The individual's username
    @invite_id: Check to see if there is an invite associated (if not, we will have None, else we will give an invite ID)

    If it is blank/no invite id, we will generate them a new "room" in the websocket server 
    else: we will find the existing room that was created when the room was created

    NOTE: This could be optimized in the future by delaying the creation of the room until the user needs it 

    Response JSON:
    @error_code: 1 if success, -1 if not success

    We will need to write a controller for the websocket to split broadcasting tasks

    Also, we should make a mock where people can see the websocket working live with
    (THIS SHOULD BE PRIORITIZED BEFORE FIND ROOM!)
    """
    return

    """
    Get's the appropriate data from the US

    returns the correct response to be parsed
    returns a list with 2 items
    @return: correct request
    @return: If the items are in a list or not (HTML objects come in a list)
    """


def get_request_data(request):
    if request.method == "GET":
        req = dict(request.GET.iterlists())
    else:
        req = dict(request.POST.iterlists())

    if (req == {}):
        data = json.loads(request.body)
        return [data, False]
    else:
        return [req, True]