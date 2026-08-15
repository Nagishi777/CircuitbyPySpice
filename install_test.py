from PySpice.Spice.NgSpice.Shared import NgSpiceShared

try:
    ng = NgSpiceShared.new_instance()
    print("OK: PySpice は ngspice を認識しています")
except Exception as e:
    print("NG: PySpice が ngspice を認識できません")
    print(e)