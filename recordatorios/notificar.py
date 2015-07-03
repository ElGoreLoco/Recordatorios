import manejar
from gi.repository import Notify
from time import localtime

Notify.init("Recordatorios")


def ejec():
    recordatorios = manejar.lista()
    #recordatorios[-1][1] = localtime().tm_year
    #recordatorios[-1][2] = localtime().tm_mon
    #recordatorios[-1][3] = localtime().tm_mday
    #recordatorios[-1][4] = localtime().tm_hour
    #recordatorios[-1][5] = localtime().tm_min

    for i in recordatorios:
        if i[1] == localtime().tm_year:
            if i[2] == localtime().tm_mon:
                if i[3] == localtime().tm_mday:
                    if i[4] == localtime().tm_hour:
                        if i[5] == localtime().tm_min:
                            notific = Notify.Notification.new(
                                i[0],
                                "Nuevo recordatorio.",
                                "recordatorios-logo"
                            )
                            notific.show()
                            return True
    return False
