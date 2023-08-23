from django.urls import path

from budget import views
urlpatterns=[
    path('',views.main,name="main"),
    path('reg',views.reg,name="reg"),
    path('reg1', views.reg1, name="reg1"),
    path('addofficer',views.addofficer,name="addofficer"),
    path('addwork', views.addwork, name="addwork"),
    path('addmanageofficer', views.addmanageofficer, name="addmanageofficer"),
    path('addmanagework', views.addmanagework, name="addmanagework"),
    path('homepage', views.homepage, name="homepage"),
    path('sentnotification', views.sentnotification, name="sentnotification"),
    path('verifycontractor', views.verifycontractor, name="verifycontractor"),
    path('viewreport', views.viewreport, name="viewreport"),
    path('viewworkstatus', views.viewworkstatus, name="viewworkstatus"),
    path('addreport', views.addreport, name="addreport"),
    path('homecontractor', views.homecontractor, name="homecontractor"),
    path('reports', views.reports, name="reports"),
    path('request', views.request, name="request"),
    path('homepage', views.homepage, name="homepage"),
    path('update/<int:id>', views.update, name="update"),
    path('updateworkstatus', views.updateworkstatus, name="updateworkstatus"),
    path('viewinstruction', views.viewinstruction, name="viewinstruction"),
    path('viewnotification', views.viewnotification, name="viewnotification"),
    path('viewworkrqst', views.viewworkrqst, name="viewworkrqst"),
    path('homeofficer', views.homeofficer, name="homeofficer"),
    path('viewcontractor', views.viewcontractor, name="viewcontractor"),
    path('viewofficernoti', views.viewofficernoti, name="viewofficernoti"),
    path('viewofficerreport', views.viewofficerreport, name="viewofficerreport"),
    path('instruction1/<int:id>', views.instruction1, name="instruction1"),
    path('viewstatus', views.viewstatus, name="viewstatus"),
    path('addinstruction', views.addinstruction, name="addinstruction"),
    path('regcode', views.regcode, name="regcode"),
    path('regcode2', views.regcode2, name="regcode2"),
    path('verifysup',views.verifysup,name='verifysup'),
    path('verifysup1/<int:id>', views.verifysup1, name='verifysup1'),
    path('rejectsup/<int:id>', views.rejectsup, name='rejectsup'),
    path('homesup', views.homesup, name='homesup'),
    path('addprod', views.addprod, name='addprod'),
    path('mngprod', views.mngprod, name='mngprod'),
    path('addprod1', views.addprod1, name='addprod1'),
    path('deleteprod/<int:id>', views.deleteprod, name='deleteprod'),
    path('vcompany', views.vcompany, name='vcompany'),
    path('chat1/<int:id>', views.chat1, name='chat1'),
    path('chat_s', views.chat_s, name="chat_s"),
    path('chat2', views.chat2, name='chat2'),
    path('vsup', views.vsup, name='vsup'),
    path('chat11/<int:id>', views.chat11, name='chat11'),
    path('chat_ss', views.chat_ss, name="chat_ss"),
    path('chat22', views.chat22, name='chat22'),
    path('vprod', views.vprod, name='vprod'),
    path('vprod1', views.vprod1, name='vprod1'),
    #  path('', views., name=''),
    # path('', views., name=''),
    path('logincode', views.logincode, name="logincode"),
    path('officercode', views.officercode, name="officercode"),
    path('viewrqstverify', views.viewrqstverify, name="viewrqstverify"),
    path('workcode', views.workcode, name="workcode"),
    path('rejectcontractor/<int:id>', views.rejectcontractor, name="rejectcontractor"),
    path('verifycontractor1/<int:id>', views.verifycontractor1, name="verifycontractor1"),
    path('notifications', views.notifications, name="notifications"),
    path('notisent', views.notisent, name="notisent"),
    path('workrqst/<int:id>', views.workrqst, name="workrqst"),
    path('workreject/<int:id>', views.workreject, name="workreject"),
    path('searchwithdate', views.searchwithdate, name="searchwithdate"),
    path('reportts', views.reportts, name="reportts"),
    path('viewanddwnmloadreport', views.viewanddwnmloadreport, name="viewanddwnmloadreport"),
    path('updateofficer', views.updateofficer, name="updateofficer"),
    path('editofficer/<int:id>', views.editofficer, name="editofficer"),
    path('deletedofficer/<int:id>', views.deletedofficer, name="deletedofficer"),
    path('instructions/<int:id>', views.instructions, name="instructions"),
    path('instruct', views.instruct, name="instruct"),
    path('updatewrkstatus', views.updatewrkstatus, name="updatewrkstatus"),
    path('searchwithcontractor', views.searchwithcontractor, name="searchwithcontractor"),
    path('editreport/<int:id>', views.editreport, name="editreport"),
    path('updatereport', views.updatereport, name="updatereport"),
    path('deletedreport/<int:id>', views.deletedreport, name="deletedreport"),
    path('workrequest/<int:id>', views.workrequest, name="workrequest"),
    path('deletework/<int:id>', views.deletework, name="deletework"),
    path('editwork/<int:id>', views.editwork, name="editwork"),
    path('updateworks', views.updateworks, name="updateworks"),
    path('adminwrlkstatusview', views.adminwrlkstatusview, name="adminwrlkstatusview"),
    path('sendrequestforwork', views.sendrequestforwork, name="sendrequestforwork"),
    path('logout', views.logout, name="logout"),
    path('prediction/<int:id>', views.prediction, name="prediction"),
    path('predictionbudget', views.predictionbudget, name="predictionbudget"),





































]