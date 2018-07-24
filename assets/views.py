from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Asset
from .models import Server
from .models import NetworkDevice
from .models import  StorageDevice
from .models import  SecurityDevice
from .models import  Software

# Create your views here.

def index(request):
    assets = Asset.objects.all()
    return render(request, 'assets/index.html', locals())

def dashboard(request):
    total      = Asset.objects.count()
    upline     = Asset.objects.filter(status=0).count()
    offline    = Asset.objects.filter(status=1).count()
    unknown    = Asset.objects.filter(status=2).count()
    breakdown  = Asset.objects.filter(status=3).count()
    backup     = Asset.objects.filter(status=4).count()
    up_rate    = round(upline/total*100)
    o_rate     = round(offline/total*100)
    un_rate    = round(unknown/total*100)
    bd_rate    = round(breakdown/total*100)
    bu_rate    = round(backup/total*100)

    server_number         = Server.objects.count()
    networkdevice_number  = NetworkDevice.objects.count()
    storagedevice_number  = StorageDevice.objects.count()
    securitydevice_number = SecurityDevice.objects.count()
    software_number       = Software.objects.count()

    return render(request, 'assets/dashboard.html', locals())

def detail(request, asset_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    asset = get_object_or_404(Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())