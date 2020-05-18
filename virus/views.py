from django.shortcuts import render
import platform, datetime, pytz
from covid_india import states
# # Create your views here.


def home(request):
    sys_name = platform.node()
    if sys_name:
        c_name = sys_name
    else:
        c_name = "Guest user"
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    dt = current_time.strftime("%B %d, %Y %H:%M %p")
    return render(request, 'Home.html', {'c_name': c_name, 'dt': dt})


def calculator(request):
    return render(request, 'calculator.html')


# def zipfile(request):
#     if request.method == "POST":
#         form = Zipforms(request.POST, request.FILES)
#         if form.is_valid():
#             sub = request.FILES["file"]
#             print("11111111111111", sub)
#             subject = "NEW"
#             msg = sub
#             to = "zkindiard03@gmail.com"
#             res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
#             if (res == 1):
#                 msg = "Mail Sent Successfuly"
#             else:
#                 msg = "Mail could not sent"
#             return HttpResponse(msg)
#     else:
#         zip = Zipforms()
#         return render(request, 'zip.html', {'zip': zip})


def coronalive(request):
    if request.method == "GET":
        ap = states.getdata('Andhra Pradesh')
        Andaman = states.getdata('Andaman and Nicobar Islands')
        Arunachal = states.getdata('Arunachal Pradesh')
        Assam = states.getdata('Assam')
        Bihar = states.getdata('Bihar')
        Chandigarh = states.getdata('Chandigarh')
        Chhattisgarh = states.getdata('Chhattisgarh')
        Delhi = states.getdata('Delhi')
        Goa = states.getdata('Goa')
        Gujarat = states.getdata('Gujarat')
        Haryana = states.getdata('Haryana')
        Himachal = states.getdata('Himachal Pradesh')
        Jharkhand = states.getdata('Jharkhand')
        jk = states.getdata('Jammu and Kashmir')
        Karnataka = states.getdata('Karnataka')
        Kerala = states.getdata('Kerala')
        Ladakh = states.getdata('Ladakh')
        mp = states.getdata('Madhya Pradesh')
        Maharashtra = states.getdata('Maharashtra')
        Manipur = states.getdata('Manipur')
        Meghalaya = states.getdata('Meghalaya')
        Mizoram = states.getdata('Mizoram')
        Odisha = states.getdata('Odisha')
        Puducherry = states.getdata('Puducherry')
        Punjab = states.getdata('Punjab')
        Rajasthan = states.getdata('Rajasthan')
        tn = states.getdata('Tamil Nadu')
        Telengana = states.getdata('Telengana')
        Tripura = states.getdata('Tripura')
        Uttarakhand = states.getdata('Uttarakhand')
        up = states.getdata('Uttar Pradesh')
        wb = states.getdata('West Bengal')
        return render(request, 'corona.html', {'ap': ap, 'Andaman': Andaman, 'Arunachal': Arunachal, 'Assam': Assam,
                                               'Bihar': Bihar, 'Chandigarh': Chandigarh, 'Chhattisgarh': Chhattisgarh,
                                               'Delhi': Delhi, 'Goa': Goa, 'Gujarat': Gujarat, 'Haryana': Haryana,
                                               'Himachal': Himachal, 'jk': jk, 'Jharkhand': Jharkhand, 'Karnataka': Karnataka, 'Kerala': Kerala, 'Ladakh': Ladakh, 'mp': mp, 'Maharashtra': Maharashtra, 'Manipur': Manipur, 'Meghalaya': Meghalaya, 'Mizoram': Mizoram, 'Odisha': Odisha, 'Puducherry': Puducherry, 'Punjab': Punjab, 'Rajasthan': Rajasthan, 'tn': tn, 'Telengana': Telengana, 'Tripura': Tripura, 'Uttarakhand': Uttarakhand, 'up': up, 'wb': wb})

