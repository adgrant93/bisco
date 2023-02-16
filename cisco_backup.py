from netmiko import ConnectHandler
class cisco:
    def __init__(self, username, password, host, device):
        self.username = username
        self.password = password
        self.host = host
        self.device = device
        self.net_connect = ConnectHandler(
            device_type = self.device,
            host = self.host,
            username = self.username,
            password = self.password,
        )

    def sh_version(self):
        return ("sh version1",self.net_connect.send_command("sh version"))
    def sh_module(self):
        return ("sh module1",self.net_connect.send_command("sh module"))
    def sh_env(self):
        return ("sh environment1", self.net_connect.send_command("sh environment"))
    def sh_run(self):
        return ("sh run1", self.net_connect.send_command("sh run"))
    def sh_boot(self):
        return ("sh boot1", self.net_connect.send_command("sh boot"))
    def dir_bootflash(self):
        return ("dir bootflash:1", self.net_connect.send_command("dir bootflash:"))
    def sh_ip_int_br(self):
        return ("sh ip int br1", self.net_connect.send_command("sh ip int br"))
    def sh_int_br(self):
        return ("sh int br1", self.net_connect.send_command("sh int br"))
    def sh_int_trunk(self):
        return ("sh int trunk1", self.net_connect.send_command("sh int trunk"))
    def sh_vlans(self):
        return ("sh vlans1", self.net_connect.send_command("sh vlans"))
    def sh_spanning_tree_summary(self):
        return ("sh spanning-tree summary1", self.net_connect.send_command("sh spanning-tree summary"))
    def sh_port_channel_summary(self):
        return ("sh port-channel summary1", self.net_connect.send_command("sh port-channel summary"))
    def sh_vpc(self):
        return ("sh vpc1", self.net_connect.send_command("sh vpc"))
    def sh_vpc_peer_keepalive(self):
        return ("sh vpc peer-keepalive1", self.net_connect.send_command("sh vpc"))
    def boot_var(self):
        return ("sh boot var1", self.net_connect.send_command("sh boot var"))
    def sh_cdp_neighbors(self):
        return ("sh cdp neighbors1", self.net_connect.send_command("sh cdp neighbors"))
    def sh_logging(self):
        return ("sh logging1", self.net_connect.send_command("sh logging"))
    def sh_inventory(self):
        return ("sh inventory1", self.net_connect.send_command("sh inventory"))
    def sh_run_all(self):
        return("sh run all", self.net_connect.send_command("sh run all"))
    def sh_vpc_brief(self):
        return("sh vpc brief", self.net_connect.send_command("sh vpc brief"))
class nxos(cisco):
    def __init__(self, username, password, host, device):
        super().__init__(username, password, host, device)

    def full_backup(self):
        commands1 = (
            self.sh_version(),
            self.sh_module(),
            self.sh_env(),
            self.sh_run(),
            self.sh_boot(),
            self.dir_bootflash(),
            self.sh_ip_int_br(),
            self.sh_int_br(),
            self.sh_int_trunk(),
            self.sh_vlans(),
            self.sh_spanning_tree_summary(),
            self.sh_port_channel_summary(),
            self.sh_vpc(),
            self.sh_vpc_peer_keepalive(),
            self.boot_var(),
            self.sh_cdp_neighbors(),
            self.sh_logging(),
            self.sh_inventory(),
            self.sh_run_all(),
            self.sh_vpc_brief
        )
        for i in commands1:
            my_file = open(i[0], "w")
            my_file.write(i[1])
