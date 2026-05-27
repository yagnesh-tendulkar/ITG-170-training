class Device:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def power_on(self):
        print(f"{self.name} is being power on.")

class Mobile(Device):
    def __init__(self, name, model,os_name):
        super().__init__(name, model)
        self.os_name=os_name
        print(f"smart phone running on {self.os_name} phone is powering on ")

    def power_on(self):
        super().power_on()
        print(f"Loading {self.os_name} home screen")

indi_phone = Mobile("POCO","C3","Android")
indi_phone.power_on()