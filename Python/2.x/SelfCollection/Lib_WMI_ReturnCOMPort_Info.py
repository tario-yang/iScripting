import wmi

class WMI:

    def __init__(self):
        self.WMI = wmi.WMI()

    def osname(self):
        "Return current name of OS"
        for i in self.WMI.Win32_OperatingSystem():
            return i.Caption

    def batteryremaining(self):
        "Return the estimated charge remaining"
        for i in objWMI.Win32_Battery():
            return i.EstimatedChargeRemaining

    def comportlist(self):
        "Return the list of COM port(s) in current computer"
        """
        Properties are listed as follow,
            referring to http://msdn.microsoft.com/en-us/library/aa394413%28v=vs.85%29.aspx
                [Provider("CIMWin32")]class Win32_SerialPort : CIM_SerialController
                {
                  uint16   Availability;
                  boolean  Binary;
                  uint16   Capabilities[];
                  string   CapabilityDescriptions[];
                  string   Caption;
                  uint32   ConfigManagerErrorCode;
                  boolean  ConfigManagerUserConfig;
                  string   CreationClassName;
                  string   Description;
                  string   DeviceID;
                  boolean  ErrorCleared;
                  string   ErrorDescription;
                  datetime InstallDate;
                  uint32   LastErrorCode;
                  uint32   MaxBaudRate;
                  uint32   MaximumInputBufferSize;
                  uint32   MaximumOutputBufferSize;
                  uint32   MaxNumberControlled;
                  string   Name;
                  boolean  OSAutoDiscovered;
                  string   PNPDeviceID;
                  uint16   PowerManagementCapabilities[];
                  boolean  PowerManagementSupported;
                  uint16   ProtocolSupported;
                  string   ProviderType;
                  boolean  SettableBaudRate;
                  boolean  SettableDataBits;
                  boolean  SettableFlowControl;
                  boolean  SettableParity;
                  boolean  SettableParityCheck;
                  boolean  SettableRLSD;
                  boolean  SettableStopBits;
                  string   Status;
                  uint16   StatusInfo;
                  boolean  Supports16BitMode;
                  boolean  SupportsDTRDSR;
                  boolean  SupportsElapsedTimeouts;
                  boolean  SupportsIntTimeouts;
                  boolean  SupportsParityCheck;
                  boolean  SupportsRLSD;
                  boolean  SupportsRTSCTS;
                  boolean  SupportsSpecialCharacters;
                  boolean  SupportsXOnXOff;
                  boolean  SupportsXOnXOffSet;
                  string   SystemCreationClassName;
                  string   SystemName;
                  datetime TimeOfLastReset;
                };
        """
        comportlist = []
        for i in self.WMI.Win32_SerialPort():
            comportlist.append((i.Caption, i.DeviceID, i.Description, i.MaxBaudRate, i.PNPDeviceID, i.ProviderType))
        return comportlist
